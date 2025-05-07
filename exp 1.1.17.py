'''
Write a program to count the number of vowels using sets in a given string.
Input Format:
The program should prompt the user to enter the string.
Output Format:
The program should print the count of vowels present in the string.
'''
def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for c in str:
		if c in vowel:
			count+=1
	print(count)
str = input()
vowel_count(str)
