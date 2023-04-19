message = input("Enter your message: ")
while message != "done":
    print("We got your message!")
    message = input("Enter your message: ")

###################################################################

passcode = input("Enter your passcode: ")
while passcode != "1234" and passcode != "4321":
    passcode = input("Try again: ")
print("Welcome to your account!")

###################################################################

counter = 0
while counter < 3:
    name = input("Enter your name: ")
    print("Congrats,",name,"You saved 20%")
    counter += 1
print("All done!")

###################################################################

tries = 0
code = ""
while tries < 5 and code != "python":
    code = input("Enter a programming language: ")
    tries += 1

if code == "python":
    print("It took you",tries,"tries...")
    
###################################################################   
    
train_tickets = input("0 - get ticket, 1 - end booking: ")
i = 1
while train_tickets != "1":
    if train_tickets == "0":
        print("Train Ticket:",str(i))
        i += 1
    train_tickets = input("0 - get ticket, 1 - end booking: ")

    


