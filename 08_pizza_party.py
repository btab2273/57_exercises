# Collect input: num_people, pizzas
num_people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))


# The math
slices = 8 
pie_divy = pizzas*slices
slices_per_person = pie_divy//num_people
left_overs = pie_divy%num_people


#Output
print(num_people,'people with',pizzas,'pizzas')
if slices_per_person >=2:
    print('Each person gets',slices_per_person,'pieces of pizza.')
else:
    print('Each person gets 1 piece of pizza')

print('There are',left_overs,'leftover pieces.')


 