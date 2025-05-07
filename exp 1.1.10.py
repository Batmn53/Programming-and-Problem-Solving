'''
Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system:



A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: Below 60


The program should display the average marks up to 2 decimal places and the assigned grade.
'''
a = [0]*5
sum = 0.0
for i in range(5):
	a[i]=float(input(f"subject {i+1}: "))
	sum += a[i]
av = sum/5
if av<=100 and av>=90:
	grade = 'A'
elif av<=89 and av>=80:
	grade = 'B'
elif av<=79 and av>=70:
	grade = 'C'
elif av>=60 and av<=69:
	grade = 'D'
else:
	grade = 'F'
print(f"Average Marks: {av:.2f}")
print(f"Grade: {grade}")
