# Coder: Daniel Iyasele
# Date: 28/01/2026
"""Program that creates a simple class template for twitter
  Twitter is a class(subclass of social media) with different users as object
  Each object(user) has different attributes and
   can perform different actions(method) based on their premium status
"""


class Twitter:
    def __init__(self, name, age, location, sex, verified):
        self.name = name
        self.age = age
        self.location = location
        self.sex = sex
        self.verified = verified

    @staticmethod
    def user_input():
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        location = input("Enter your location: ")
        sex = input("Enter your sex: ")
        premium = input("Are you a premium user? (Y/N): ")

        return name, age, location, sex, premium

    def is_user_premium(self):
        if self.verified:
            return "You are a premium user"
        else:
            return "You are not a premium user"

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Location:", self.location)
        print("sex:", self.sex)
        print(self.is_user_premium())
        print(self.write_article())
        print(self.lock_comments())

    def write_article(self):
        # method to return your x benefit based on your premium status
        if self.verified:
            return "You can write an article on x"
        else:
            return "You cannot write an article on x"

    def lock_comments(self):
        # method to return your x benefit based on your premium status
        if self.verified:
            return "You can lock comments on x"
        else:
            return "You cannot lock comments on x"


# initialize loop counter for iteration
i = 0

# create empty object list to store details of different users
user_list = []

while True:
    """Loop to ask user for details,
     append to empty object list then terminates if user response is no"""

    name, age, location, sex, premium = Twitter.user_input()  # Assign userinput() return values to the variables
    if premium.upper() == "Y":
        # checks for premium user status and assigns value to premium and update object to boolean
        premium = True
        user = Twitter(name, age, location, sex, premium)
    else:
        premium = False
        user = Twitter(name, age, location, sex, premium)
    user_list.append(user)
    # Append user objects to userlist

    response = input("Do you want to input another set of details ? (Y/N):")
    print("\n")
    if response.upper() == "Y":
        i = i + 1
        print("Entering another set of details.....")
        continue  # control returns to start of loop if user inputs is yes(Y)
    else:
        break  # loop terminates if user inputs is no(N)

for detail in user_list:
    # loop to print user details
    print(".....User details....")
    detail.display()
    print("\n")
