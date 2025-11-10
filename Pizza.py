print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

#Block of code to calculate price based on pizza size
if size == "S":
    bill += 15
elif size =='M':
    bill += 20
elif size =='L':
    bill += 25
else:
    print("You have chosen an invalid size.")

#Block of code to calculate prize based on pepperoni preferences
if pepperoni == "Y" :
    if size =="S" :
        bill += 2
    else :
        bill += 3

#Block of code to calculate prize based on cheese preferences
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

#Print the final bill
print(f"Your final bill is: ${bill}.")



