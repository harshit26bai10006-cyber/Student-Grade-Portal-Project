def add_marks(student_list):
    common_subjects = {"English": 0,
                       "EVS" : 0,
                       "Maths" : 0
                       }
    registration_number = input("Enter your Registration Number : ")
    if registration_number not in student_list:
        print("Student is not registered!!")
        return student_list
    student = student_list[registration_number]
    if student.get("Marks"):
        print("Marks Already Added")
        return student_list
        
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
    if (English > 100 or English < 0 or EVS > 100 or EVS < 0 or Maths > 100 or Maths < 0 or course_marks > 100 or course_marks < 0):
        print("You have entered Invalid Marks!!")
        return student_list 
    student["Marks"] = {"English" : English, "EVS" : EVS, "Maths" : Maths, course_shorthand : course_marks} 
    print("Marks Successfully Added!!")
    return student_list

def view_marks(student_list):
    registration_number = input("Enter your Registration Number : ")
    if registration_number not in student_list:
        print("Specified Student is not Registered!!")
        return student_list
    student = student_list[registration_number]
    if not student.get("Marks"):
        print("Marks Not added of specified Student")
        return student_list
    marks = student["Marks"]
    for a, b in marks.items():
        print(a,":",b)
    return student_list

def calculate_grades(student_list):
    registration_number = input("Enter your Registration Number : ")
    if registration_number not in student_list:
        print("Specified Student is not Registered!!")
        return student_list
    student = student_list[registration_number]
    if not student.get("Marks"):
        print("Marks Not added of specified Student")
        return student_list
    print("*--------------Subject Report-------------*")
    marks = student["Marks"]
    total = 0
    total_grade_points = 0
    temp = {}
    for a, b in marks.items():
        total += b
    
        if b>=90 and b<=100:
            grade = "S"
            grade_point = 10
        elif b>=80 and b<90:
            grade = "A"
            grade_point = 9
        elif b>=70 and b<80:
            grade = "B"
            grade_point = 8
        elif b>=60 and b<70:
            grade = "C"
            grade_point = 7
        elif b>=50 and b<60:
            grade = "D"
            grade_point = 6
        elif b>=40 and b<50:
            grade = "E"
            grade_point = 5
        elif b<40:
            grade = "Fail"
            grade_point = 0
        total_grade_points +=grade_point
        temp[a] = grade
        print(a,":",grade)
    student["Grades"] = temp
    print("*-----------------------------------------*")
    percentage = total/4
    cgpa = total_grade_points/4
    print("Percentage = ", percentage)
    print("CGPA", cgpa)
    student["Percentage"] = percentage
    student["CGPA"] = cgpa
    if percentage<33:
        print("Fail In the Course!")
        student["Status"] = "Fail"
    else:
        print("Pass")
        student["Status"] = "Pass"
    return student_list

def update_marks(student_list):
    registration_number = input("Enter your Registration Number : ")
    if registration_number not in student_list:
        print("Specified Student is not Registered!")
        return student_list
    student = student_list[registration_number]
    if not student.get("Marks"):
        print("Specified Student's marks not added!!")
        return student_list
    marks = student["Marks"]
    for a,b in list(marks.items()):
        mark = input(f"{a} (Current: {b}): ")
        if mark.strip() != "":
            new_val = float(mark)
            if new_val > 100 or new_val < 0:
                print("Invalid range! Keeping previous mark.")
            else:
                marks[a] = new_val
    return student_list

def remove_marks(student_list):
    registration_number = input("Enter your Registration Number : ")
    if registration_number not in student_list:
        print("Specified Student is not Registered!")
        return student_list
    student = student_list[registration_number]
    if not student.get("Marks"):
        print("Specified Student's marks not added!!")
        return student_list
    confirm = int(input("Are you sure want to remove the marks of the particular student?\n1 : Yes\n2 : No\nEnter : "))
    if confirm == 1:
        student.pop("Marks", None)
        student.pop("Grades", None)
        student.pop("Percentage", None)
        student.pop("CGPA", None)
        student.pop("Status", None)
        print("Student marks successfully removed!")
    if confirm == 2:
        print("Operation Cancelled. returning to previous page..")
        return
    return student_list

