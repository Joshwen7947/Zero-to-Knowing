movie = input("Do you want to watch a movie? ").lower()
if movie == 'yes':
    genre = input("Enter a genre: ").lower()
    if genre == "comedy":
        print("Watch the Hangover Trilogy")
    else:
        print("Watch Top Gun")
else:
    print("Watch a TV series!")
    
###################################################################

accomodation = input("Hotel or Resort: ").lower()
if accomodation == "resort":
    max_price = int(input("Enter your max price: "))
    if max_price >= 350:
        print("Book at the Six Senses Resort")
    else:
        print("Book at the Four Seasons")
else:
    print("Go to the nearest Hilton")

###################################################################

item1 = int(input("Enter the price for item 1: "))
item2 = int(input("Enter the price for item 2: "))
item3 = int(input("Enter the price for item 3: "))

total = item1+item2+item3

if item1 < item2 and item2 < item3:
    total *= 0.5
    print("Savings!")
    
if item1 > item2 and item2 > item3:
    total *= 0.33
    print("Savings!")
print("Total:",total)
    
###################################################################

cost = int(input("Enter the price: "))
hour = int(input("Enter the current hour: "))
if hour >= 7 and hour <= 9:
    cost *= 0.8
    print("Total:",cost)

elif hour >= 10 and hour < 18:
    print("Total:",cost)
    
else:
    print("Store is closed!")
    
###################################################################   

review = int(input("Enter a rating: "))
if review >= 9:
    print("Thank you so much!")
elif review < 9 and review >= 5:
    improve = input("How can we improve: ")
    print("You said:",improve)
    print("We will work harder!")
else:
    print("We are sorry to hear that!")