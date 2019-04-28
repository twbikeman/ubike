import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(hostname)
print(ipaddr)