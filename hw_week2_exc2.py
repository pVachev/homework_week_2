def get_grades():
    while True:
        try:
            grade = (int(input('Enter grade(2/3/4/5/6): '))) 
            if grade in [2,3,4,5,6]:
                grades.append(grade)
                answer = input("Would you like to add another grade?(y/n): ")
                if answer == "n":
                        break
            else:
                print("Invalid input.")
        except:
            print("Bro, What the fuck?")       

students = {}
for i in range(0,3):
    name = input("Enter name: ")
    grades = []
    get_grades()
    my_student = {'name': name, 'grades': grades}
    students[i] = my_student

for i in range(0,len(students)):
    print(students[i]["name"]+ "'s grade average")
    sum = 0
    for grade in students[i]["grades"]:
        sum += grade
    sum = sum/len(students[i]["grades"])
    print(sum) 





