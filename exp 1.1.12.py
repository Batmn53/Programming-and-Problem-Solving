#Write a python program to print factorial of given number.
def fact(a) :
	return 1 if a <= 0 else a * fact(a-1);
x = int(input("Enter a number : "))
if x >= 0 :
	print(f"Factorial of given number is : {fact(x)}")
else :
	print("Enter a positive number")
