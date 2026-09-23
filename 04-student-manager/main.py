students = []

 

def display_menu():
    print("==== STUDENT MANAGER ====")
    print("01. Add students")
    print("02. View all students")
    print("03. Add/update grades")
    print("04. View student Report Card")
    print("05. Delete student")
    print("06. Exit")

def add_Student():
    student_name = input(" Enter student name: ").strip()
    if student_name == "":
        print("NO RECORD")
        return

    roll_number = (input(" STUDENT ROLL NO. : "))
    if not roll_number.isdigit():
        print(" VALUE ERROR: ENTER NUMBER ONLY")
        return

    roll_number = int(roll_number)

    if any(student["roll_number"] == roll_number for student in students):
        print(" ERROR: Student with this roll number already exists")
        return
    roll_number = int(roll_number)
    new_student={ "student_name":student_name,
                 "roll_number": roll_number,
                  "grades": {} 
                  }
    students.append(new_student)
    print(f"student {student_name} added succesfully to record!! :> <3")



    
def view_student():
    if len(students) == 0:
        print("NOTHING RECORDED YET!!")

    else:
        for student in students:
            print(f"{student['student_name']} | {student['roll_number']}")



            
def find_student_by_roll(roll_number):
    for student in students:
        if student["roll_number"] == roll_number :
            return student
    return None


    
def add_update_grades():
    roll_number = input(" enter student roll number: ")
    if not roll_number.isdigit():
        print("ERROR: ENTER NUMBER ONLY!!!!")
        return
    roll_number= int(roll_number)

    student= find_student_by_roll(roll_number)

    if student is None:
        print(" STUDENT NOT FOUND!!!")
        return

    subject_name = input("Subject Name: ").strip()
    if subject_name == "" :
        print(" NO subject Recorded yet!")
        return
    
    update_grades = input("Score: ")
    try:
        update_grades = float(update_grades)
    except ValueError:
        print("ERROR: Score must be a valid number!")
        return

    if update_grades < 0 or update_grades > 100:
        print(" ERROR")
        return
    student["grades"][subject_name] = update_grades
    print(" Grades Updated!")



def view_report():
    pass




def delete_student():
    pass



def main():
    while True:
        display_menu()

        choice = input (" Select option from 1 - 6: " )

        if choice == "1":
            add_Student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            add_update_grades()

        elif choice == "4":
            print("Viewing student report card feature coming ssoon!!!")
            view_report()

        elif choice == "5":
            print("deleting a student record coming soon!!!")
            delete_student()

        elif choice == "6":
            print("EXIT!!!!")
            break

        else:
            print("INVALID OPTION!")




if __name__ == "__main__":
    main()