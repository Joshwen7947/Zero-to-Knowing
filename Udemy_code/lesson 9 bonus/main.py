def terminal_1():
    print("Departing from terminal 1 - Budget")
    flight_check()
    
def terminal_2():
    print("Departing from terminal 2 - Domestic")
    flight_check()
    
def terminal_3():
    print("Departing from terminal 3 - International")
    flight_check()
    
def flight_check():
    answer = input("Budget/Domestic/International: ").lower()
    if answer == 'budget':
        terminal_1()
    elif answer == 'domestic':
        terminal_2()
    elif answer == 'international':
        terminal_3()
    else:
        print("No other terminal")

flight_check()

######################################################

def calc_bmi(weight, height):
    calculation = weight / (height *height)
    return calculation

def results(weight, height):
    calculate = calc_bmi(weight, height)
    if calculate <= 18.5:
        print("Under weight!")
    elif calculate > 18.5 and calculate <= 25:
        print("Normal weight")
    else:
        print("Overweight")
        
        
people = int(input("Enter number of people: "))
for i in range(people):
    weight = float(input("Enter weight: "))  
    height = float(input("Enter height: "))
    results(weight, height)
        
        
