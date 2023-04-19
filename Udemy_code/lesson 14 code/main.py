class Animal():
    def __init__(self,name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound
        
    def speak(self):
        print(self.sound)
    
    def pet_info(self):
        print("My",self.pet,"has the name",self.name,"They make the sound",self.sound)
        
dog = Animal("Champ","Dog","Woof Woof")
cat = Animal("Toby","cat","Meow meow")

dog.speak()
cat.speak()

dog.pet_info()
cat.pet_info()

#####################################################

class Player():
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.team = None
    
    def show_Stats(self):
        print("Player:",self.name)
        print("Score:",self.score)
        print("Team:",self.team)
        
    def select_team(self):
        team = input("Enter the team: ")
        self.team = team
        
player1 = Player("Steph Curry","9")
player1.show_Stats()
player1.select_team()

player1.show_Stats()

#####################################################

class Rectangle():
    def __init__(self,length, width):
        self.length = length
        self.width = width
        
    def print_info(self):
        print("Rectangle with the length:",self.length,"and the width of:",self.width)
        
    def calc_perimeter(self):
        self.perimeter = (self.length + self.width) *2
        return self.perimeter
    
    def calc_area(self):
        self.area = self.length * self.width
        return self.area
    
    def updated(self, length):
        self.update = (self.length - length) * self.width
        return self.update
    
a = int(input("Enter the length: "))
b = int(input("Enter the width: "))

rect = Rectangle(a,b)
rect.print_info()
print("Perimeter:",rect.calc_perimeter())
print("Area:",rect.calc_area())

c = int(input("Enter number to subtract from the length: "))
print("Updated Area:",rect.updated(c))