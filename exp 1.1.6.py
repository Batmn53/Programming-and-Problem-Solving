#Write a python program to find the largest of three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a > b :
	if a > c :
		largest = a
	else : largest = c
else :
	if b > c : largest = b
	else : largest = c
print(f"Largest number: {largest:.1f}")
