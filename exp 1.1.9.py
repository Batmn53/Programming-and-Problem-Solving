#Write a Python program to check if a given year is a leap year or not.
y = int(input("Enter a year: "))
if y%4==0 :
	print(f"{y} is a leap year")
else :
	print(f"{y} is not a leap year")
