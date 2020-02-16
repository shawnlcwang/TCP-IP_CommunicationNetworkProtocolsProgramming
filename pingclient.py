import time
from socket import *

host = 'localhost'
port = 12000

num_pings = 10
sequence_number = 1

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)

def get_time():
    return time.time()

def wait_for_response():
    global sequence_number
    while True:
        try:
            message, address = clientSocket.recvfrom(1024)
	    print ('received: ' + message)
	    #print (type(message))
            return message
        except timeout as e:
	    print ('Request timed out'+'\n')
	    sequence_number = sequence_number + 1
    	    break


def send_message(message, wait=False):
    clientSocket.sendto(message, (host, port))
    if wait == False:
 	return
    else:
	return wait_for_response()

while sequence_number <= num_pings:
    message = 'PING ' + str(sequence_number) + ' ' + str(get_time())
    print (message)
    received = send_message(message, True)
    if received is not None:
    	#print (received)
    	received_array = received.split(' ')
    	#print (received_array)
    	received_type = received_array[0].upper()
    	received_seq = int(received_array[1])
    	received_time = float(received_array[2])
    	rtt = get_time() - received_time
    	print ('getTime: ' + str(get_time()))
    	print ('receivedTime: ' + str(received_time))
    	print ('rtt: ' + str(rtt))
    	if received_type == 'PING':
    	    print ('ping ' + str(sequence_number) + ' ' + str(rtt) + '\n')
    	    sequence_number = sequence_number + 1
	else:
	    print ('Unknown Error')
