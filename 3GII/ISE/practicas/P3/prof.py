#!/usr/bin/env python3
import profile

def fib(n):
	if n == 0:
		return 0

	elif n == 1:
		return 1

	else:
		return fib(n-1)+fib(n-2)

def loop():
	n = 0
	while n < 10000000:
		n = n+1

def main():
	print ("IN LOOP")
	loop()
	print("FIB(30)")
	print("El término fib(30) es", fib(30))

profile.run('main()')
