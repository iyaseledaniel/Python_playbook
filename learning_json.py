#learning how to use json file
import json

def get_studentdetails():
    data={}
    data['name']=input("Enter Student name")
    data['class']=input("Enter Class")
    data['maths']=input("Enter Marks for Maths")
    data['eng']=input("Enter English Marks")
    data['sci']=input("Enter Science Marks")
    return (data)
out=[]
while True:
    quit =input("Enter Y/N to continue")
    if quit.lower() == 'n':
        break
    record = get_studentdetails()
    out.append(record)


with open('students.json','a') as file:
    json.dump(out,file,indent=4)
