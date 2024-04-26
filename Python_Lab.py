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

# Python have five standard data types:
''' Numbers
    String
    List
    Tuple
    Dictionary 
'''
var1 = 1
del var1                    # var1 ois no longer in memory


