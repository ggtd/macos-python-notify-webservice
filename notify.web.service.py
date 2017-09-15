#!/usr/bin/env python


# Simple Web service to Send Notifications to MacOS via (Remote) HTTP call.
# by: Tomas Dobrotka ( www.dobrotka.sk )
# v0.1 - 15.09.2017


import time
import BaseHTTPServer
import urlparse
import hashlib
from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter


#WARNING: Use this only on your own risk. Consider changing 0.0.0.0 to your IP and configure your LAN/MAC firewall accordingly.


HOST = '0.0.0.0' #Or better use your DHCP IP on LAN
PORT_NUMBER = 8090


def macodNotification(TITLE='',SUBTITLE='',MESSAGE='',SOURCE='',FORCE=0):
    TITLE=TITLE.strip()
    SUBTITLE=SUBTITLE.strip()
    MESSAGE=MESSAGE.strip()
    SOURCE=SOURCE.strip()

    # if title or message are empty: stop/return
    if (TITLE=='' or MESSAGE==''):
        return false

    # Make Uniqe message ID
    m = hashlib.md5()
    m.update(TITLE)
    m.update(MESSAGE)
    m.update(SUBTITLE)
    m.update(SOURCE)
    MESSAGE_UNIQE_ID=m.hexdigest()

    notification = NSUserNotification.alloc().init()
    notification.setTitle_(TITLE)
    notification.setSubtitle_(SUBTITLE)
    print SUBTITLE
    if SUBTITLE<>'':
        notification.setSubtitle_(SUBTITLE)
    notification.setInformativeText_(MESSAGE)
    if FORCE<>1:
        notification.setIdentifier_(MESSAGE_UNIQE_ID)

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)
    return MESSAGE_UNIQE_ID


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        param = urlparse.parse_qs(urlparse.urlparse(s.path).query)
        try:
            title=param['t']
        except:
            title=''
        try:
            subtitle=param['st']
        except:
            subtitle=''
        try:
            message=param['m']
        except:
            message=''
        try:
            if param['f']<>'':force=1
        except:
            force=0
        res=macodNotification(TITLE=str(title[0]),SUBTITLE=str(subtitle[0]), MESSAGE=str(message[0]),FORCE=force)
        s.wfile.write(res)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT_NUMBER)
    macodNotification(TITLE='Notification WebService', MESSAGE="Server Start - "+str(HOST)+":"+str(PORT_NUMBER),FORCE=1)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    macodNotification(TITLE='Notification WebService', MESSAGE="Server Stops - "+str(HOST)+":"+str(PORT_NUMBER))
