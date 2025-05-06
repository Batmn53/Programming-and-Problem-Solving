#Write a program to calculate the area of a circle and print the result as shown in the displayed test cases.
a = float(input("Enter the radius : "))
area = 3.14 * a * a
if a >= 0.0 and a <= 100.0 :
	print(f"Area of circle = {area:.6f}")
else :
	print("Enter a positive value upto 100")
