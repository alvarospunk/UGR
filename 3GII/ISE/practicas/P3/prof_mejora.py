#!/usr/bin/env python3
import profile

def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
	return a

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
