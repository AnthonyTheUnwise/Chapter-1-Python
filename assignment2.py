# Enter name:Anthony

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 95, 78, 88]
#Task1 on other save i cant access idk why
Mean = 0
for y in range(0, len(scores)):
    Mean = Mean + scores[y]
Mean = Mean//4
#print("The average is:", Mean)
Good = 0
Bad = 0
for y in range(0, len(scores)):
    if scores[y] >= Mean:
        print(students[y], "is above average!")
        Good = Good + 1
    else:
        print(students[y], "is below average!")
        Bad = Bad + 1
print("There are", Good, "Students above average, and the other", Bad, "are not.")
        
