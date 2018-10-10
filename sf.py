#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
	return 'hello ' + user


@app.route('/add/<x>/<y>')
def add(x,y):
	return 'result of summ is ' + x + y  ##ahahah int(x) + int(y)


if __name__ == '__main__':
	app.run()