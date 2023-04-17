## Python - Global Variables

## Create a variable outside of a function, and use it inside the function

name = ('justin')

def first_name():
    print("hello my name is " + name)

first_name()
## hello my name is justin

## Create a variable inside a function, with the same name as the global variable

name = ('justin')

def first_name():
    name = ('emanuel')  ## local scope
    print("hello my name is " + name)

first_name()

print("hello my name is " + name)

## The global Keyword

name = ('justin')

def first_name():
    global name
    name = ('justin')  ## local scope

first_name()

print("hello my name is " + name)

## Also, use the global keyword if you want to change a global variable inside a function.

name = ('justin')

def first_name():
    global name
    name = ('emanuel')  ## local scope

first_name()

print("hello my name is " + name)


## Exercise:

## Create a variable named carname and assign the value Volvo to it.

carname = 'Volvo'

## Create a variable named x and assign the value 50 to it.

X = 50

## Create a variable named x and assign the value 50 to it.

## Display the sum of 5 + 10, using two variables: x and y.

x = 5
y = 10
print(x + y)
## 15

## Create a variable called z, assign x + y to it, and display the result.
x = 5
y = 10

z = x + y
print(z)
