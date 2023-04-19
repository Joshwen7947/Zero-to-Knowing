rental_price = int(input("Enter the price per day: "))
days = int(input("Number of days to rent: "))
total = rental_price * days
print("Total car price:",total)

###################################################################

package1 = int(input("enter the weight of package 1: "))
package2 = int(input("enter the weight of package 2: "))
package3 = int(input("enter the weight of package 3: "))

total = (package1+package2+package3)*0.8
print("Shipment total:",total)

###################################################################

income = int(input("enter your income: "))

food = int(input("Enter your food expenses: "))
rent = int(input("Enter your rent: "))
extra = int(input("Enter any extra expenses: "))

remaining = income - food - rent - extra
print("You are left with: ", remaining)

###################################################################

monthly_pay = int(input("Enter your monthly pay: "))
overtime = int(input("Enter extra hours worked: "))
bonus = (monthly_pay*overtime) *0.2
print("Bonus Pay:",bonus)