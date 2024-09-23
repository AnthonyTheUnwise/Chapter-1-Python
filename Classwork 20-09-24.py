"""
Anthony ;D
20/09/24
P25 Q2-...
"""

#Task 2
Name = input("Enter your full name:")
Space = Name.index(" ")
print(Name[:Space])
print(Name[Space+1:])
print(" ")

#Task 3
Time = input("Enter your current time like so: 22:11.00:")
Dots = Time.index(":")
Dot = Time.index(".")
Hour = Time[:Dots]
Minute = Time[Dots+1:Dot]
Second = Time[Dot+1:]
Hour = int(Hour)*60*60
Minute = int(Minute)*60
TimeInSeconds = int(Second)+int(Minute)+int(Hour)
print("Your current time in seconds is:", TimeInSeconds)
print(" ")

#Task 4
time_InSeconds = input("Please enter your time in seconds:")
TotalTime = int(time_InSeconds)//60
print("Your total time is:", TotalTime)
print(" ")

#Task 5
a = input("Please inpur your charachter:")
b = input("Please inpur your charachter:")
c = input("Please inpur your charachter:")
d = input("Please inpur your charachter:")
e = input("Please inpur your charachter:")
a = ord(a)
b = ord(b)
c = ord(c)
d = ord(d)
e = ord(e)
print(a, b, c, d, e)

#Task 6
IntPrice = input("Enter your units:")
TotalPrice = int(IntPrice)*0.19+26.20
print("The total price is:", TotalPrice)

#Task 7
Fish = input("Input your portion of fish:")
Chips = input("Input your portion of chips:")
TotalFish = int(Fish)*4.5
TotalChips = int(Chips)*2.8
total2 = int(TotalFish)+int(TotalChips)
print(total2)

#Task 8
#Im like 99% sure we did this as classwork so i will refer to that / upload that attached !!!