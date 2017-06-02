# Excercise 11 - Currency Conversion

# Import the forex converter: c
from forex_python.converter import CurrencyRates as c
from forex_python.converter import CurrencyCodes

# Force decimals and get the currency symbols: c, code
c = c(force_decimal=True)
code = CurrencyCodes()

# Collect user input: euros
euros = int(input('How many euros are you exchanging?'))

rate = round(c.get_rate('EUR', 'USD'), 2)
print(code.get_symbol('EUR'),euros, 'euros at an exchange rate of' , rate, 'is', round(c.convert('EUR', 'USD', euros), 2), 'U.S. Dollars. \n')