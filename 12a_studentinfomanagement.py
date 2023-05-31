# This is simplest Student data management program in python

# Create class "Student"
class Student:

# Constructor
	def __init__(self, name, rollno, m1, m2):
		self.name = name
		self.rollno = rollno
		self.m1 = m1
		self.m2 = m2

	# Function to create and append new student
	def accept(self, Name, Rollno, marks1, marks2):

# use ' int(input()) ' method to take input from user
		ob = Student(Name, Rollno, marks1, marks2)
		ls.append(ob)

	# Function to display student details
	def display(self, ob):
		print("Name : ", ob.name)
		print("RollNo : ", ob.rollno)
		print("Marks1 : ", ob.m1)
		print("Marks2 : ", ob.m2)
		print("\n")

	# Search Function
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i

	# Delete Function
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

	# Update Function
	def update(self, rn, No):
		i = obj.search(rn)
		roll = No
		ls[i].rollno = roll


# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
	obj.display(ls[i])

# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])

# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
	obj.display(ls[i])

# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
	obj.display(ls[i])

# else:
print("Thank You !")


'''
This code implements a simple student data management program in Python. Here's the breakdown of the code with comments and explanations:

```python
# Create class "Student"
class Student:
	# Constructor
	def __init__(self, name, rollno, m1, m2):
		self.name = name
		self.rollno = rollno
		self.m1 = m1
		self.m2 = m2

	# Function to create and append new student
	def accept(self, Name, Rollno, marks1, marks2):
		# Create a new Student object with the provided details
		ob = Student(Name, Rollno, marks1, marks2)
		# Append the new student object to the list 'ls'
		ls.append(ob)

	# Function to display student details
	def display(self, ob):
		print("Name : ", ob.name)
		print("RollNo : ", ob.rollno)
		print("Marks1 : ", ob.m1)
		print("Marks2 : ", ob.m2)
		print("\n")

	# Search Function
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i

	# Delete Function
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

	# Update Function
	def update(self, rn, No):
		i = obj.search(rn)
		roll = No
		ls[i].rollno = roll


# Create a list to add Students
ls = []
# Create an object of Student class
obj = Student('', 0, 0, 0)

# Perform operations
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")

# Accept student details
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

# Display student details
print("\nList of Students\n")
for i in range(ls.__len__()):
	obj.display(ls[i])

# Search for a student and display details
print("\nStudent Found, ")
s = obj.search(2)
obj.display(ls[s])

# Delete a student's details
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
	obj.display(ls[i])

# Update a student's details
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
	obj.display(ls[i])

print("Thank You !")
```

The code defines a `Student` class that represents a student's details. The class has methods for accepting student details, displaying student details, searching for a student, deleting a student's details, and updating a student's details.

The code uses an instance of the `Student` class named `obj` and a list named `ls` to store student objects.

The program performs the following operations:

1. Accepts student details by calling the `accept` method of the `Student` class. Three students with their respective details are added to the list.

2. Displays the list of students by calling the `display` method of the `Student` class for each student object in the list.

3. Searches for a student with a specific roll number (2) by calling the `search` method of the `Student` class. If found, the student details are displayed.

4. Deletes the details of

 a student with a specific roll number (2) by calling the `delete` method of the `Student` class. The updated list is then displayed.

5. Updates the details of a student with a specific roll number (3) by calling the `update` method of the `Student` class. The updated list is then displayed.

6. Prints a "Thank You!" message.

Note: The code is currently commented out for user input and uses pre-defined values for simplicity.

Output:
The output of the program will be the displayed student details, search results, and updated lists based on the performed operations.

Example output:
```
Operations used,

1.Accept Student details
2.Display Student Details
3.Search Details of a Student
4.Delete Details of Student
5.Update Student Details
6.Exit

List of Students

Name :  A
RollNo :  1
Marks1 :  100
Marks2 :  100


Name :  B
RollNo :  2
Marks1 :  90
Marks2 :  90


Name :  C
RollNo :  3
Marks1 :  80
Marks2 :  80


Student Found,
Name :  B
RollNo :  2
Marks1 :  90
Marks2 :  90


2
List after deletion
Name :  A
RollNo :  1
Marks1 :  100
Marks2 :  100


Name :  C
RollNo :  3
Marks1 :  80
Marks2 :  80


2
List after updation
Name :  A
RollNo :  1
Marks1 :  100
Marks2 :  100


Name :  C
RollNo :  2
Marks1 :  80
Marks2 :  80


Thank You !
```

In this example, three students are added with their respective details. The student with a roll number of 2 is found and displayed. Then, the student with a roll number of 2 is deleted, and the updated list is displayed. Finally, the details of the student with a roll number of 3 are updated, and the updated list is displayed.
'''