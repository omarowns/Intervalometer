#!/usr/bin/python
from time import sleep

class Parameter:

	# Delay menu parameters
	DELAY_H	= 	0 # Hours
	DELAY_M	=	0 # Minutes
	DELAY_S =	0 # Seconds

	# Longevity menu parameters
	LONG_H 	= 	0 # Hours
	LONG_M 	= 	0 # Minutes
	LONG_S 	= 	0 # Seconds

	# Interval menu parameters
	INTER_H =	0 # Hours
	INTER_M =	0 # Minutes
	INTER_S =	0 # Seconds

	# Length menu parameters
	LENG_H 	= 	0 # Hours
	LENG_M 	= 	0 # Minutes
	LENG_S 	= 	0 # Seconds

	# Number of shots to take
	N = 0

	def __init__(self, n = 0):
		self.N = n
