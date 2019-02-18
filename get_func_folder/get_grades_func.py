    


def get_grades():
    while True:
        
        grade = (input('Enter grade(A/B/C/D/F): '))
        grades  =  []
        if grade in ["A", "B", "C", "D", "F"]:
            grades.append(grade)
            answer = input("Would you like to add another grade?(y/n): ")
            if answer == "n":
                    break
        else:
            print("Invalid input.")    





    

