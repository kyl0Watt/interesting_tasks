#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def sender(url, data):
	result = requests.post(url, data)
	return result.text

def main():
	url = str(input('url to post = '))
	while True:
		key = str(input('post key '))
		if key == 'exit':
			break
		value = int(input('post {}: value '.format(key)))
		data = {key:value}
		print('server answer: {}'.format(sender(url, data)))

if __name__ == '__main__':
	print('You can send only one string key and int valie\n')
	main()