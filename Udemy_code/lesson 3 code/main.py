first_name = input("Enter the first name: ")
city = input("Enter the city: ")
country = input("Enter the country: ")
print(first_name, "lives in",city,",",country)

###################################################################

rental_price = input("Enter the price per day: ")
rental_price = int(rental_price)
days = input("Number of days to rent: ")
days = int(days)
total = rental_price * days
print("Total car price:",total)

###################################################################

package1 = input("enter the weight of package 1: ")
package2 = input("enter the weight of package 2: ")
package3 = input("enter the weight of package 3: ")

package1 = int(package1)
package2 = int(package2)
package3 = int(package3)

total = (package1+package2+package3)*0.8
print("Shipment total:",total)

###################################################################

user = input("Enter the username: ")
age = input("Enter the age: ")
id_number = 786147

id_number = str(id_number)
print("Welcome, "+user+". You are "+age+". Your ID is:"+id_number)