import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 
sock.connect(('127.0.0.1',port))
data = sock.recv(4096)

sock.close()

print(data.decode())
