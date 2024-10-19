""" This is the Scratchpad!
This file is not graded, but you can use it to test your code.

You can write and test your function in the Scratchpad, but make
sure to copy and paste it into the Unit Test file before checking
your answer. Remember to only copy and paste the function you want
to submit, not all of your tests.
"""
import math
import time

# Add your own tests here

def gauss_easter(y):
    a=y%19
    b=y%4
    c=y%7
    p = math.floor(y / 100)
    q = math.floor((13 + 8 * p) / 25)
    m = (15 - q + p - p // 4) % 30
    n = (4 + p - p // 4) % 7
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    if ((d == 29) and (e == 6)):
        print("April 19, " + str(y))
        
        y="April 19, " + str(y)
    elif ((d == 28) and (e == 6)):
        print("April 18, " + str(y))
        
        y="April 18, " + str(y)
    elif ((22 + d + e) > 31):
        print("April " + str(22 + d + e - 31) + ", " + str(y))
        
        y="April " + str(22 + d + e - 31) + ", " + str(y)
    else:
        print("March " + str(22 + d + e) + ", " + str(y))
        y="March " + str(22 + d + e) + ", " + str(y)
    
    return y
yrs = input("How many easters to calculate?: ")
yr=1
if yrs=="all":
    while True:
            gauss_easter(yr)
            yr=yr+1
            time.sleep(0.1)
else:
    gauss_easter(int(yrs))
