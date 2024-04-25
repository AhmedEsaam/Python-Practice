# Comparison Operators:
'''
    >   >=  <   <=  ==  !=   
'''

# Boolean logic Operators
'''
    not     and     or
'''

# Conditional Statements -------------------------------------------------------

# if ... else Statement
x = int(input('Please Eneter a Number: '))

if (x % 2 == 0):
    print("Even")
else:
    print("Odd")

print('Done with conditional')


# Nested If
x = int(input('Please Eneter a Number: '))

if (x % 2 == 0):
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')   
elif x%3 == 0:
    print("Divisible by 3 and not by 2")

print('Done with conditional')


# Compound Booleans
x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')



# Loops ------------------------------------------------------------------------

# While Loops
n = 0
while n < 5:
    print(n)
    n = n+1


# For Loops
for n in range(5):          # range(int) returns a list {0 : (int - 1)}
    print(n)

sum = 0
for i in range(7,11):       # range(start, stop) returns a list from start to (stop - 1)
    sum += i
print(sum)

print()
for i in range(2, 11, 3):   # range(start,stop,step) : list from start to (stop-1) with step
    print(i)


# Break Statements
print()
mysum = 0
for i in range(5,11,2):
    mysum += i
    if mysum == 5:
        break               # stops the loop at this point
print(mysum)


# For Loops with Strings
print()
s = 'abcdefgh'

for index in range(len(s)):
    print(s[index])
print()

for char in s:              # iterates over whatever the list is (here, the string characters)
    print(char)



# Algorithms -------------------------------------------------------------------

# Bisection Search Algorithm (Binary Search)
print('Please think of a number between 0 and 99!')
low = 0; high = 100; mid = (low + high) // 2 

while True:
    print('Is your secret number is ' + str(mid) + '?')
    ans = input("Enter 'h' to indicate the guess is too high.\n\
                Enter 'l' to indicate the guess is too low.\n\
                Enter 'c' to indicate I guessed correctly.\n= ")

    if ans == 'c':
        print('Game Over. Your secret numebr was: ' + str(mid))
        break    
    elif ans == 'h':
        high = mid; 
        mid = (high + low) // 2
    elif ans == 'l':
        low = mid; 
        mid = (high + low) // 2
    else:
        print('Sorry, I did not understand your input.')


#-------------------------------------------------------------------------------

    