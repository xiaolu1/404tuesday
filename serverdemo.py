#!/usr/bin/env python

# Copyright (c) Xiaolu Wang

import socket, os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#12345: number greater than 1024
#0.0.0.0: all IP address in the computer
serverSocket.bind(("0.0.0.0", 12345))
serverSocket.listen(5)

#curl localhost:12345
#telnet localhost 12345
while True:
	(incomingSocket, address) = serverSocket.accept()

	childPid = os.fork()
	if (childPid != 0):
		#we must be still in the connection accepting process
		#continue: go back to while and loop again
		continue
	#we must be in a client talking process
	#print str(address)

	outgoingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	outgoingSocket.connect(("www.google.com", 80))

	done = False
	while not done:
		#fix cpu use with poll() or select()
		incomingSocket.setblocking(0)
		try:
			part = incomingSocket.recv(2048)
		except IOError, exception:
			if (exception.errno == 11):
				part = None
			else:
				raise
		if (part):
			outgoingSocket.sendall(part)

		outgoingSocket.setblocking(0)
		try:
			part = outgoingSocket.recv(2048)
		except IOError, exception:
			if (exception.errno == 11):
				part = None
			else:
				raise
		if (part):
			incomingSocket.sendall(part)
	
