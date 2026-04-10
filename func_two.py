#testing Global and local variable scope
from pickle import GLOBAL

"""glo_var = "global variable"

def local_function():
    global glo_var
    loc_var = "local variable"
    glo_var = glo_var*2
    print(glo_var)
    print(loc_var)

local_function()
print(glo_var)"""

# testing how nonlocal, global keywords work in nested function

def function1():
    x = 40
    def function2():
        global x
        x = 50
    print("Before calling nested function x is ", x)
    print("Calling nested function ......")
    function2()
    print("After calling nested function x is ", x)
function1()
print("In the main function x is ", x)