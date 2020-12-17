myinput = input('Give me a number:')
print(myinput, type(myinput))

# casting - convert from one type of data to another

# string to int
num = int(myinput)
print(myinput, type(myinput), num, type(num))

# string to float
num = float(myinput)
print(myinput, type(myinput), num, type(num))

# to boolean
b = bool(0)
print(0, b, type( b ) ) # 0 is False

# Any data that is NOT 0 or False will be True!
b = bool(1)
print(1, b, type(b) )

v = 5
print(v, type(v), 'After casting to boolean: ', bool(v))

v = .5
print(v, type(v), 'After casting to boolean: ', bool(v))

v = '5'
print(v, type(v), 'After casting to boolean: ', bool(v))

v = 'False'
print(v, type(v), 'After casting to boolean: ', bool(v))

v = False
print(v, type(v), 'After casting to boolean: ', bool(v))
