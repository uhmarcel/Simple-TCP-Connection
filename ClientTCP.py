import socket
import sys

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('localhost', 10000)

print('Connecting to server', serverAddress[0], 'at port', serverAddress[1]) 
socketClient.connect(serverAddress)

try:
	print('Enter input to send to server: ')
	userInput = input()
	
	print('Sending message...')
	socketClient.sendall(str.encode(userInput))

	sizeExpected = len(userInput)
	serverResponse = socketClient.recv(sizeExpected)
	
	print('Server response:', serverResponse)

finally:
    print('Closing socket')
    socketClient.close()