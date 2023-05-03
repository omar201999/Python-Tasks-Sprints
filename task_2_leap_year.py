# this function take a year and determine is a leap year or not
def is_leap(year) -> int:
    # take a Integer input and initialising boolean variable to check is a leap year or not
    leap = False
    if year % 4 == 0:
        # if year  can be evenly divided by 4 is a leap year if not then it's not a leap year
        leap = True
        if year % 100 == 0:
            # if year can be evenly divided by 100 is not  a leap year if not then it's a leap year
            leap = False
            if year % 400 == 0:
                # if year can be evenly divided by 400 is  a leap year if not then it's not a leap year
                leap = True
    return leap


print(is_leap(2100))
