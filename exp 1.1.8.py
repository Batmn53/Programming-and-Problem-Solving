#Write a Python program to perform union, intersection and difference operations on Set A and Set B.
a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)
print(f"Union:  {A | B}")
print(f"Intersection:  {A & B}")
print(f"Difference:  {A - B}")
