import socket

serverName = 'localhost'
serverPort = 12000
bufferSize = 2048

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((serverName, serverPort))
message = 'hola'

clientSocket.send(str.encode(message))

modifiedMessage = clientSocket.recv(bufferSize)

print(modifiedMessage)

clientSocket.close()