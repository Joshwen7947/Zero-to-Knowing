print("Welcome to Kayak 3.0. Let's plan an adventure")
enter = int(input("1 - start or 2 - quit: "))
while enter == 1:
    destination = input("Do you have a destination in mind? ")
    if destination == 'yes':
        print("Let's plan your trip!")
        transport = input("Transport: Plane/Train or Car: ").lower()
        if transport == 'plane':
            class_type = input("Which fare (First/Business/Economy): ")
            luggage = int(input("Enter weight in KG: "))
            if luggage >= 21 and class_type == 'business' or class_type == 'first':
                print("Great, you can have more baggage in those classes!")
            elif luggage < 21 and class_type == 'business' or class_type == 'first':
                print("You can bring more if your want")
            else:
                print("Warning! You may have too much!")
        elif transport == 'train':
            seat_class = input("Economy or Business: ")
            if seat_class == 'business':
                print("Great! More comfort your way")
            else:
                print("You save more this way!")
        elif transport == 'car':
            num_people = int(input("How many people? "))
            if num_people <= 4:
                print("Great, you can rent a car")
            else:
                print("You may want to get a van for more people!")
        else:
            print("We don't have that transport type yet!")
    else:
        print("I can help you choose a desintation!")
        trip_type = input("Beach/City or Adventure: ").lower()
        if trip_type == 'beach':
            print("How about Hawaii?")
            beach_type = input("Popular or Remote beach? ").lower()
            if beach_type == "popular":
                print("Check out Waikiki beach near Honolulu")
            elif beach_type == 'remote':
                print("Head over to Maui")
            else:
                print("We don't have that option...")
        elif trip_type == 'city':
            activity = input("Indoor or Outdoor: ").lower()
            if activity == "indoor":
                print("Check out the Met Museum")
            elif activity == 'outdoor':
                print("Relax in Central Park")
            else:
                print("Wrong input")
        elif trip_type == 'adventure':
            print("Head to Yoesimite National Park!")
            outdoor_activity = input("Hiking or Camping: ").lower()
            if outdoor_activity == 'hiking':
                print("Try hiking Half Dome!")
            elif outdoor_activity == 'camping':
                print("Check out one of the many camping sites with the park")
            else:
                print("That is not offered...")
        else:
            print("That trip is not available")
            
    print("Enter for a chance to win a free trip!")
    for i in range(1,4):
        if input("What is the largest desert in the world? ").lower() == 'antartica':
            print("WOW, you win a FREE Trip!")
            
print("Enjoy your Trip!")
    
            