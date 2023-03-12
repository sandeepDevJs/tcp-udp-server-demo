import socket

serverPort = 12000
bufferSize = 2048

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))

serverSocket.listen(1)

print("server is ready!")

while 1: 
   connectionSocket, addr  = serverSocket.accept()
   message = connectionSocket.recv(bufferSize)
   capitalizedMessage = message.upper()

   connectionSocket.send(capitalizedMessage)
   connectionSocket.close()