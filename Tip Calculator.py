#welcome to the tip calculator
# print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_per_person = ((bill/people) + ((bill*(tip/100))/people))
total_per_person = "The total bill per person is " + "$" + str(bill_per_person)
print (total_per_person)




