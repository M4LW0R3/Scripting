import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "172.26.176.1" # server address
port =12345 #server port
s.connect((host,port))
print (s.recv(1024))
