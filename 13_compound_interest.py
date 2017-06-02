principal = float(input('What is the principal amount? '))

rate = float(input('What is the rate? '))

time = int(input('What is the number of years? '))

compounded = int(input('What is the number of times the interest is compounded per year? '))

#Calculations

roi = principal*(1 + ((rate/100)/compounded))**(compounded*time)

# Output
print(principal,'invested at',rate,'% for', time,'compounded',compounded,'times per year is $',round(roi,2))