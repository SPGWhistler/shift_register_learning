#!/usr/bin/env python

import CHIP_IO.GPIO as GPIO
import time

LATCH="CSID2"

GPIO.setup(LATCH, GPIO.OUT)

GPIO.output(LATCH, GPIO.HIGH);
