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