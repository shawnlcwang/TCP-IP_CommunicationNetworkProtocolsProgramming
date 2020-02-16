from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.uvic.ca", 25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO shawnlcwang\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mailFrom = "mail from: shawnlcwang@uvic.ca\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response. 
rcptTo = "rcpt to: <shawnlcwang@gmail.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send DATA command and print server response. 
data = "data\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send message data.
subject = "subject: from Shawn\r\n\r\n"
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024).decode()
print(recv_msg)

# Send QUIT command and get server response.
quit = "quit\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
clientSocket.close()
