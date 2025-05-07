#Write a Python program that prints prime numbers less than n which represents the upper limit.
import math
n = int(input("Enter upper limit: "))
def isPrime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True
for i in range(2,n+1):
	if isPrime(i):
		print(f"{i}")
