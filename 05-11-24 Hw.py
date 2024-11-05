"""
Anthony ;D
05/11/24
Reversing Hexa Code to decimal!
"""
Result = 0
Base = int(input("Please enter your base:"))
Hexa = str(input("Please enter your value:"))
HexaReverse = ""
for y in range (0, len(Hexa)):
    HexaReverse = Hexa[y] + HexaReverse
Hexa = HexaReverse
for Power in range (0, len(Hexa)):
    if Hexa[Power-len(Hexa)] == "1":
        Result = 1*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "2":
        Result = 2*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "3":
        Result = 3*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "4":
        Result = 4*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "5":
        Result = 5*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "6":
        Result = 6*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "7":
        Result = 7*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "8":
        Result = 8*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "9":
        Result = 9*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "A":
        Result = 10*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "B":
        Result = 11*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "C":
        Result = 12*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "D":
        Result = 13*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "E":
        Result = 14*(Base**Power) + Result
    elif Hexa[Power-len(Hexa)] == "F":
        Result = 15*(Base**Power) + Result
print("In decimal, this is:", Result)