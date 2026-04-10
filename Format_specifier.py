# working with format specifier

name = "Biggs"
country = "South Africa"
sex = "Male"
age = 40

print("My name is %s, I am from %s, a %s and i am %d years old" %(name, country, sex, age))

print("My name is {}, I am from {}, a {} and i am {} years old".format(name, country, sex, age))

# printing values in different format

value =int (input("Please enter a number: "))
print("The number you input in integer is: {:d}".format(value))
print("The number you input in float is: {:f}".format(value))
print("The number you input in binary is: {:b}".format(value))
print("The number you input in octal is: {:o}".format(value))
print("The number you input in hexadecimal is: {:x}".format(value))
