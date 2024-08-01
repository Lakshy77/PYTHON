#Employee_file = open("newtext.txt","r")
'''print(Employee_file.readline())
print(Employee_file.readline())
print(Employee_file.readline())
print(Employee_file.readlines())
print(Employee_file.readlines()[1])
for employee in Employee_file.readlines():
    print(employee)
#WRITE IN FILE
Employee_file = open("newtext.txt","a")
Employee_file.write("\nKelly - Human Resource")'''
Employee_file = open("newtext.txt","w")
Employee_file.write("\nKelly - Human Resource")
Employee_file.close()