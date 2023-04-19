answers = list()
fruit = input("Enter a fruit: ")
while fruit != "quit":
    answers.append(fruit)
    fruit = input("Enter a fruit: ")

guess = input("Guess a fruit: ").lower()
for answer in answers:
    if guess == answer:
        print("Congrats!")
        break
    else:
        print("Sorry, that's wrong!")
        break
    
#########################################################

cities = list()
city = input("Enter a capital city: ").lower()
while city != "0":
    if city in cities:
        print("You have already said this city")
    else:
        cities.append(city)
    city = input("Enter a capital city: ").lower()
cities.sort()
print("List of capital cities:",cities)

#########################################################

from random import *
players = input("Enter each player: ").split(" ")
player_amt = len(players)
team = list()
for player in players:
    random_team = randint(1,3)
    team.append(random_team)
    
for i in range(player_amt):
    print(players[i],"-",team[i])
    
#########################################################   
      
scores = ["Billy - 5","Sarah - 4","Leo - 3","John - 3","Anna - 4"]
avg = 0

for score in scores:
    x = int(score[len(score)-1])
    avg += x
    
avg /= len(scores)
print("The average score:",avg)

#########################################################

def calc_avg(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

numbers_list = [2,5,6,4,3,1,7]
for i in range(len(numbers_list)):
    sublist = numbers_list[:i+1]
    average = calc_avg(sublist)
    print("The average of",sublist,"is",average)












