import sipfullproxy
import socketserver
import socket

sipfullproxy.registrar = {}

hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
print(ipaddress)

sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)

server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
server.serve_forever()

