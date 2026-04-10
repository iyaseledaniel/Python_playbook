# learning how continue works in a loop
""" pc_owner = "daniel"
family = ['stephen', 'kelvin', 'daniel', 'magdalene','matthew','destiny']

for name in family:
    if name == pc_owner:
        continue
    print(name) """

#Program to print multiplication table/ using continue statement

user_input = int(input("How many multiplication table do you want: "))
table_length = int(input("How long should each table be: "))

for i in range(1,user_input+1):
    print("Multiplication Table ", i)
    for j in range(1,table_length+1):
        if j == 7:
            continue
        print("{}*{}={}".format(i,j,i*j))
    print("\t")


