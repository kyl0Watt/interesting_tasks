#!/usr/bin/env puthon3
# -*- coding: utf8 -*-

# In this task i recive information from /proc/cpuinfo
# and print cpu model with regular expr

import sys
import re

# open file
file = open('/proc/cpuinfo', 'r')
cpuinfo = file.read()
file.close()

# and now re
cpu_re = re.search(r'model name\t: (.*)', cpuinfo)
cpu = cpu_re.group(1)

print('My cpu is {}'.format(cpu))
