# Input variables: room_lenght, room_width, metric_area

room_length = int(input("What is the length of the room in feet? "))
room_width = int(input("What is the width of the room in feet? "))



#try:
#    room_length+=1
#except ValueError:
#    print('Enter an integer')
    

standard_area = (room_length*room_width)
# Define a metric converter
def converter(standard_area):
    return (room_length*room_width) * 0.09290304

# Confirm the values

print("The area is:")
print(str(standard_area)+" square feet")
print(converter(standard_area),"square meters")