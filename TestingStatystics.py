"""
Anthony ;D
Practising Statystics
25/03/25
"""
List_1 = [15, 12, 16, 19, 12, 14, 16, 12]
List_2 = [3, 3, 7, 8, 7, 9, 8, 5, 7, 11, 12]
List_3 = [67, 43, 89, 45, 54, 86, 45, 76, 53]
Mean = 0
Largest = 0
Smallest = 100
print(List_1)
print(List_2)
print(List_3)
ListNum = int(input("please enter the list you want:"))
if ListNum == 1:
    ListNum = List_1
elif ListNum == 2:
    ListNum = List_2
elif ListNum == 3:
    ListNum = List_3
Len_List = len(ListNum)
print(Len_List)
for y in range (0, Len_List):
    Mean = Mean + ListNum[y]
print(Mean/Len_List)
EvenMiddle = Len_List
if Len_List%2!=0:
    EvenMiddle = Len_List - 1
Median = ListNum[EvenMiddle]
print(Median)
for y in range (0, Len_List):
    if ListNum[y]>Largest:
        Largest = ListNum[y]
    if ListNum[y]<Smallest:
        Smallest = ListNum[y]
print(Largest)
print(Smallest)
print(Largest - Smallest)