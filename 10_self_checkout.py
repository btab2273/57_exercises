# Input item prices: item1_price, item1_units, item2_price, item2_units
# item3_price, item3_units
item1_price = int(input('Enter the price of item 1: '))
item1_units = int(input('Enter the quantity of item 1: '))

item2_price = int(input('Enter the price of item 2: '))
item2_units = int(input('Enter the quantity of item 2: '))

item3_price = int(input('Enter the price of item 3: '))
item3_units = int(input('Enter the quantity of item 3: '))

# Calculations: item1_cost, item2_cost, item3_cost, sub_total, sales_tax,tax_rate
item1_cost = item1_price*item1_units

item2_cost = item2_price*item2_units

item3_cost = item3_price * item3_units

sub_total = item1_cost + item2_cost + item3_cost

tax_rate = 0.055

sales_tax = sub_total*tax_rate

total = sub_total + sales_tax

# Output
print('Subtotal: ',float(sub_total))
print('Tax: ', sales_tax)
print('Total: ',total)