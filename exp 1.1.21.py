#Write a program to print the sum of digits of a number.
n = int(input("num: "))
i = n
sum = 0
while i > 0:
	sum = sum + i%10
	i=int(i/10)
print("sum:",sum)
