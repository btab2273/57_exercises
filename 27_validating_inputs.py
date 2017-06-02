# Exercise 27 - Validating Inputs

# import regex
import re

# Prompt user for inputs: f_name,l_name, employee_id, zip_code
# Check for errors

f_name = input('Enter the first name: ')

l_name = input('Enter the last name: ')

zip_code = int(input('Enter the ZIP code:'))

employee_id = input('Enter an employee ID: ')

# Functions for error checking


def name_check(f_name):
    """ Check the length of the first name """
    if len(f_name) == 0:
        print('The first name must be filled in.')
    if len(f_name) < 2:
        print(f_name + ' is not a valid name. Itis too short.')


def last_check(l_name):
    """ Check the length of the last name """
    if len(l_name) == 0:
        print('The last name must be filled in.')
    if len(l_name) < 2:
        print(l_name + ' is not a valid last name. It is too short.')


def id_check(employee_id):
    """ Use regex to make sure the employee_id matches the pattern"""
#    badge_pattern = re.compile('[A-Za-z]{2}-\d{4}')
#    re.search(badge_pattern, employee_id)

    # if statement
    if not re.match('[A-Z]{2}-\d{4}', employee_id):
        print(employee_id, 'is not a valid ID.')


def valid_input_func():
    name_check(f_name)
    last_check(l_name)
    id_check(employee_id)

valid_input_func()
