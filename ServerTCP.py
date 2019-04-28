import socket
import sys
import re

MAX_MSG_SIZE = 255

def removeNonAlphanumeric(byteMessage):
    msg = ''.join(map(chr, byteMessage))
    msgNonAlpha = ''.join([i for i in msg if i.isalnum()])
    return bytes(msgNonAlpha, 'utf-8')

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ('', 10000)

print('Starting server at port', serverAddress[1]) 
socketServer.bind(serverAddress)
socketServer.listen()

while True:

    print('Waiting for a client connection')
    connection, clientAddress = socketServer.accept()
	
    try:
        print('Connection from', clientAddress)

        while True:
            message = connection.recv(MAX_MSG_SIZE)
			
            if not message:
                break
            
            print('Received', message)
            response = removeNonAlphanumeric(message)

            print('Sending back answer:', response)
            connection.sendall(response)

    finally:
        connection.close()