# Import socket module
from socket import *
import sys
import argparse

# Set arguments
host = sys.argv[1]
port = sys.argv[2]
path = sys.argv[3]

if len(sys.argv) != 4:
    print ('Usage: python %s <IP Address> <Port Number> <relative file path>' % (sys.argv[0]))
    sys.exit()

# Create a client socket
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
except error as msg:
    print ('Failed to create socket. Message: ' + str(msg))
    sys.exit()
print ('Socket created')

# Connect to remote server
try:
    clientSocket.connect((host, int(port)))
    print ('Socket Connect to ' + host)
except error as msg:
    print ('Socket connection failed: ' + str(msg))
    sys.exit()

# Send message data to remote server
message = path
try:
    clientSocket.sendall(message.encode())
except:
    print ('Send failed')
    sys.exit()
print ('Message send successfully')

# Recevie data from remote server
reply = clientSocket.recv(4096)
print (reply)

# Close client socket
clientSocket.close()
print ('Socket closed')