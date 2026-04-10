#testing execution time for tuple and list
import datetime
from time import time

#code to calculate time to loop a list
test_list = list(range(1,100))

start_time = time()
print("List loop started at: ", start_time)

for i in test_list:
    print(i, end=" ")
print("\n")

end_time = time()
list_loop_time = end_time - start_time
print("List loop ended at: ", end_time)
print("Time taken to iterate list is: ", list_loop_time)

# code to calculate time to loop a tuple
test_tuple = tuple(range(100))

tuple_start_time = time()
print("Tuple loop started at: ", tuple_start_time)
for i in test_tuple:
    print(i, end=" ")
tuple_end_time = time()
tuple_loop_time = tuple_end_time - tuple_start_time
print("Tuple loop ended at: ", tuple_end_time)
print("Time taken to iterate tuple is: ", tuple_loop_time)