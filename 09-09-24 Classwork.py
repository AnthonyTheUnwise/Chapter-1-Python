"""Anthony ;D
09/09/24
Task 1:
"""

PersonName = "Alex"
FavouriteColour = "Red"
print ("Hi" , PersonName, "- your favourite colour is", FavouriteColour)
print("Goodbye", PersonName)

#Before running it, i think it will just state the persons name and state thier favourite colour
#I was correct, now task 1 part 2

PersonName = "Charlie"
FavouriteColour = "Green"
print ("Hi" , PersonName, "- your favourite colour is", FavouriteColour)
print("Goodbye", PersonName)

#I believe this one will just display Charlie and green, should be simple
#I was correct, now task 2

PersonName = input("Enter your name:")
FavouriteColour = input("Enter your favourite colour:")
print ("Hi" , PersonName, "- your favourite colour is", FavouriteColour)
print("Goodbye", PersonName)

"""I believe the python code works by having the "Input" function make you insert
your own variable for your name / colour before reading it / inserting it in.
Task 3:
I have learned that variables are a general name we give to storing different types of
 data, such as a string, boolean, float and integer.
 Task 4 !!!"""

goals = 0
goals = goals+1
print("The value of goals is", goals)
#States that goals is one as there is no loop

answer = 1+2
print(answer)
value1 = answer+3
value2=1+2+3
print (value1, value2)
# Will probably print 6 twice? (It did)

a = 10
b = 5
Temp = a
a = b
b = Temp
#Either crashes or defaults temp to be B (It defaulted temp to b)
#next line is to make a space for tidier code
print(" ")

accountBalance = 1000
WithdrawAmmount = 600
accountBalance = accountBalance - WithdrawAmmount
#Should just minus and give us 400 (It did)

days = 2
hrs = 24
mins = 60
total = days*hrs*mins
print(total)

#prints total

"""Thats the end of task 4, now its task 5 time"""

year = int(input("Enter the current year:"))
age = int(input("Enter the age you will be on December 31st:"))
year = year - age
print("You were born in the year:", year)
#It errors as you need to specify what type of data it is !!! fixed is above ^^^

#A way to convent Centigrade to Fahrenheit
centi = float(input("Enter the Centigrade Value:"))
faren = 9/5 * centi + 32
print(centi, "degrees C equals:", faren, "Degrees F")
#Task 7
principal = input("Enter Principal:")
principal = float(principal)
rate = input("Enter rate:")
rate = float(rate)
time = input("Enter time")
time = float(time)
amount = principal * rate * time
print("The intrest amount is:", amount)
"""
The inputs are the principal. rate and time the user puts in!!!
If we removed those lines, our code would get confused and break :(
"""
#Task 8
print(pow(10, abs(-2)))
#I think this will turn the -2 into 20 (It turned it into 100 :cry:)
print(" ")

#Task 9
runTotal = 0
price1 = 10
runTotal =runTotal + price1
price2 = 14
runTotal = runTotal + price2
price3 = 6
runTotal = runTotal + price3
print("Total amount is:", runTotal)
"""
Yes, we can swap around price 1, 2 and 3 completely!
What are running totals???
"""

#Task 10, finally

import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)
print(num1, "Times", num2, "=", num1*num2)

#just realised i dint have to type these, the questions are done in my copy !!!