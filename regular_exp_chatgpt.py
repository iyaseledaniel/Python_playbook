import re
from time import time
Start_time = time()
while True:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")

    invalid_fields = []

    # Name validation
    if not re.fullmatch(r"[A-Za-z ]+", name):
        invalid_fields.append("Name")

    # Email validation
    if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
        invalid_fields.append("Email")

    # Age validation
    if not re.fullmatch(r"\d{1,3}", age) or not (1 <= int(age) <= 120):
        invalid_fields.append("Age")

    # Check invalid fields
    if len(invalid_fields) == 1:
        print(f"{invalid_fields[0]} invalid")

    elif len(invalid_fields) == 2:
        print(f"{', '.join(invalid_fields)} fields invalid")

    elif len(invalid_fields) == 3:
        print(f"{', '.join(invalid_fields)} fields invalid. Please enter again.\n")
        continue

    else:
        # All valid → save to file
        with open("user_details.txt", "a") as file:
            file.write(f"Name: {name}, Email: {email}, Age: {age}\n")

        print("Details saved successfully")
        break
end_time = time()
print(f"Time taken: {end_time - Start_time} seconds")