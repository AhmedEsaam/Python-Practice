# Functions --------------------------------------------------------------------

# No args and No return: .................
def printHello():
    print('We printed this through no inpur parameters or return!')
    
printHello()

# With args and No return: ...............
def printSum(num1, num2):
    print(num1+num2)

x = 20; y = 30
printSum(x, y)

# No args and With return: ...............
def pi():
    return 22/7

circle = 2 * 7 * pi()
print(circle)

# With args and With return: .............
def isEven(num):
    return num%2 == 0

print(isEven(10))

# Docstrings: (use multiline comment to document functions)
def isOdd(num):
    '''
    This function is used to tell if the given number is odd
    input: Num, Type: Integer
    Output: Booloean
    '''
    return num%2 != 0

print(isOdd(10))


# Variable Scope ---------------------------------------------------------------

# Globab Scope: Defined in the main body of scope
a = 5
def func():
    a = 3
    print(a)
func()

# Formal Parameter: Defined inside a function
def func():
    b = 5
    print(5)
func()

print()

# Example 1: ......................
x = 5
def f(y):
    x = 1       # formal parameter (local)
    x += 1
    print(x)
    
f(x)            # prints 2 whatever x is.
print(x)        # prints x => 5

print()

# Example 2: ......................
def g(y):
    print(x)    # Global vars are defined bwfore the whole script
    print(x+1)

x = 5           # Global variable
g(4)
print(x)

print()

# Example 3: ......................
x = 5
def h(y):
    # x = x + 1     # as long as you created a local x, it overrides the global x in this scope
                    # So (x + 1) is using a local x before it is defined
    print(x)
    
h(x)
print(x)

# Example 4: ......................
x = 5
def h(y):
    x = 1       # a local x
    print(x)
    
h(x)
print(x)

#-------------------------------------------------------------------------------
