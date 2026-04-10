# program to check list of keywords in python
import keyword

print(keyword.kwlist)

# count all keywords
counter = 0
for i in keyword.kwlist:
    counter = counter + 1
print(counter)