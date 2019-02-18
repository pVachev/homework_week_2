from get_grades_folder import get_grades_func 



name = input("enter name: ")

grades = []

get_grades_func.get_grades()
my_student = {'name': name, 'grades': grades}



print(my_student["name"]+ "'s grades")

s = ""
for grade in my_student["grades"]:
    s+= grade + ", "
print(s[0:-2]) 
