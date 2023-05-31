print("\n\n\t\t *** Employee Performance Evaluation Expert System ***\n")

questions=[
    'What is your name? ',
    'what is your emop id? ',
    'What is your job title? ',
    'How many years experience do you have? ', 
    'Rate your communication skill on scale of 1-10 : ',
    'Rate your teamwork-skills on scale of 1-10 : ',
    'Rate your problem solving on scale of 1-10 : ',
    'Rate your tech-skills onn scale of 1-10 : ',
    'Rate your overall performance onn scale of 1-10 : ',
]

employees=[]
num_emp=2
employee_datails={}

for i in range(num_emp):
    print(f"\n\t\t--- Employee {i+1} ---")
    employee_responses={}

    for i in questions:
        answer=input('\n\t'+i)
        employee_responses[i]=answer
    
    total_score=(
        int(employee_responses[questions[4]])+
        int(employee_responses[questions[5]])+
        int(employee_responses[questions[6]])+
        int(employee_responses[questions[7]])+
        int(employee_responses[questions[8]])
    )
    employee_datails={
        'Name':employee_responses[questions[0]],
        'Emp id':employee_responses[questions[1]],
        'Job Title':employee_responses[questions[2]],
        'Years of Experience':employee_responses[questions[3]],
        'Total score':total_score
    }

    employees.append(employee_datails)
    

print('emp: ',employees)
best_performer=max(employees, key=lambda x: x["Total score"])
print('Best Performer is : ',best_performer)
