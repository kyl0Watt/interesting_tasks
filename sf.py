#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
	return 'hello ' + user


@app.route('/add/<x>/<y>')
def add(x,y):
	return 'result of summ is ' + x + y  ##ahah + (int(x) + int(y))


@app.route('/file/<file>')
def trytoopen(file = None):
	if file is None:                     # when will it run???
		return 'try /file/file_name'
	try:
		f = open(file)
		if file == 'sf.py':
			r = f.read()
			f.close()
			return r
		else:
			f.close()
			return 'File {} exist'.format(file)
	except FileNotFoundError:
		return 'File {} does not exist! try /file/sf.py or 1.txt'.format(file)


if __name__ == '__main__':
	app.run()