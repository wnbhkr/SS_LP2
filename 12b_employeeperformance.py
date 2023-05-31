rules = {
    'rule1': {'Communication': 8, 'Productivity': 9, 'Output': 'Excellent'},
    'rule2': {'Communication': 7, 'Productivity': 9, 'Output': 'Good'},
    'rule3': {'Communication': 6, 'Productivity': 9, 'Output': 'Average'},
    'rule4': {'Communication': 8, 'Productivity': 6, 'Output': 'Good'},
    'rule5': {'Communication': 7, 'Productivity': 6, 'Output': 'Average'},
    'rule6': {'Communication': 6, 'Productivity': 6, 'Output': 'Poor'},
    'rule7': {'Communication': 8, 'Productivity': 3, 'Output': 'Average'},
    'rule8': {'Communication': 7, 'Productivity': 3, 'Output': 'Poor'},
    'rule9': {'Communication': 6, 'Productivity': 3, 'Output': 'Poor'},
}

class Employee:
    def __init__(self, name, productivity, teamwork, communication):
        self.name = name
        self.productivity = productivity
        self.teamwork = teamwork
        self.communication = communication

    def calculate_performance_score(self):
        performance_score = (self.productivity + self.teamwork + self.communication) / 3
        return performance_score

    def evaluate_performance(self):
        for rule, conditions in rules.items():
            if (
                conditions['Communication'] <= self.communication
                and conditions['Productivity'] <= self.productivity
            ):
                return conditions['Output']
        return 'Unknown'

    def display_employee_data(self):
        print("Employee Data:")
        print(f"Name: {self.name}")
        print(f"Productivity: {self.productivity}")
        print(f"Teamwork: {self.teamwork}")
        print(f"Communication: {self.communication}")

# Main program
def main():
    print("Employee Performance Evaluation")
    print("-------------------------------")
    name = input("Enter Employee Name: ")
    productivity = int(input("Enter Productivity rating (3/6/9): "))
    teamwork = int(input("Enter Teamwork rating (0-10): "))
    communication = int(input("Enter Communication rating (7-9): "))

    employee = Employee(name, productivity, teamwork, communication)
    performance_score = employee.calculate_performance_score()
    performance = employee.evaluate_performance()

    employee.display_employee_data()
    print(f"Performance Score: {performance_score}")
    print(f"Performance: {performance}")

# Run the main program
if __name__ == '__main__':
    main()

'''
Sure! Here's the code breakdown with comments and explanations:

```python
rules = {
    'rule1': {'Communication': 8, 'Productivity': 9, 'Output': 'Excellent'},
    'rule2': {'Communication': 7, 'Productivity': 9, 'Output': 'Good'},
    'rule3': {'Communication': 6, 'Productivity': 9, 'Output': 'Average'},
    'rule4': {'Communication': 8, 'Productivity': 6, 'Output': 'Good'},
    'rule5': {'Communication': 7, 'Productivity': 6, 'Output': 'Average'},
    'rule6': {'Communication': 6, 'Productivity': 6, 'Output': 'Poor'},
    'rule7': {'Communication': 8, 'Productivity': 3, 'Output': 'Average'},
    'rule8': {'Communication': 7, 'Productivity': 3, 'Output': 'Poor'},
    'rule9': {'Communication': 6, 'Productivity': 3, 'Output': 'Poor'},
}
```

The `rules` dictionary defines different evaluation rules based on the communication and productivity ratings of employees. Each rule is represented by a key-value pair, where the key is a rule name, and the value is a dictionary containing the required communication rating, productivity rating, and the corresponding output for that rule.

```python
class Employee:
    def __init__(self, name, productivity, teamwork, communication):
        self.name = name
        self.productivity = productivity
        self.teamwork = teamwork
        self.communication = communication

    def calculate_performance_score(self):
        performance_score = (self.productivity + self.teamwork + self.communication) / 3
        return performance_score

    def evaluate_performance(self):
        for rule, conditions in rules.items():
            if (
                conditions['Communication'] <= self.communication
                and conditions['Productivity'] <= self.productivity
            ):
                return conditions['Output']
        return 'Unknown'

    def display_employee_data(self):
        print("Employee Data:")
        print(f"Name: {self.name}")
        print(f"Productivity: {self.productivity}")
        print(f"Teamwork: {self.teamwork}")
        print(f"Communication: {self.communication}")
```

The `Employee` class represents an employee in the evaluation system. It has an initializer (`__init__`) that takes the employee's name, productivity rating, teamwork rating, and communication rating as input and assigns them to corresponding instance variables.

The `calculate_performance_score` method calculates the average performance score based on the productivity, teamwork, and communication ratings.

The `evaluate_performance` method evaluates the performance of an employee by iterating over the rules dictionary. It checks if the employee's communication rating is greater than or equal to the required communication rating and if the employee's productivity rating is greater than or equal to the required productivity rating. If a matching rule is found, it returns the corresponding output. If no matching rule is found, it returns 'Unknown'.

The `display_employee_data` method prints the employee's data, including the name, productivity rating, teamwork rating, and communication rating.

```python
def main():
    print("Employee Performance Evaluation")
    print("-------------------------------")
    name = input("Enter Employee Name: ")
    productivity = int(input("Enter Productivity rating (3/6/9): "))
    teamwork = int(input("Enter Teamwork rating (0-10): "))
    communication = int(input("Enter Communication rating (7-9): "))

    employee = Employee(name, productivity, teamwork, communication)
    performance_score = employee.calculate_performance_score()
    performance

 = employee.evaluate_performance()

    employee.display_employee_data()
    print(f"Performance Score: {performance_score}")
    print(f"Performance: {performance}")

if __name__ == '__main__':
    main()
```

The `main` function is the entry point of the program. It prompts the user to input the employee's name, productivity rating, teamwork rating, and communication rating. It creates an instance of the `Employee` class with the provided information.

The performance score is calculated using the `calculate_performance_score` method, and the performance is evaluated using the `evaluate_performance` method.

Finally, the employee's data, performance score, and performance are displayed to the user.

Output:
The program prompts the user for input and displays the employee's data, performance score, and performance based on the provided ratings.

Example output:
```
Employee Performance Evaluation
-------------------------------
Enter Employee Name: John
Enter Productivity rating (3/6/9): 9
Enter Teamwork rating (0-10): 8
Enter Communication rating (7-9): 7

Employee Data:
Name: John
Productivity: 9
Teamwork: 8
Communication: 7
Performance Score: 8.0
Performance: Good
```

In this example, an employee named John has a productivity rating of 9, a teamwork rating of 8, and a communication rating of 7. Based on the provided ratings, the performance score is calculated as 8.0, and the performance is evaluated as "Good" according to the defined rules.
'''

'''
database = [(1,'Nishant'),(2,'Swayam')]

name = input("Enter Name: ")
id = int(input("Enter id: "))

box = (id,name)

def knowledgeBase(total):
    percentage = ((total)/50)*100
    return percentage

if box in database:
    com = -1
    while com < 0 or com > 10 :
        com = int(input("Enter Communication skills:(0 to 10)"))
    
    tech = -1
    while tech < 0 or tech > 10:
        tech = int(input("Enter technical skill: "))
    
    manage = -1
    while manage < 0 or manage > 10:
        manage = int(input("Enter management skill: "))

    soft = -1
    while soft < 0 or soft > 10:
        soft = int(input("Enter other softskills: "))

    att = -1
    while att < 0 or att > 10:
        att = int(input("Enter other Attendence: "))
    
    total = com + tech + manage + soft + att
    percentage = knowledgeBase(total)

    if percentage < 20:
        print("poor performance")
    elif percentage < 50:
        print("Performance could be better")
    elif percentage < 80:
        print("Good Overall performacne")
    else:
        print("Excellent performance")
else:
    print("Employee Not in database! Please Search again! ")
'''