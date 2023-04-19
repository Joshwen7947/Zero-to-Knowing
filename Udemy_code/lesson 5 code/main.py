trip_type = input("Is your trip Business/Leisure or PErsonal? ").lower()
price = int(input("Expected trip cost: "))

discount = trip_type == "business" and price >= 1200
print("Customer receives a discount:",discount)

###################################################################

code = input("Enter your code here: ")
if code =="winter23":
    print("You get 20% off!")
else:
    print("Code is invalid")

###################################################################

cost = int(input("Enter your trip funds: "))

if cost < 350:
    print("Go on a stay-cation")
if cost >= 350 and cost < 1000:
    print("Go on a road trip!")
if cost >= 1000:
    print("Catch a flight!")
print("Have fun!")

###################################################################

bag_weight = int(input("Enter the baggage weight: "))
destination = input("Enter domestic or international: ").lower()

if bag_weight <= 18:
    price = 25
else: 
    price = 75
    
if destination == "domestic":
    price = price + 300
elif destination == "international":
    price += 750
else:
    print("Spelling Error!")
print("Ticket price:",price)




