## macos-python-notify-webservice

Simple Web service to Send Notifications to MacOS via (Remote) HTTP call.


![Demo](https://raw.githubusercontent.com/ggtd/macos-python-notify-webservice/master/README.images/notifiy_demo_curl_1.jpg "Demo")


# Configuration
- set IP of server
- check port

# Usage Example

curl 'http://127.0.0.1:8090/?t=title&st=subtitle&m=message+abc+xyz'

### or

curl 'http://127.0.0.1:8090/?t=title&m=message+abc+xyz&f=1'

Please Note: Use + as 'space' in Title and Body URL part, when making the request.

#### URL parameters
&t=some+title

&st=some+sub+title

&m=some+message

#### Force message ('f' url parameter)
By default, repeating notifications are not displayed. Uset the URL parameter 'f' to change this behavior.

If the '&f=' parameter is used in URL (any non-empty value). All notifications are displayed, even repeating messages.


## TODO:
- [ ] run on startup script
- [ ] install script
- [ ] Add "say" command call. To say something passed via HTTP


## Security Warning:
- Use this on you own risk!
- set HOST IP address to your local(home) network. Configure your LAN/MAC firewall accordingly!

