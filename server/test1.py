#!/usr/bin/python

import socket
import time

if(__name__ == "__main__"):
	port = 1234
	address = ('192.168.132.128',port)

	listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#listen_socket.setsockopt(socket.SOL_SOCKET,SO_REUSEADDR,1)
	listen_socket.bind(address)
	listen_socket.listen(1)

	print("Python HTTP server on port %d" %port)
	
	"""
	while True:
		time.sleep(1)
		print("hello")
	"""

	
	while True:
		client_connection,client_address = listen_socket.accept()
		request = client_connection.recv(2048)
		res = request.split("\r\n")[0].split(" ")[1].split('/')[1]
		if res == "add":
			str = 'HTTP/1.1 200 OK\r\n\r\n<html><body>add</body></html>'
			print("client",client_address,"request")
		elif res == "del":
			str = 'HTTP/1.1 200 OK\r\n\r\n<html><body>del</body></html>'
			print("client",client_address,"request")
		else:
			str = 'HTTP/1.1 200 OK\r\n\r\n<html><body>input error</body></html>'
		client_connection.send(str)
		client_connection.close()

	listen_socket.close()