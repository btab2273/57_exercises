import math
# Exercise 26 - Months to Pay Off a Credit Card

# Assign variables: num_months, daily_rate(APR/365), bal, payment

bal  = float(input('What is your balance (USD)?'))

apr = float(input('What is the APR on the card (as a percent)? '))

payment = float(input('What is the monthly payment you can make (USD)? '))

daily_rate = apr/365
def pay_calendar():
    """ function to determine how long it takes"""
    
    divisor = math.log10(1+(bal/payment)) * (1 - ((1 + daily_rate)**30))
    dividend = math.log10(1+daily_rate)
    months = divisor/dividend*(-1/30)
    return months

time_till = pay_calendar()

print(time_till)