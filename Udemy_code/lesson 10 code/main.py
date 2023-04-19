from bmi import results

people = int(input("Enter number of people: "))
for i in range(people):
    weight = float(input("Enter weight: "))  
    height = float(input("Enter height: "))
    results(weight, height)


########################################################


from terminals import *
question = input("Would you like to check your flight: ").lower()
while question != 'quit':
    if question == 'yes':
        flight_check()
    else:
        print("You did not say yes...")
    question = input("Would you like to check your flight: ").lower()

########################################################

from payscale import *
account = int(input("1 - start, 2 - end: "))
while account != 2:
    employee = input("Enter name: ")
    employee_type = input("Salary or Hourly: ").lower()
    if employee_type == 'hourly':
        time = float(input("Enter hours worked this month: "))
        pay = part_time(time)
    elif employee_type == 'salary':
        exp = int(input("Enter years worked: "))
        pay = salary(exp)
    else:
        print("You are unemployeed...")
    print(employee,"-salary:",pay)
    account = int(input("1 - start, 2 - end: "))

    
    