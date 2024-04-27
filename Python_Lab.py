# Multi-Line Statements
if True:
    print('Answer \
the phone!')
    print('True')
else:
    print('False')

L = [1, 2, 3,
     4, 5, 6]               # statements contained within [], {}, () do not need to use: \

# Quotation in Python
word = 'word'
sentence = "This is a sentence."
paragraph = '''  This is a paragraph. It's
made up of multible lines'''
paragraph2 = """  Same as
this paragraph."""          # triple quotes ''' ''' and """ """ are used to span the string across multiple lines 
print(word)
print(sentence)
print(paragraph)
print(paragraph2)

# Dynamic Typing
counter = 100               # An integer assignmnet
miles   = 1000.0            # A floating point
name    = 'John'            # A string
print(name)

name = 5.6
print(name)

# Multiple Assignment 
a = b = c = 1               # assign a single value to several variables simultaneously
a, b, c = 1, 2, "John"      # assign multiple objects to multiple variables  


## Python have six standard data types:
''' Numbers                 : int (signed and represented as long), float, complex
    String                  : str:  "" immutable contiguous set of characters
    List                    : list: [] mutable collection of different data types
    Tuple                   : tuple:() immutable collection of different data types
    Dictionary              : dict: {} mutable unordered colection of keys and values
    Set                     : set:  {} mutable unordered collection of elemnets with no dublicates 
'''

# Numbers
var1 = 1
var2 = 100
del var1, var2              # var1 and var2 are no longer in memory

intVar = 10
intVar = -780
intVar = -0x260             # hex

floatVar = 0.0
floatVar = 32.3e18          # exponential
floatVar = 90.
floatVar = 702E-12

complexVar = 3.14j
complexVar = 45.j
complexVar = 9.325-36j
complexVar = .8j
complexVar = -.54+2J
complexVar = 3e+26J

# Strings
st = "Hello World! "
print(type(st))
print(st)
print(st[0])
print(st[2:5])              # slice from str[0] to str[4]
print(st[2:])               # slice from str[0] to the end
print(st * 2)               # repeat
print(st + "TEST")          # concatenate
print()

# Lists
L = ['abcd', 456, 2.32, 5+2j, 2.54]
tinyList = [163, "John"]
print(type(L))
print(L)
print(L[-1])                # the last item
print(L[1:3])
print(L[2:])
print(tinyList * 2)
print(L + tinyList)
L[2] = [1,2]                # lists are mutable, here we assigned a list object in the list[2]
print(L)
print()

# Tuples
tup = ('abcd', 456, 2.32, 5+2j, 2.54)
tinyTuple = (163, "John")
print(type(tup))
print(tup)
print(tup[0])
print(tup[1:3])
print(tup[2:])
print(tinyTuple * 2)
print(tup + tinyTuple)
# tuple[2] = 5              # Error: tuple objects are immutable, ...
tup = (2, 'efgh', 2.65)     # ... but you can overwrite it altogether by assigning ...
print()                     # ... a different tuple object to the same identifier.

# Dictionaries
dct = {}
dct['one'] = "This is one"
dct[2] = "This is two"
tinyDict = {'name': 'john', 'code': 6314, 'dept': 'sales'}
print(type(dct))
print(dct['one'])
print(dct[2])
print(tinyDict)
dct.update(tinyDict)        # extends the dict dictionary by the tinyDict
print(dct)
print(dct.keys())
print(dct.values())

# Sets
mySet = {1, "Python", 2.65, ('A', 'B', 'C')}
print(type(mySet))
print(mySet)
mySet = {1, 2, 3, 4, 3, 4, 5}
print(mySet)
# mySet = {2, 4, [3, 4]}    # set cannot contain mutable items like lists and dicts
...
print()


## Data Type Conversions:
x = "2+5"
y = int("25")
print(y)
y = float("2.65")
print(y)
y = complex(5,2)
print(y)
y = str(2.5)
print(y)
y = repr(x)                 # returns the printable representation of the object
print(y)
y = eval(x)
print(y)
y = tuple(x)
print(y)
y = list(x)
print(y)
y = set(x)
print(y)
y = dict(A = 5, B = 6, C = 7)
print(y)
y = frozenset(x)            # immutable version of the python set
print(y)
y = chr(2)
print(y)
y = ord('a')
print(y)
y = hex(16)
print(y)
y = oct(8)
print(y)
print()

