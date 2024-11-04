"""
Anthony ;D
01/11/24
Making a conversion from decimal to binary!
"""
Decimal = int(input("Enter your number:")) #Asks for decimal number
Hexa = "" #Makes sure binary is a string (Needed)
while Decimal != 0: #While our number isnt 0:
    if Decimal%16 == 0: #If it divides perfectly
        Hexa = "0" + Hexa #Add 0 to start
        Decimal = Decimal/16 #Divides by 2
    elif Decimal%16 == 1: #Else it doesnt divide
        Hexa = "1" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-1)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 2: #Else it doesnt divide
        Hexa = "2" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-2)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 3: #Else it doesnt divide
        Hexa = "3" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-3)/16 #Divides by 2 (-3) as to make sure number go correctly
    elif Decimal%16 == 4: #Else it doesnt divide
        Hexa = "4" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-4)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 5: #Else it doesnt divide
        Hexa = "5" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-5)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 6: #Else it doesnt divide
        Hexa = "6" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-6)/16 #Divides by 2 (- 1) as to make sure number go 
    elif Decimal%16 == 7: #Else it doesnt divide
        Hexa = "7" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-7)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 8: #Else it doesnt divide
        Hexa = "8" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-8)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 9: #Else it doesnt divide
        Hexa = "9" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-9)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 10: #Else it doesnt divide
        Hexa = "A" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-10)/16 #Divides by 2 (- 1) as to make sure number go correctly
    elif Decimal%16 == 11: #Else it doesnt divide
        Hexa = "B" + Hexa #Adds 1 as not even to start
        Decimal = (Decimal-11)/16
    elif Decimal%16 == 12:
        Hexa = "C" + Hexa 
        Decimal = (Decimal-12)/16 
    elif Decimal%16 == 13: 
        Hexa = "D" + Hexa 
        Decimal = (Decimal-13)/16 
    elif Decimal%16 == 14: 
        Hexa = "E" + Hexa 
        Decimal = (Decimal-14)/16 
    elif Decimal%16 == 15: 
        Hexa = "F" + Hexa 
        Decimal = (Decimal-15)/16 
print(Hexa) #Prints result!