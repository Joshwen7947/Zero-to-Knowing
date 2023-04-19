def grade(score):
    print("Your score is: ")
    if score > 0 and score <= 50:
        print("Below passing, improve!")
    elif score > 50 and score <= 70:
        print("Barely passing!")
    elif score > 70 and score <= 90:
        print("You have a passing grade!")
    else:
        print("You are in the top")
score = int(input("Enter a score: "))
grade(score)

################################################

def flight_charges(price):
    upgrade = input("Would you like to upgrade: ")
    if upgrade == 'yes':
        price += 99
    baggage = input("Will you have baggage: ")
    if baggage == 'yes':
        price += 35
    tax = (price*.08)+price
    return tax

price = int(input("Enter the base fare: "))
grand = flight_charges(price)
print("Grand total after tax:",grand)

################################################

def bank_balance(balance):
    if balance >= 500:
        return True
    else:
        return False

bankers = int(input("Number of bank customers: "))
for i in range(bankers):
    first_name = input("Enter first name: ")
    balance = float(input("Enter your balance: "))
    res = bank_balance(balance)
    print("Enough funds in "+first_name+"'s account: "+ res)
    if res == True:
        print("Don't worry, enough funds!")
    else:
        print("Your account is getting low...")

################################################

def mortagage(cash):
    if cash >= 50000:
        print("Instant approval")
    elif cash < 50000 and cash >= 20000:
        print("You need approval")
    else:
        print("Not approved at this time")

cash = int(input("Deposit amount: "))
total_balance = 0
while cash != 0:
    total_balance += cash
    mortagage(cash)
    cash = int(input("Deposit amount: "))
print("Total money requested:",total_balance)
    