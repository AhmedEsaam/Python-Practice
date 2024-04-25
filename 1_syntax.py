print("hello world!")

# Division
print(5 / 8)
#-------------------------------------------------------------------------------
#Objects:
'''
• Scalar:
    Can't be sub-divided.
    (int, float, bool, NoneType)

• Non-Scalar:
    Has internal structure that can be accessed
'''
type(5.3)       # returns the type of expression
float(5)        # explicit conversion to float => 5.0
int(5.6)        # explicit conversion to type int => 5 (does not round numbers)

#-------------------------------------------------------------------------------
# Expressions:
'''
any expresion:
    Object    Operator    Object

Operators:
    +   -   *   /   // (int division)   % (reminder)   ** (exponent)

'''

#-------------------------------------------------------------------------------
# Variables:
'''
    ► Variable name should be descriptive.
    ► Avoid using Python keywords.
    ► Vars must be assigned before they can be used in expressions.
    ► Vars are case-sensetive ('a' is not 'A').
'''
x = 5
pi = 3.14159
radius = 2.2
radius = radius + 1


#-------------------------------------------------------------------------------
# Strings:
'''
    String is a Non-scalar object
'''

user = "Adam"
greet = 'hi'

# String operations:
greet_user = greet + ' ' + user     # '+' for concatination
two_greetings = 2*greet             # '*' for multiplication/repeatition
length = len(greet_user)            # 'len()' for string length
included = 'da' in user             # returns 'True' if 'da' is part of the string: user
char = user[0]                      # '[]' for indexing, [-1]: last character
lastChar = user[-1]                 # returns last character
# slicing:
slice = user[0:2]                   # '[index:index]' for slicing (not inclosive to last char index)
toLast = user[2:]                   # '[index: ]' returns string from index to last char => "am"
all = user[:]                       # returns all string
sliceWithSteps = 'Gargantua'[0:7:2] # [starting_index : last_char_index+1 : step]
reverse = user[::-1]                # to return reverse string: use step of -1

print(greet_user)
print(two_greetings)
print(length)
print(included)
print(char)
print(lastChar)
print(slice)
print(toLast)
print(all)
print(sliceWithSteps)
print(reverse)

#-------------------------------------------------------------------------------
# print()
'''
    Displays the string value inside the parentheses on the screen.
'''
print("Hello")

# input()
'''
    ► Takes one argument: the prompt, or instructions, that we want to display 
        to the user so they know what to do.
    ► Always returns string.
        → So you might need to Use the int() to convert this string value to an integer value.
'''
input('Enter an integer: ')
num = input("Type a number: ")
print(num)
print(type(num))

num = int(input("Type a number: "))
print(num)
print(type(num))

#-------------------------------------------------------------------------------
