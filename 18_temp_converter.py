def cel_to_far(value):
    """ Convert a celsius temperature to fahrenheit"""
    new_temp = (value-32)*(5/9)
    return new_temp


def far_to_cel(value):
    """Convert a fahrenheit temperature to celsius"""
    new_temp = value*5/9 + (32)
    return new_temp
print('Press C to convert from Fahrenheit to Celsius.')
print('Press F to convert from Celsius to Fahrenheit.')
choice = print(str(input('Enter your choice: ')))

if choice == 'C':
    print(far_to_cel(float(input('Enter the temp in degrees F: '))))


#F  = fahrenheit = print(cel_to_far(float(input('Enter the temp in degrees C:'))))
    
