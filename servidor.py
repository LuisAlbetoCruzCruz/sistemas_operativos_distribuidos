import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 
sock.bind(('127.0.0.1',port)) 

print ("Esperando conexiones en el puerto ", port)

sock.listen(1)
con, client_addr=sock.accept()

print("Cliente conectado")

text = "Hola, soy el servidor!" 
con.send(text.encode())

print("Cliente desconectado")
con.close() 
sock.close()

