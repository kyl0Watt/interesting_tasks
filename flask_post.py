#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
import random

random.seed = 1
secret_number = random.randint(0, 100)

app = Flask(__name__)
app.config.update(
	DEBUG=False
	)

def game(number, secret_number):
	if number == secret_number:
		return 'You win! The secret number is {}'.format(secret_number)
	elif number > secret_number:
		return 'The secret number is smaller than {}'.format(number)
	elif number < secret_number:
		return 'The secret number is bigger than {}'.format(number)


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return 'Gues the secret number game', 200
	if request.method == 'POST':	
		try:
			r = request.form
			if r['number']:
				n = int(r['number'])
				return game(n, secret_number), 200
		except Exception as e:                                       # i can't catch BadRequestKeyError ((( i don't know why
			return 'You shold send you gues in key "number" and this is must be a number', 400

		else:
			return 'Something go wrong', 400



if __name__ == '__main__':
	app.run()