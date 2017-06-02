# Input the first number: first_num
first_num = input('What is the first number? ')
first_num = int(first_num)

# Catch value errors for negative numbers
if first_num < 0:
    raise ValueError ('Enter a positive integer')

# Input the second number: second_num

second_num = input('Wnat is the second number?')
second_num = int(second_num)

# Catch value errors for negative numbers
if second_num < 0:
    raise ValueError ('Enter a positive integer')


# Print the simple maths
# addition
print(first_num, "+" ,second_num, "=", first_num + second_num)

# subtraction
print(first_num, "-",second_num, "=", first_num - second_num)

# multiplication
print(first_num, "*",second_num, "=", first_num * second_num)

# division
print(first_num, "/",second_num, "=", first_num / second_num)

