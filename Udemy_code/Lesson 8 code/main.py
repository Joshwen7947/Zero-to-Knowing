passcode = input("Enter your passcode: ")
invalid = "!@#$%^&*()"
for letter in passcode:
    if letter in invalid:
        print("This is not allowed:",letter)

##########################################################

vowels = 'aeiou'
const = 'bcdfghjklmnpqrstvwxyz'
word = input("Enter a word: ")
vowel_num = 0
for letter in word:
    if letter in vowels:
        vowel_num += 1
    elif letter in const:
        vowel_num += 0
print("There are",vowel_num,"vowels in the word:",word)

##########################################################

phone = input("Enter a phone number: ")
valid = "1234567890+"
for number in phone:
    if number not in valid:
        print("Not a valid number")
        break
    
##########################################################

guests = int(input("Enter number of guests: "))
for i in range(guests):
    name = input("Enter name: ")
    age = int(input("Enter the age: "))
    if age >= 18:
        print("Welcome,",name)
    else:
        print("You must be 18 to drink...")

##########################################################

for i in range(5):
    username = input("Enter username: ")
    passcode = input("Enter passcode: ")
    if username == 'admin' and passcode == '12345':
        print("Welcome admin!")
        break
if username != 'admin' or passcode != "12345":
    print("This is not your account!")