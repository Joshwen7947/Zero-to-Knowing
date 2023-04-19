from time import *
timer = int(input("1 - start, 2 - end: "))
while timer != 2:
    if timer == 1:
        start_timer = time()
    timer = int(input("1 - start, 2 - end: "))
end_timer = time()
total = end_timer-start_timer
print("Time that has passed:",total,"seconds")

points = 0
if total < 10:
    points += 3
elif total >= 10 and total < 15:
    points += 2
else:
    points += 1
print("You are awarded:",points,"points") 

###########################################################

from time import *
countdown_start = int(input("Enter a starting time: "))
countdown = countdown_start
while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print("Your countdown finished after:",countdown_start,"seconds!")

###########################################################

from time import *
file_size = int(input("What is the file size: "))
internet_speed = int(input("What is your internet speed: "))
file_size *= 8
download_time = file_size/internet_speed
print("Time to complete download:",download_time,"seconds")

countdown = round(download_time)
while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print("Download Completed!")