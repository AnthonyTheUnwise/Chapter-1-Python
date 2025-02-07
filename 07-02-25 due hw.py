"""
Anthony ;D
04/02/25
More functions !!!11!1!11
"""
GradeList = [85, 92, 78, 90, 88, 76, 95, 89, 73, 84]
#Task 1

def Hello(Name):
    print("Heya,", Name)
UserName = input("Please enter your name: ")
Hello(UserName)

#Task 2

def CalculateAverage(Grade1, Grade2):
    Average = (Grade1 + Grade2) / 2
    print("Your average is:", Average)
UserGrade1 = int(input("Enter your Grade: "))
UserGrade2 = int(input("Enter your other Grade: "))
CalculateAverage(UserGrade1, UserGrade2)

#Task 3

def ClassAverage(List):
    NewTotal = 0
    for y in range (0, len(List)):
        NewTotal = NewTotal + List[y]
    Average = NewTotal / len(List)
    print(Average)
ClassAverage(GradeList)

#Task 4

def ValidGrade(Grade):
    if Grade < 0:
        print("Invalid Grade")
    elif Grade > 100:
        print("Invalid Grade")
    else:
        print("Valid Grade")
UserGrade = int(input("Enter your grade: "))
ValidGrade(UserGrade)

#Task 5

def AddGrade(GradeT):
    if GradeT < 0:
        print("Invalid Grade")
    elif GradeT > 100:
        print("Invalid Grade")
    else:
        GradeList.append(GradeT)
UserGrade3 = int(input("Enter your grade: "))
AddGrade(UserGrade3)

#Task 6

def RemoveGrade(GradeU):
    for y in range (0, (len(GradeList)-1)):
        if GradeList[y] == GradeU:
            GradeList.remove(GradeU)
UserGrade4 = int(input("Enter your grade: "))
RemoveGrade(UserGrade4)

#Task 7

def HighGrade():
    HighestGrade = 0
    for y in range (0, len(GradeList)):
        if GradeList[y] > HighestGrade:
            HighestGrade = GradeList[y]
    print("Your highest Grade is:", HighestGrade)
HighGrade()

#Task 8

def LowGrade():
    LowestGrade = 100
    for y in range (0, len(GradeList)):
        if GradeList[y] < LowestGrade:
            LowestGrade = GradeList[y]
    print("Your lowest Grade is:", LowestGrade)
LowGrade()

#Task 9

def PassingGrade():
    PassList = []
    Pass = 49
    for y in range (0, len(GradeList)):
        if GradeList[y] > Pass:
            PassList.append(GradeList[y])
    print(PassList)
PassingGrade()

#Task 10
def Report():
    print("The Class Average was:", ClassAverage(GradeList))
    print("The highest result was:", HighGrade())
    print("The lowest result was:", LowGrade())
    print("The passing results were:", PassList())

                    