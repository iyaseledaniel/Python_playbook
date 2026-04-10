# Using break statement
# Program prints item in list but terminates once value is greater than 100

numbers = [30,50,60,80,120,300,100,70,25,210]
#code is not efficient, it does not run through all list to print all values less than 100
for number in numbers: # use sorted(numbers) for efficient output
    if number > 100:
        break
    print(" The Current number:", number)