# learning how to use list

a = [1,2,3,49,'daniel','stevo','maggy']

count = 1
while count <= len(a):
    print(a[0-count])
    count += 1

# looping nested list
nested_list = [[1,2,3],[4,4,5,6],[7,8,8]]

for rows in nested_list:
    for item in rows:
        print(item, end=" ")

#""" list comprehension """o
a = [1,2,3,4,5,6,7,8,9]
#number = [item for row in nested_list for item in row]
#print(number)