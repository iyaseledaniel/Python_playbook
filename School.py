#working with class
from encodings.cp862 import encoding_map


class School:
    def __init__(self,owner, school_name, director_name):
        self.owner = owner
        self.school_name = school_name
        self.director_name = director_name
        self._var = ""
        self.__var2 = ""

    def welcome_message(self):
        print("Hello fellas welcome to ", self.school_name)
        print(self.school_name," is owned by ", self.owner, " and overseen by ", self.director_name)
        print("Please proceed to registering yourself........")

    def registration(self):
        pass

aspirant1 = School("Mr Fashola","Global school of science and technology", "Mr Adeyinka")
aspirant1.welcome_message()
