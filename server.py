# Import socket module
from socket import *
import sys  # In order to terminate the program


host = '10.0.2.15'
port = 8888

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
print('Socket created')

# Prepare a server socket
try:
    serverSocket.bind((host, port))
except error as msg:
    print ('Bind failed. Message: ' + str(msg))
    sys.exit()
print ('Socket bind complete')

# Listen for connections
serverSocket.listen(1)
print ('Socket now listening')

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    try:
        message = connectionSocket.recv(1024)
        # print(message)
        filename = message.split()[1]
        # print (list(filename))
        # print (filename)
        # print (type(filename[1:]))
        f = open(filename[1:])

        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        print ('IOError')
        # Send response message for file not found
        connectionSocket.send('404 Not Found ')

        # Close client socket
        connectionSocket.close()

# Close server socket
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
