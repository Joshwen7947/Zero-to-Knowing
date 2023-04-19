import random
winner = 365
current = random.randint(1,500)
print("Winner:",current)
if current == winner:
    print("You win a FREE trip!")
else:
    print("You didn't win...")
    
####################################################

from random import randint

flight_1 = 0
flight_2 = 0

ask = input("Would you like to book another flight: ").lower()
while ask != 'no':
    flight_number = randint(1,2)
    print("Flight number:",flight_number)
    if flight_number == 1:
        flight_1 += 1
    else:
        flight_2 += 1
    ask = input("Would you like to book another flight: ").lower()
print("Number of passengers on flight 1:",flight_1)
print("Number of passengers on flight 2:",flight_2)

####################################################   

from random import *
guess = int(input("Enter a number between 1 - 10: "))
random_num = randint(1,10)
if guess < random_num:
    print("Too Low!")
elif guess > random_num:
    print("Too High!")
else:
    print("Congrats!")
    
####################################################  
    
from random import *
guess = int(input("Enter a number between 1 - 10: "))
random_num = randint(1,10)

while guess != random_num:
    x = random_num
    tries = 1
    while x != guess:
        if guess < x:
            print("Too low!")
            tries += 1
        elif guess > x:
            print("Too High!")
            tries += 1
        guess = int(input("Enter a number between 1 - 10: "))
    print("Congrats!")
    print("It took you:",tries,"tries")
            
        
    
    
    