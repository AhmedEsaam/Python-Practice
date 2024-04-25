# Tuples -----------------------------------------------------------------------

t = ()
print(type(t))
''' Denoted by parenthesis '()' with comma ','.
    Can contain mixed types.
    Tuples are immutable.
'''

tup = (1, 'c', 3, 'Num')
print(tup)

print(tup[3])

tup2 = tup + (20, 2.3)
print(tup2)


# slicing:
print(tup2[1:2])        # tuple[start:stop] slice from start to (stop - 1)


# the comma ',' tells that this is a tuple:
x = ('c')               # a string
print(type(x))

y = ('c',)              # a tuple (there is a comma ',')
print(type(y))

x = 10
print(type(x))          # int
x = 10,
print(type(x))          # tuple


# Tuples are immutable:
''' (values cannot change once created) 
    so, tuple object does not support item assignment '''
# tup[2] = 5    # Error

# But, you can overwrite the whole tuple
tup = ('f', 2.3)
print(tup)


# Tuples Features: ...................... 

# Use Tuples to swap value:
x = 5
y = 20
(x,y) = (y,x)
print('x = ' + str(x))
print('y = ' + str(y))

# Use Tuples to return more than one value from a function:
def quotient_and_reminder(x,y):
    q = x // y
    r = x % y
    return (q,r)

print(quotient_and_reminder(17,4))


 
# Lists ------------------------------------------------------------------------

''' Denoted by brackets '[]'.
    Can contain mixed types.
    Lists are mutable, so assigning to an element at an index changes the value.
'''
a_list = []             # an empty list
b_list = [2, 'a', 4, True]
L = [1, 2, 3]           # it's favourable to use homogeneous elements
L[1] = 5                # list are mutable
print(L)


# list functions: ...........................

# .append(object)   : add an item to the end of the list
L.append(15)
print(L)

# .extend(list)     : concatinate two lists (append all the items from a list)
L.extend([11,15])
print(L)

# delete element: 
# del(L[index])    : delete element from list L at a specific index
del(L[2])
print(L)

# .remove(element)  : removes a specific element
''' - if element occurs multiple times, removes first occurrance
    - raises a ValueError if there is no such item '''
L.remove(15)
print(L)

# pop element:
# .pop()            : removes and returns the last item in the list
x = L.pop()
print(x)
print(L)
# .pop(index)       : remove an item at any position by including the index of the item
print(L.pop(1))
print(L)

# Spitting a string into a list:
# list(str)         : returns a list with every character from s
s = "I <3 Py"
char_list = list(s)
print(char_list)
# str.split(sep)    : returns a list of strings, splits a string on a character (separator)
print(s.split('<'))
for i in s.split(' '):
    print(i)

# Concatenating list into string:
# str.join(L)       : turn a list of characters into a string separated by the str object
L = ['hi', 'there', 'world!']
s = ' '.join(L)
print(s)
s = '/'.join(L)
print(s)

# Sort this list:
L = [-3, 4, 21, 9, 8, -8]
# Temporarily:      : returns a sorted list of the given list, does not mutate L
list = sorted(L)    # temporarily sort l
print(list)
print(L)            # L is not changed
# Permanently:      : mutates L, sorts the items of the list in place 
L.sort()            # returns None
print(L)

# .reverse()        : Reverse the elements of the list in place
L.reverse()
print(L)


# Lists in Memory (Aliasing vs Cloning): .....................
# Aliasing
l1 = [1,2,3]
l2 = l1             # here, l2 and l1 refer to the same object: list in memory

l2[1] = 9           # Changes made with one alias affect the other
print(l1)

# Cloning
l3 = [1,2,3]
l4 = l3[:]          # here, you simply make a copy of all the lements of the list l3
                    # Remember: the slice list[start:stop] returns a list
l4[1] = 9
print(l3)
print(l4)

L1 = [5, -9, 2]
L2 = sorted(L1)     # Remember: sorted(list) returns a sorted list of the given list
print(L1)
print(L2)


# Mutation and Iteration: .............................
''' Dont iterate over a list that you change its length
    Here is a function to remove elements from l1 if they are present in l2: '''

# wrong remove-dups function:
def remove_dups_wrong(l1,l2):
    for e in l1:
        if e in l2:
            l1.remove(e)    # when removing an element, all the next elements indeces decrease by 1 

l1 = [1,2,3,4,5]
l2 = [2,3]
remove_dups_wrong(l1,l2)
print(l1)


# remove-dups function:
def remove_dups(l1,l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)    # here, we remove from the original l1, 
                            # yet we iterate over the l1_copy that is not changed 

l1 = [1,2,3,4,5]
l2 = [2,3]
remove_dups(l1,l2)
print(l1)



# Dictionaries -----------------------------------------------------------------
''' Use a key to access the value.
    Key can be any immutable type. '''

my_dict = {}            # initializing an empty dictionary
grades = {'Ana':'B', 'John':'A+', 'Denise':'A'}
print(grades['Ana'])

# Add a new entery into the dict object:
grades['Dina'] = 'C'    # automatically adds new element if not existed
print(grades)

# Test whether a key is (in / not in) the dict:
if 'John' in grades:
    del(grades['John'])
print(grades)

# Getting all the dict keys or values:
# keys()                : to get an iterable that acts like a tuple of all keys
keys = grades.keys()
print(keys)
print(type(keys))       # dict_keys type: acts like a tuple

for i in keys:
    print(i)

# values()              : to get an iterable that acts like a tuple of all values
values = grades.values()
print(values)
print(type(values))     # dict_values type: acts like a tuple


# Dictionary Operators: ............................
d1 = {'A':10, 'B':20}

# iterating over the dict obejct:
for key in d1:
    print(key + ':' + str(d1[key]))
    
# Retrieving dict element value:
x = d1['A']
print(x)

# x = d1['C']           # Error: KeyError: 'C'

# or you can use .get(key)
x = d1.get('A')
print(x)

x = d1.get('C')         # returns None (No Error)
print(x)

x = d1.get('C', -1)     # returns -1 if key does not exist
print(x)

# Extending a dictionaryby another one:
d2 = {'C':30, 'D':40, 'E':50}
d1.update(d2)
print(d1)


#-------------------------------------------------------------------------------
