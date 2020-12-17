# Numbers

# integer - whole number
int1 = 187687623048234729384729384
int2 = -98
int3 = 0
int4 = 4

print(int3 + int2)
print(int3 - int2)
print(int2 * int4)

print('int1 type: ', type(int1*int4))

# float - fractions
float1 = 3.14
float2 = 11.0
float3 = .8

print(float1 + float2)
print(float1 - float2)

print('float1 type: ', type(float1))


# Exercise
# Create 2 variables num1 with value 8 and num2 with value 4
num1 = 8
num2 = 4
# Add the variables and save results in a variable named res
res = num1 + num2
# What is res type?
print('res', res, type(res))

# Divide the variables and save results in a variable named res2
res2 = num1 / num2
# What is res2 type?
print('res2', res2, type(res2))

# Modulus - retuns the left over of the division
print('10 % 2 = ',  10 % 2 )
print ( '8 % 5= ', 8 % 5 )
print( '5 % 2= ',5 % 2 )

# using operators only how do I divide 2 integers and get an integer value
print( '8 // 5 = ', 8 // 5 )

# Power of
print('2**4 = ', 2**4)
print('1**14 = ', 1**14)


# Strings
# A collection of characters
empty_string = ''
stam_string = 'Stam string haya po'
single_quote_str = ''
double_quote_str = ""
single_quote_str1 = '"'
double_quote_str1 = "'"

multi_line_string = '''
Hello,
I am a multi line string...
'''
print(multi_line_string)
multi_line_string2 = """
Second way
creating a multi line string with double quotes
"""
print(multi_line_string2)

# Escape characters:
print('I can\'t. Do this')
print('I can\"t. \nDo this')
print('\tTab is written by \\t')

"""
Write the following message in console

Please enter a number and choose an action:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division 
"""
print('\n\nPlease enter a number and choose an action:\n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division')


# Boolean (True or False)
b = True
bs = False

print(b, bs, type(b))


