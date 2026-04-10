# using lamda for various purposes
# also using filter(), map() and reduce() with lambda
from Learning_phase_python.func_example import addition

#lamda fn to print squares of number

square = lambda x: x * x
print(square(20))

#using filter() to filter odd numbers

num_list = list(range(100))
odd_num_list = list(filter(lambda x: x % 2 != 0, num_list))
print(odd_num_list)

#using map()

divide_by_two = list(map(lambda x: x / 2, odd_num_list))
print(divide_by_two)

#using reduce() we need to import it from functools
from functools import reduce

addition = reduce(lambda x, y: x + y, num_list)
print(addition)
