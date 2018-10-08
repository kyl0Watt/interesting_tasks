#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# in this task i recive page from link and print all links in tag 'a'
# for test regex i use https://pythex.org/

import requests
import re

page = 'http://habr.com'

get_page = requests.get(page)
text = get_page.text

result = re.findall(r'<a href="(http[^\s]*)"', text)

print('I find {} link on this page:\n'.format(len(result)))

for x in range(0, len(result)):
	print('{} link is: {}'.format(x+1, result[x]))
