#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Student Name"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Returns True if the year is a leap year"
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check."
    # Days in months for regular years
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # If it's February and the year is a leap year, return 29 days
    if month == 2 and leap_year(year):
        return 29
    
    return days_in_month[month - 1]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for years after 1582.
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # Increment the day by one
    tmp_day = day + 1  # Next day

    # Check if the day exceeds the maximum days in the month
    if tmp_day > mon_max(month, year):
        to_day = 1  # Reset day to 1
        tmp_month = month + 1  # Increment month
    else:
        to_day = tmp_day
        tmp_month = month

    # If the month exceeds 12, reset to January and increment the year
    if tmp_month > 12:
        to_month = 1
        year += 1
    else:
        to_month = tmp_month

    # Return the next date in the format YYYY-MM-DD
    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def valid_date(date: str) -> bool:
    "Check validity of date and return True if valid"
    # Ensure the date is in the correct format: YYYY-MM-DD
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        return False
    
    try:
        # Try to split the date into year, month, day
        year, month, day = map(int, date.split('-'))

        # Check if the month is valid (1-12)
        if month < 1 or month > 12:
            return False
        
        # Check if the day is valid for the given month/year
        if day < 1 or day > mon_max(month, year):
            return False
        
        return True
    except ValueError:
        # This will handle cases where the date is not in correct format or cannot be converted
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    count = 0
    current_date = start_date

    # Loop through all days starting from start_date to stop_date inclusively
    while True:
        year, month, day = map(int, current_date.split('-'))
        # Check if the current day is a weekend (Saturday or Sunday)
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1
        
        # Stop the loop when the current date equals the stop date
        if current_date == stop_date:
            break
        
        # Move to the next day
        current_date = after(current_date)

    return count

if __name__ == "__main__":
    # Check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    # Check if the dates are valid
    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # Ensure start_date is earlier than end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    # Calculate the number of weekend days
    weekend_days = day_count(start_date, end_date)

    print(f"The period between {start_date} and {end_date} includes {weekend_days} weekend days.")

