#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end_number = number % 10

if end_number > 5:
    print(f"Last digit of {number} is {end_number} and is greater than 5")
elif end_number == 0:
    print(f"Last digit of {number} is {end_number} and is 0")
else:
    print(f"Last digit of {number} is {end_number} and is less than 6 and not 0")
