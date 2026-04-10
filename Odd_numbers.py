# using continue with while loop to print odd numbers

number = int(input("Enter a number: "))
counter = 1

while counter < number:
    if counter == 7:
        #counter += 1
        continue
    else:
        print(counter)
        counter += 1