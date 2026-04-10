# program to guess users year of birth
from datetime import datetime
import random
import pdb

year = datetime.today().year

print("Guessing your year of birth and printing your age......")
while True:
    random_year = random.randint(1900, 2026)
    # print(random_year) cheat the guessing system
    birth_year = int(input("Enter birth year (1900-2026): "))
    age = year - birth_year
    # pdb.set_trace()
    if birth_year < 1900 or birth_year > 2026:
        print("Please try again with a year between 1900 and 2026")
    elif birth_year == random_year:
        print(f"Oh we gotcha!!! Birth year is: {random_year} and you are {age} years old")
        break
    else:
        print("Oh guess was wrong")
        print(f"Please try again our guess was {random_year}")