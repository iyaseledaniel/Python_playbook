#how to use regular expressions in code
import re
from time import time

start_time = time()

age_pattern = re.compile(r'(\d+)')
email_pattern = re.compile(r'[a-zA-Z0-9._#&$]+@[a-zA-z0-9]+\.[a-zA-Z]+$')
name_pattern = re.compile(r'[a-zA-Z]+')

def test_cond(args):
    """Method to handle test conditions depending on mismatch data from user input
     if (1 or 2 or 3) data mismatch print (1,2,3) corresponding error message
     else save data to text file
    """
    key = [] # empty list to store users key
    value = [] # empty list to store results after comparing user's input with regular expression pattern
    for k,v in (args.items()):
        key.append(k)
        value.append(args[k])
    #print(key,value) #Testing output
    counter = value.count(None) # get numbers of mismatch data
    for index in range(len(key)-2):
        #Use first index key to compare other keys for mismatch
        index2 = index + 1
        for index2 in range(1,len(key)):
            # loop through 2nd index till last for comparison

            if counter == 1:
                if not value[index]:
                    print(f"Please enter a valid {key[index]}")
                    break
            elif counter == 2:
                if not value[index] and not value[index2]:
                    print(f"Please enter a valid {key[index]} and {key[index2]}")
                    break
            elif counter == 3:
                print("Please enter valid details")
                # print(f"Please enter valid {key[index]},{key[index2]} and {key[index2+1]}")
                break



while True:
    name = input("Please enter your name: ")
    email = input("Please enter your email address: ")
    age = (input("Please enter your age: "))

    #validate user input
    test_name = name_pattern.fullmatch(name)
    test_email = email_pattern.fullmatch(email)
    test_age = age_pattern.fullmatch(age)

    if test_name and test_email and test_age:
        with open("profile.txt", "a") as profile:
            profile.write("\nProfile: ")
            profile.write(name+"," +email + ","+ age)
            print("profile created and saved Successfully")

        endtime1 = time()
        print(f"Time taken: {endtime1 - start_time}")

        repeat = input("Would you like to create another profile (y/n)? ")
        if repeat.lower() == "y":
            continue
        else:
            break
    elif not test_name:
        data = {"name": test_name, "email": test_email, "age": test_age}
        test_cond(data)

    elif not test_email:
        data = {"email": test_email,"name": test_name, "age": test_age}
        test_cond(data)

    elif not test_age:
        data = {"age": test_age, "name": test_name, "email": test_email}
        test_cond(data)
end_time = time()
print(f"Time taken: {end_time - start_time} seconds")
