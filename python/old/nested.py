#!/usr/bin/python

var = 100
if var < 200:
	print "Expression value is less than 200"
	if var == 150:
		print "which is 150"
	elif var == 100:
		print "which is 100"
	elif var == 50:
		print "which is 50"
elif var < 50:
	print "expression value is less than 50"
else:
	print "could not find true expression"

print "good bye!"
