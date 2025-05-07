#Write a python program to find whether a given string is a palindrome or not
str = input()
if str == str[::-1]:
	print("palindrome")
else :
	print("not a palindrome")
