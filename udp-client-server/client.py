import socket

serverName = 'localhost'
serverPort = 12000
bufferSize = 2048

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
message = 'hola'

clientSocket.sendto(str.encode(message), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize)

print(modifiedMessage)
print(serverAddress)

clientSocket.close()