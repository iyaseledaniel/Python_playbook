# working with list comprehension in python

number_list  = [-12,-10,-11,-9,-1,0,3,5,8,9,7,6,4]

positive_even_numbers = [x for x in number_list if x % 2 == 0 and x > 0]
#print(positive_even_numbers)


# moving zeros to the end

def move_zeros(lst):
    zero_list = []
    zero = 0
    while zero in lst:
        zero_list.append(zero)
        lst.remove(zero)
    lst.extend(zero_list)
    return lst

test1 =  [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
test2 =  [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros(test1))
print(move_zeros(test2))