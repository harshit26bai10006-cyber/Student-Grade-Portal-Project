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

    student_list[Registration_number_generator()]=student_details
    return student_list


def Registration_number_generator():
    import random
    reg_no = ""
    for i in range(10):
        reg_no += str(random.randint(1,8))
    return reg_no