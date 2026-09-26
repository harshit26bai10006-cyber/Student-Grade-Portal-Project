def add_marks(student_list):
    common_subjects = {"English": 0,
                       "EVS" : 0,
                       "Maths" : 0
                       }
    registration_number = input("Enter your Registration Number : ")
    if registration_number not in student_list:
        print("Student is not registered!!")
        return
    student = student_list[registration_number]
    if student.get("Marks"):
        print("Marks Already Added")
        return
        
    course = student.get("Course")
    if  course == "Computer Science and Engineering(CSE)":
        course_shorthand = "CSE"
    elif course == "Mechanical Engineering(ME)":
        course_shorthand ="ME"
    elif course == "Chemical Engineering(CE)":
        course_shorthand = "CE"
    elif course == "Electrical and Electronics Engineering(ECE)":
        course_shorthand = "ECE"
    elif course == "Aerospace Engineering(AE)":
        course_shorthand = "AE"
    
    English = float(input("Enter the English Marks : "))
    EVS = float(input("Enter the EVS Marks : "))
    Maths = float(input("Enter the Maths Marks : "))
    course_marks = float(input("Enter the Course Subject Marks : "))
    student["Marks"] = {"English" : English, "EVS" : EVS, "Maths" : Maths, course_shorthand : course_marks} 
    print("Marks Successfully Added!!")
    return student_list





