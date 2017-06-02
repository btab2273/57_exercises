import sys

# Get user input: char_count

char_count = input('What is the input string? ')

# Raise an error for no input or non-string
if len(char_count) == 0:
   raise TypeError ('Input must be a string!')

# Print the character count
print(char_count+ ' has', +len(char_count), 'characters.')