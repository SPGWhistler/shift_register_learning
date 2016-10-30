#!/usr/bin/env python
#1016 = data = XIO-P0	XIO-P0	U14_13
#1018 = clock = XIO-P2	GPIO1	U14_15
#1020 = latch = XIO-P4	GPIO3	U14_17

import CHIP_IO.GPIO as GPIO
import time

dataBit = "CSID0"
LATCH = "CSID1"
CLK = "CSID2"

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

def ssrWrite(value):
	for x in range(0, 16):
		if value == x:
			GPIO.output(dataBit, GPIO.HIGH)
		else:
			GPIO.output(dataBit, GPIO.LOW)
		pulseCLK()
	serLatch()
	return

while 1:
	temp = 0
	for j in range(0, 16):
		ssrWrite(temp)
		temp = temp + 1
		time.sleep(.5)

	for j in range(0, 16):
		temp = temp - 1
		ssrWrite(temp)
		time.sleep(.5)
