class Animal():
    def __init__(self,name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound
        
    def speak(self):
        print(self.sound)
    
    def pet_info(self):
        print("My",self.pet,"has the name",self.name,"They make the sound",self.sound)
        
class Fish(Animal):
    def swim(self):
        if self.sound == None:
            print("You are a fish")
        else:
            print("Are you sure you're a fish?")
    
    def ocean(self):
        region = input("Which ocean are you from: ")
        print(self.name,"is a",self.pet,"who lives in the",region,"ocean!")
        
nemo = Fish("nemo","fish",None)
nemo.speak()
nemo.pet_info()

nemo.swim()
nemo.ocean()

################################################################

class Vehicles():
    def __init__(self,make,model,year,price):
        self.make = make
        self.model =model
        self.year = year
        self.price = price
    
    def get_make(self):
        if self.make == 'ford' or self.make == 'chevy' or self.make == 'tesla':
            return "American Made"
        else:
            return "Imported"
    
    def get_model(self):
        return self.model   
    
    def get_year(self):
        if self.year >= 2000:
            return "21st century car"
        else:
            return "This car is old"
    
    def get_price(self, max_price):
        if self.price < max_price:
            return "Good buy, within your budget"
        else:
            return "Over budget"
        
class Style(Vehicles):
    def __init__(self, make, model, year, price, num_of_doors):
        super().__init__(make, model, year, price)
        self.num_of_doors = num_of_doors
        
    def get_doors(self):
        if self.num_of_doors == 4:
            return "Family Car!"
        else:
            return "Sports Car"
        
        
truck = Vehicles('ford','f-15-',1999,15000)
print(truck.get_make())
print(truck.get_price(12000))

car = Style("Toyota",'camry','2001',9000,4)
print(car.get_doors())

sports_car = Style('lamborghini','aventador',2022,350000,2)
print(sports_car.get_make())
print(sports_car.get_doors())

################################################################

from time import *

class Agent():
    def __init__(self,name,health,car):
        self.name = name 
        self.health = health
        self.car =car
    
    def agent_info(self):
        print("Welcome:",self.name)
        print("Your health:",self.health)
        print("Car choice:",self.car)
        
    
class Spy(Agent):
    def __init__(self, name, health, car,agency, location):
        super().__init__(name, health, car)
        self.agency = agency
        self.location = location
        self.killed = False
        
    def assassinate(self,bad_guy):
        if bad_guy.health >0:
            bad_guy.health -= 20
            print(bad_guy.name,"has lost 20 from their health")
            print(bad_guy.name,"has a health level of",bad_guy.health)
            if bad_guy.health <= 0:
                self.killed = True
                print(bad_guy.name,"is dead...",self.killed)
                
james_bond = Spy("James Bond",100,"Jaguar","MI6","London")
ethan_hunt = Spy("Ethan Hunt",60,"Ferrari","CIA","Dubai")

james_bond.agent_info()
ethan_hunt.agent_info()
sleep(5)
while ethan_hunt.health > 0 and james_bond.health >0:
    james_bond.assassinate(ethan_hunt)
    ethan_hunt.assassinate(james_bond)
    sleep(2)
                

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    