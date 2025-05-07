#Write a python profram to find the roots of a quadratic equation by taking the coefficients from the user
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
det = b*b-4*a*c
den = 2*a
if det < 0 :
	print(f"The roots are: {(-b/den):.2f}+{(math.sqrt(-det)/den):.2f}j and {(-b/den):.2f}{(-math.sqrt(-det)/den):.2f}j")
elif det == 0 :
	print(f"The root is: {(-b/(2*a)):.2f}")
else :
	print(f"The roots are: {((-b+math.sqrt(det))/den):.2f} and {((-b-math.sqrt(det))/den):.2f}")
