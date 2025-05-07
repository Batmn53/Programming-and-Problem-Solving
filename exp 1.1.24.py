'''
Write a python program to define a module to find Fibonacci Numbers and 
import the module to another program.
Aim:
To create a Python program that generates a Fibonacci sequence up to a given 
maximum value.
Algorithm:
Step 1: Import the fibonacci_module.
Step 2: Accept an integer input from the user as the maximum value (n).
Step 3: If n is greater than 0:
Generate the Fibonacci sequence up to n using the generate_fibonacci_sequence() function from the fibonacci_module.
Print the generated Fibonacci series.
Step 4: If n is not greater than 0, print "Please enter a positive integer".
Step 5: End the program.
Note: The fibonacci_module contains the generate_fibonacci_sequence() function to generate the Fibonacci sequence up to a specified maximum value.
'''
import fibonacci_module
n = int(input("Enter the max value: "))
fibonacci_module.generate_fibonacci_sequence(n)
# print("Fibonacci series upto",n,":")
# for i in range(0,len(l)):
# 	print(f"{l[i]} ",end="")
