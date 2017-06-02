import datetime
# input current age: age
age = input('What is your current age? ')
age = int(age)
# input retirement age: retire
retire = input('At what age would you like to retire? ')
retire = int(retire)

# print the number of years before retirement
years_till = retire-age


    
if age >= retire:
        print("You can retire already!")
    
else:
    print('You have',years_till, 'years left until you can retire.')

    # print the year of retirement: retire_date
    current_date = datetime.datetime.now().strftime('%Y')
    current_int = int(current_date)
    
    print("It's",current_date+",so you can retire in",current_int+retire)
        
