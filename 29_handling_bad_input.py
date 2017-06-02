# Exercise 29 - Handling Bad Input

# Write a calculator for the rule of 72

while True:
    r = int(input('What is your rate of return? '))

    if r > 0:
        break
    else:
        print('Sorry that is not a valid input.')
        int(r)

years = int(72/r)

print('It will take you', years, 'years to doulbe your investment')
