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

