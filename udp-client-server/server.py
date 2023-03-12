import socket

serverPort = 12000
bufferSize = 2048

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))

print("server is ready!")

while 1: 
    message, clientAddress = serverSocket.recvfrom(bufferSize);
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
    print(clientAddress)