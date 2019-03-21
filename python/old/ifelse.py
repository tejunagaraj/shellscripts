#!/usr/bin/env python
# This is some secure program which uses security

import sys

validpassword = 'secret' # This is our password

inputpassword = raw_input('Please enter password: ')

if inputpassword == validpassword:
	print 'You have access!'
else:
	print 'Access denied!'
	sys.exit(0)

print 'Welcome!'
