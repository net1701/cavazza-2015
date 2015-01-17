#!/usr/bin/python

import RPi.GPIO as GPIO
import socket

UDP_IP = "192.168.150.2"
UDP_PORT = 22001
GPIO_PINS = [3, 5]
GPIO_STATE = {}


for pin in GPIO_PINS:
	GPIO_STATE[pin] = False;

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
	for pin in GPIO_PINS:
		x = GPIO.input(pin)
		if GPIO_STATE[pin] != x:
			GPIO_STATE[pin] = x
			if x:
				sock.sendto(str(pin), (UDP_IP, UDP_PORT))
				print pin

