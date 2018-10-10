#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

def listensoc(port):
	sk = socket.socket()
	sk.bind(('', port))
	sk.listen(1)
	conn, addr = sk.accept()
	print('New connection from adress: ', addr)
	while True:
		data = conn.recv(1024)
		if not data:
			break
		print(data)
	conn.close()


if __name__ == '__main__':
	listensoc(5555)