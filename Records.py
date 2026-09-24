def Register_Student(student_list):
    student_first_name = input("Enter First name of the student: ")
    student_last_name = input("Enter Last name of the student: ")
    student_age = int(input("Enter the age of the student: "))
    print("Follow the instructions to specify the course of the student - ")
    student_course = int(input("Press :\n 1: Computer Science and Engineering\n 2: Mechanical Engineering\n 3: Chemical Engineering\n 4: Electrical and Electronics Engineering\n 5: Aerospace Engineering\n 0: None of the above\n Enter: "))
    if student_course==1:
        course = "Computer Science and Engineering(CSE)"
    elif student_course==2:
        course = "Mechanical Engineering(ME)"
    elif student_course ==3:    
        course = "Chemical Engineering(CE)"
    elif student_course==4:
        course = "Electrical and Electronics Engineering(ECE)"
    elif student_course==5:
        course = "Aerospace Engineering(AE)"
    elif student_course==0:
        course = None
    student_details = {"First Name":student_first_name, "Last Name":student_last_name, "Age":student_age, "Course":course}
    a = Registration_number_generator()
    student_list[a]=student_details
    return student_list, a


def Registration_number_generator():
    import random
    reg_no = ""
    for i in range(10):
        reg_no += str(random.randint(1,8))
    return reg_no


def Update_Student(student_list):
    while True:
        registration_number = input("Enter the Registration number of the Student: ")
        if registration_number in student_list:
            a = student_list[registration_number]
        else:
            print("Invalid Registration Number!!")
            break
        
        while True:
            b = int(input("Enter the following to update the information!:\n 1: First Name\n 2: Last Name\n 3: Age\n 4: Course"))
            if b == 1:
                student_first_name = input("Enter First name of the student: ")
                a["First Name"] = student_first_name
            elif b== 2:
                student_last_name = input("Enter Last name of the student: ")
                a["Last Name"] = student_last_name
            elif b == 3:
                student_age = int(input("Enter the age of the student: "))
                a["Age"] = student_age
            elif b == 4:
                print("Follow the instructions to specify the course of the student - ")
                student_course = int(input("Press :\n 1: Computer Science and Engineering\n 2: Mechanical Engineering\n 3: Chemical Engineering\n 4: Electrical and Electronics Engineering\n 5: Aerospace Engineering\n 0: None of the above\n Enter: "))
                if student_course==1:
                    course = "Computer Science and Engineering(CSE)"
                elif student_course==2:
                    course = "Mechanical Engineering(ME)"
                elif student_course ==3:    
                    course = "Chemical Engineering(CE)"
                elif student_course==4:
                    course = "Electrical and Electronics Engineering(ECE)"
                elif student_course==5:
                    course = "Aerospace Engineering(AE)"
                elif student_course==0:
                    course = None
                a["Course"] = course
            elif b == 0:
                break
            else:
                print("Invalid Input")

        student_list[registration_number] = a
    return student_list

def Remove_Student(student_list):

    registration_number = input("Enter the registration number of the student: ")
    if registration_number in student_list:
        del student_list[registration_number]
    elif type(registration_number in student_list) == None:
        print("Invalid Registration Number!!")
    return student_list
        

def Print_Student_Details(student_list):
    while True:
        registration_number = input("Enter the Registration Number of the Student: ")
        if registration_number in student_list:
            a = student_list[registration_number]
        else:
            print("Invalid Registration Number!!")
            break
        for keys,values in a.items():
            print(keys,":",values)

    


        
        
        
