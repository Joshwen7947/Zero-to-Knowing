def person_info(name,age,nationality):
    print("Welcome:",name)
    print("You are:",age)
    print("You are:",nationality)

number = int(input("Amount: "))
for i in range(number):
    name = input("Enter first name: ").capitalize()
    age = input("Enter age: ")
    nationality = input("Enter nationality: ").capitalize()
    person_info(name,age,nationality)
    
#######################################################
    
def total_score(game_score):
    points = 0
    while game_score != 0:
        if game_score >= 5 and game_score <= 10:
            points += 1
        if game_score > 10 and game_score <= 20:
            points += 3
        game_score = int(input("Enter the game score: "))

score = int(input("Enter the score: "))
game_points = total_score(score)
print("Total points:",game_points)

#######################################################

def good_deal(cost):
    if cost >= 50 and cost < 150:
        response = "This is a good deal!"
    elif cost >= 150:
        response = "This is overpriced!"
    else:
        response = "Cheap, Buy now!"
    return response

store = input("Enter the store name: ")
cost = float(input("Enter the item cost: "))
res = good_deal(cost)
print(store,"-",res)
if res == "This is a good deal!":
    print("Buy before it's too late... ")
