# Inputs: principle, interest_rate, years

principal = float(input('Enter the principle: '))
interest_rate = float(input('Enter the rate of interest: '))
years = int(input('Enter the number of years: '))


# Calculations: simple interest, roi
simple_interest = principal*(1 + ((interest_rate/100)*years))
roi = principal + simple_interest
# Output
print('After', years, 'at', interest_rate, '%, the investment will be worth $', roi, '.')
