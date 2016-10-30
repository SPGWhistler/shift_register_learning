#!/usr/bin/env python
#1016 = data = XIO-P0	XIO-P0	U14_13
#1018 = clock = XIO-P2	GPIO1	U14_15
#1020 = latch = XIO-P4	GPIO3	U14_17

import CHIP_IO.GPIO as GPIO
import time

dataBit = "CSID0"
LATCH = "CSID1"
CLK = "CSID2"

state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

GPIO.setup(LATCH, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(dataBit, GPIO.OUT)

GPIO.output(LATCH, GPIO.LOW);
GPIO.output(CLK, GPIO.LOW);

def pulseCLK():
	GPIO.output(CLK, GPIO.HIGH)
	GPIO.output(CLK, GPIO.LOW)
	return

def serLatch():
	GPIO.output(LATCH, GPIO.LOW)
	GPIO.output(LATCH, GPIO.HIGH)
	return

def sendBit(value):
	GPIO.output(dataBit, value)
	pulseCLK()
	return

def ssrWrite(p, newval):
	for pin, val in enumerate(state):
		if pin == p:
			sendBit(newval)
			state[pin] = newval
		else:
			sendBit(val)
	serLatch()
	return

ssrWrite(0, 1)
ssrWrite(1, 1)
ssrWrite(2, 1)
ssrWrite(3, 1)
ssrWrite(4, 1)
ssrWrite(5, 1)
ssrWrite(6, 1)
ssrWrite(7, 1)
ssrWrite(8, 0)
ssrWrite(9, 0)
ssrWrite(10, 0)
ssrWrite(11, 0)
ssrWrite(12, 0)
ssrWrite(13, 0)
ssrWrite(14, 0)
ssrWrite(15, 0)

#while 1:
	#temp = 0
	# This is just looping over each output, it doesn't have to be 16
	# for j in range(0, 16):
	# 	ssrWrite(temp)
	# 	temp = temp + 1
	# 	time.sleep(.5)

	# for j in range(0, 16):
	# 	temp = temp - 1
	# 	ssrWrite(temp)
	# 	time.sleep(.5)
