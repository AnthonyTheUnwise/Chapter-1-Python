names = []
scores = []
print("Enter names and scores for 5 students:")
student_number = 1
for _ in range(5):
    name = input("Enter name of student " + str(student_number) + ": ")
    score = int(input("Enter score for " + name + ": "))
    names.append(name)
    scores.append(score)
    student_number += 1
for y in range(0, len(names)):
    if scores[y] > scores[0]:
        _ =names.pop(y)
        names.insert(_, 1)
        _ =scores.pop(y)
        scores.insert(_, 1)
print("Our top scorer is ", names[0], ", with a score of:", scores[0])
print("\nStudent\tAverage\n-------\t-------")
for y in range(0, len(names)):
    print(names[y], "\t", scores[y])