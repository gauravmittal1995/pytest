#!/usr/bin/python
'''
	Test Runner
'''

from re import findall
import sys
from interpreter import interpret

filename = sys.argv[1]
if filename.split(".")[-1] != "pyt":
	print "Not A valid File. Should be a .pyt file"
else:
	f = open(filename, 'r')
	for line in f:
		words = findall(r"\S+(?:\s\S+)*", line)
		interpret(words)
