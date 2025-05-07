'''
Write a Python program that functions as a simple phone book manager with a 
menu-driven interface. The program prompts the user to choose from the 
following options:

Add Contact
Remove Contact
Display
Quit


The program uses a dictionary to store contact information, where the contact 
name serves as the key and the associated phone number as the value. The user 
can add a contact, remove a contact, display the current contacts, or exit the 
program.
'''
dict = {}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")
	choice = int(input("Enter choice (1-4): "))
	match choice:
		case 1:
			name = input("Name: ").strip()
			number = input("Phone number: ")
			dict[name] = number
		case 2:
			name = input("Name: ").strip()
			if name in dict:
				del dict[name]
			else:
				print("Not found")
		case 3:
			print(dict)
		case 4:
			break
		case _:
			print("Invalid")
