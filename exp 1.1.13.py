'''
Write a Python program to print the following pattern.

Sample Input and Output:
Enter a number : 6
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
n = int(input("Enter a number : "))
for i in range(n, 0, -1):
	for j in range(i, 0, -1):
		print("* ",end="")
	print("")
