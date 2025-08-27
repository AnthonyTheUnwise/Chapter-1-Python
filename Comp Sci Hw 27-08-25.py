"""

Anthony ;D 

27/08/25, Classwork 

"""

 

#Task 1 

 

print(12+7) 

print(15//4) 

print(15/4) 

print(5**3) 

 

#Task 2 

 

""" 

String 

Float 

Boolean 

Integer 

""" 

 

#Task 3 

 

""" 

It will print ‘You are too young’ 

""" 

age = 17 

if age == 17: 

    print("Almost there!") 

elif age >= 18: 

    print("You can vote") 

else: 

    print("You are too young") 

 

#Task 4 

 

for y in range (0, 10):

    print(y+1) 

 

input1 = 1 

while input1 != 0: 

    input1=int(input("Enter a number!"))

 

#Task 5 

 

numbers = [4, 7, 2, 9, 6] 

print(numbers[0]) 

print(numbers[-1]) 

numbers.append(12) 

numbers.sort() 

 

#Task 6 

 

def square(x): 

    x = x * x 

    print("The square is:", x) 

    return  

def is_even(n): 

    if n%2 == 0: 

        return True 

    else: 

        return False 

x = int(input("Enter your number to be squared:")) 

#square(x) 

n = int(input("Enter the odd or even number:"))

is_even(n) 

 

#Task 7 

data = [5, 3, 8, 3, 9, 12, 5, 3] 

mean = 0 

mode = 0 

counter = 0 

for y in range (0, len(data)): 

    mean = mean + data[y] 

    counter = data.count(y) 

    if counter > 0: 

        y = mode 

print("The mean is:", mean) 

print("The mode is:", mode) 

 

#Task 8 

 

list = [] 

for y in range (0, 5): 

    user = int(input("Enter your number:"))

    list.append(user) 

for y in range (0, 5): 

    if list[y] % 2 == 0: 

        print(list[y]) 

 

#Task 9 

 

def get_range(values):

    values.sort() 

    range = (values[-1] - values[0]) 

    print("The range is:", range) 

    print("The maximum is:", values[-1]) 

    print("The minimum is:", values[0]) 

    values = []
    
    ty = 0

    print("Type a letter to stop inputting") 

    while ty == 0: 

        input=int(input("Enter a number:")) 

    try: 

        input = int(input) 

        values.append(input) 

    except ValueError: 

         ty = 1

#get_range(values) 

 

#Task 10 

count = 0 

lister = [] 

while count > 7: 

    count = count + 1 

    floater = int(input("Enter your number:"))

    lister.append(floater) 

for y in range (0, len(lister)):
    mean = mean + lister[y] 

    counter = lister.count(y) 

    if counter > 0: 

        y = mode 

def median(lister): 

    lister.sort() 

    median = len(lister)//2 

    # median = lister[median] 

    # print("The median is:", median) 

    return 

#get_range(lister) 

print("The mean is:", mean) 

print("The mode is:", mode) 

median(lister) 

 

 

 

 

 

 