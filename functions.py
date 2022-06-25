#functions

def details(name, age):

    print (name, age)
    #print (age)

details ("hina", 32)

#create a function which accepts variable number or lenght of arguments

def variablelenghtarguments(*args):
    for item in args:
        print(item)

variablelenghtarguments(10, 20)
variablelenghtarguments(30, 40, 50)

#create a function in which functions has default argument
def defaultargumentfunction(name, salary=10000):
    print(name, salary)

defaultargumentfunction("hina", 20000)
defaultargumentfunction("hina")

#create a nested function

def outerfunction(a, b):

    def innerfunction(a, b):

        return a + b
    res = innerfunction(a, b)
    return res + 5
result = outerfunction(5, 10)
print(result)

#change name of the function and call it through a new name

def oldname(name, age):
    print(name, age)

newname = oldname

newname("hina", 23)

#function for add, sub, mul
def calculation(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    print(f"sum is {add}, sub is {sub}, mul is {mul} ")

calculation(2, 3)

#function for add, sub and mul with input from user

def calculation(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    print(f"sum is {add}, sub is {sub}, mul is {mul} ")

x = input("enter the value of X: ")
y = input("ente the value of Y: ")
x= int(x)
y= int(y)
calculation(x, y)

#function that check if roll number is present or not

def checkroll(roll):
    r = [22, 34, 45, 56, 72]
    if roll in r:
        print(f"{roll} is present")
    else:
        print("not present")

roll = int(input("enter the rollnumber: "))
checkroll(roll)

#function to check if the number is even or odd

def checknumber(num):
    if num % 2 == 0:
        print(f"({num} is even)")
    else:
        print("it is odd")

num = int(input("enter your number: "))
checknumber(num)
