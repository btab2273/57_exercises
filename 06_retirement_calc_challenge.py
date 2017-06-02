# Import datetime
import datetime

# Create variables for all of the inputs


current_age = int(input('What is your current age? '))

retirement_age = int(input("At what age would you like to retire? "))

years_out = int(retirement_age - current_age)

current_year = datetime.datetime.now(().strft('%Y'))