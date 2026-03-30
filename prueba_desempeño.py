institution = {}

def add_student(institution):

    print("\n add new student")

    go = True
    while go: 
        name = str(input("enter student name: ").strip())#It was placed in str because if the student's name is 6, I took it .strip() is to prevent empty space 
        if name: 
            break
        print("Error: the name cannot be empty. Please try again.")

    while go: 
        try: 
            identifications = int(input("Enter your identification number: ").strip())
            if identifications <= 0:
                print ("Please enter a valid number")
            else:
                break
        except ValueError:
            print ("Error: invalid value. Enter a number")

    while go: 
        try:
            age = int(input("Enter age: ").strip())
            if age <= 0:
                print ("Please enter a valid number")
            else: 
                break
        except ValueError: 
            print ("Error: invalid value. Enter a number")

    while go: 
        course = str(input("enter course: ").strip())
        if course: 
            break
        print("Error: The course cannot be entered")

    while go:
        try:
            status = (input("Enter status (active/inactive): "))
            if status == "":
                print("Error: Enter a valid state. Please try again.")
            else:
                break
        except ValueError:
            print("Error: Enter a valid status.")

    aggregates = {"name": name, "id": identifications, "age": age, "course": course, "status": status }
    institution.append(aggregates)

def check_student_list(institution):

    print("\n--- student list ---")

    if len(institution) == 0:
        print ("The student list is empty, please add students")
        return
    
    print ("-" * 20)
    for i, list in enumerate (institution, start=1):
        print(
            f"{1}. student: {institution["name"]}"
        )

def search_student(institution):
    print ("\nSearch_student")
    id = input ("student identification").strip()
    result = search_student(institution, consult_students)
    if result:
        print (f"\n student found")
        print (f"Nmbre: {result['nombre']}")
        print (f"id: {result['identifications`']}")
        print (f"course {result['course']}")
    else: 
        print (f" student {id} not found")

def update_student_information(institution):
    print("\n update student ")
    name = input ("name of the student who wishes to update")

    if not search_student(institution, name): 
        print (f" student {name} not found" )
        return
    
    print ("*If you do not wish to modify a value, please leave it blank.*")

    identifications = input = ("Enter your new ID:").strip()
    new_identifications = int (identifications) if identifications else None

    name = input ("enter new name: ").strip()
    new_name = str (name) if name else None

    age = input ("enter new age:").strip()
    new_age = str (age) if age else None

    course = input ("enter new course: ").strip()
    new_course = str (course) if course else None

    status = input ("enter new status: ").strip()
    new_status = str (status) if status else None 

    if identifications is None and age is None and course is None and status is None and name is None:
        print("  ℹNO CHANGE WAS MADE")
        return
    
    institution(new_identifications, new_name, new_age, new_course, new_status)

def remove_student(institution):
    print ("\n remove students")
    name = input ("name of student you wish to delete: ")

    if not search_student(institution, name): 
        print (f"name {name} not found")
        return
    
    confirm = input (f"¿You confirm to delete {name}? (S/N): ").strip().upper()
    if confirm == "S":
        
def delete_student (institution, name):
    name = search_student(institution, name)

    if not name:
        print (f"name {name} not found")
    return False

institution.remove(name)
print (f"producto {name} not found")
return True


def show_menu():
  
    print("\n" + "-" * 20)
    print ("(1) register student")
    print ("(2) check student list")
    print ("(3) search student")
    print ("(4) update student information")
    print ("(5) remove student")
    print ("(6) exit")
    print ("\n " + "-" * 20)


def menu ():
    print("\nWelcome to the menu!")
    go = True

    while go: 

        show_menu()

        option = input ("select an option (1-6): ").strip()

        if option == "1":
            add_student()
        
        elif option == "2":
            check_student_list()

        elif option == "3":
            search_student()
        
        elif option == "4":
            update_student_information()

        elif option == "5":
            remove_student()
        
        elif option == "6":
            print ("\nExiting the system . Goodbye")
            go = False

        else: 
            print ("\nInvalid option, please enter an option from (1-6)")


def consult_students():

    print ("\nstudent list")

    if len(institution) == 0:
        print (" The list is empty. Please add students.")
        return
    print ("-" * 10)
    for i, institution in enumerate(institution, start=1):