#Welcome to the tip calculator
#Display a welcome message to use the calculator
print("Welcome to the tip calculator!")
#Create a variable to store the total bill amount input by the user
bill = float(input("What was the total bill? $"))
#Create a variable to store the tip % input by the user
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#Create a variable to store the number of people input by the user
people = int(input("How many people to split the bill? "))
#Create a variable to calculate the total bill person including the tip amount per person """
bill_per_person = ((bill/people) + ((bill*(tip/100))/people))
#Create another variable 'total_per_person' to concatenate the string and the convert the integer to string
total_per_person = "The total bill per person is " + "$" + str(bill_per_person)
#print the total per person
print (total_per_person)




