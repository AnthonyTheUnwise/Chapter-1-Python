"""
Anthony ;D
05/11/24
Reversing Hexa Code to decimal!
"""
Result = ""
Base = 16
Hexa = str(input("Please enter your value:"))
HexaReverse = ""
for y in range (0, len(Hexa)):
    HexaReverse = Hexa[y] + HexaReverse
Hexa = HexaReverse
for Power in range (0, len(Hexa)):
    if Hexa[Power-len(Hexa)] == "1":
        Result = "0001" + Result
    elif Hexa[Power-len(Hexa)] == "2":
        Result = "0010" + Result
    elif Hexa[Power-len(Hexa)] == "3":
        Result = "0011" + Result
    elif Hexa[Power-len(Hexa)] == "4":
        Result = "0100" + Result
    elif Hexa[Power-len(Hexa)] == "5":
        Result = "0101" + Result
    elif Hexa[Power-len(Hexa)] == "6":
        Result = "0110" + Result
    elif Hexa[Power-len(Hexa)] == "7":
        Result = "0111" + Result
    elif Hexa[Power-len(Hexa)] == "8":
        Result = "1000" + Result
    elif Hexa[Power-len(Hexa)] == "9":
        Result = "1001" + Result
    elif Hexa[Power-len(Hexa)] == "A":
        Result = "1010" + Result
    elif Hexa[Power-len(Hexa)] == "B":
        Result = "1011" + Result
    elif Hexa[Power-len(Hexa)] == "C":
        Result = "1100" + Result
    elif Hexa[Power-len(Hexa)] == "D":
        Result = "1101" + Result
    elif Hexa[Power-len(Hexa)] == "E":
        Result = "1110" + Result
    elif Hexa[Power-len(Hexa)] == "F":
        Result = "1111" + Result
print("In decimal, this is:", Result)