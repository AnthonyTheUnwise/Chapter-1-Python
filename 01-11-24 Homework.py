"""
Anthony ;D
01/11/24
Making a conversion from decimal to binary!
"""
Decimal = int(input("Enter your number:"))
Binary = ""
while Decimal != 0:
    if Decimal%2 == 0:
        Binary = "0" + Binary
        Decimal = Decimal/2
    else:
        Binary = "1" + Binary
        Decimal = (Decimal-1)/2
print(Binary)