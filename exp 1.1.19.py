#Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.
import string
sentence = input()
sen = ''.join(char for char in sentence if char not in string.punctuation)
print(sen)
