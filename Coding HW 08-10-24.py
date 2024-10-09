"""
Anthony ;D
Task 1-5 and 1-5 in if workbook
08/10/24
"""
import random
#Task 1
Num1 = input("Please enter a number:")
Num2 = input("Please enter a second number:")
if int(Num1)%int(Num2) == 0: #Checks whether they divide anf if they do|:
    print("When divided, these make the number:", int(Num1)/int(Num2)) #Prints the divided result
elif int(Num2)%int(Num1) == 0:
    print("When divided, these make the number:", int(Num2)/int(Num1)) #This checks for when theyre the other way around
else:
    print("These do not divide perfectly") #When they dont divide:
    print(" ")

#Task 2
Age = input("Input age:")
if int(Age) > 16: #If above 16 gives liscence
    print("Get liscense:")
else: #if not doesnt say too young
    print("Too young D:")
print(" ")
#Task 3
Prc = input("Enter price:")
if int(Prc) < 500: #if low let them buy
    print("Order item?")
elif int(Prc) < 10000: #If imbetween give choices
    print("Do you want to buy from Company A, B or C?")
else:
    print("Sorry, too big order, go get a \"tender\"!") #Too high so cant buy
print(" ")
#Task 4
WhichBus = input("Congrats user, we are giving away free bus passes depending on what bus you take! Please input your letter:")
if WhichBus == "A":#If they redeem A they go place, same for B and C specifically
    print("Congrats! You win a trip to Dundrum Shopping Centre!")
elif WhichBus == "B":
    print("Congrats! You win a trip to Tallagadh!")
elif WhichBus == "C":
    print("Congrats! You win a trip to Broombridge!")
else: #If wrong code, get nothing
    print("Invalid Entry")
print(" ")

#Task 5
Test = input("Enter your test result as a full percentage without the \"%\":") #Asks for percentaqge
if int(Test) > 30: #If in H8 range gives H8
    print("You got a H8")
elif int(Test) > 40: #Repeats down
    print("You got a H7")
elif int(Test) > 50:
    print("You got a H6")
elif int(Test) > 60:
    print("You got a H5")
elif int(Test) > 70:
    print("You got a H4")
elif int(Test) > 80:
    print("You got a H3")
elif int(Test) > 90:
    print("You got a H2")
elif int(Test) > 101:
    print("You got a H1")
else: #If they enter wrong, insult them >;D
    print("Impossble value, probably a H8")
print(" ")

#FINALLY IF STATEMENTS 1-5
#Task 1
Name = input("Enter your name:")
if len(Name)<7:
    print("Your name is short, ", Name, "!")
elif len(Name)>9:
    print("Wow,", Name, "! Your name is long!")
print(" ")

#Task 2
print(" | Menu:                       | ")
print(" | 1. Music                    | ")
print(" | 2. History                  | ")
print(" | 3. Design and Technology    | ")
print(" | 4. Exit                     | ")
Choice = input(" | Choose:                     | ")
if int(Choice) == 1:
    print("You chose Music!")
elif int(Choice) == 2:
    print("You chose History!")
elif int(Choice) == 3:
    print("You chose Design and Technology!")
else:
    print("Goodbye!")
print(" ")

#Task 3
D1 = random.randint(1, 6)
D2 = random.randint(1, 6)
print("Your simulated dice rolls are:", D1, "and", D2)
MinTotal = D1 + D2
if D1 == D2:
    Total = MinTotal*2
    print("Your total score is:", Total)
else:
    print("Your total score is:", MinTotal)
print(" ")

#Task 4
Price = input("Enter your total price:")
if int(Price) > 199.99:
    TotPrice = int(Price)*0.9
    print("Your total is:", TotPrice)
elif int(Price) > 99.99:
    TotPrice = int(Price)*0.95
    print("Your total is:", TotPrice)
else:
    print("Your total is:", Price)
    
#Task five, order is A, D, C, B