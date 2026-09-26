import Records
import Grading
import Analytics
a = {}
while True:
    print("*-------Welcome to Student Portal-------*")
    print("|                                       |")
    print("| 1: Registration Center                |")
    print("| 2: Marks Updation                     |")
    print("| 3: Analytical Grades                  |")
    print("| 4: Admin Login                        |")
    print("| 0: Exit                               |")
    print("*---------------------------------------*")
    option = int(input("Enter: "))
    
    if option == 1:
        while True:
            print("Select and Enter the numbers shown: ")
            option1 = int(input("1 : Register Student\n2 : Update Student Details\n3 : Get Student Information\n4 : Remove Student Details\n0 : Go Back\nEnter : "))
            if option1 == 1:
                b= Records.Register_Student(a)
                a = b[0]
                print("Registration number =", b[1])

            elif option1 == 2:
                a = Records.Update_Student(a)


            elif option1 == 3:
                a = Records.Print_Student_Details(a)


            elif option1 == 4:
                a = Records.Remove_Student(a)

            elif option1 == 0:
                break

    elif option == 2:
        while True:
            print("Welcome to Student Grading Portal!")
            option2 = int(input("1 : Add Marks\n2 : View Marks\n3 : Calculate Percentage and CGPA\n4 : Update Marks\n5 : Remove Marks\n0 : Go Back\nEnter : "))
            if option2 == 1:
                a = Grading.add_marks(a)
            elif option2 == 2:
                a = Grading.view_marks(a)
            elif option2 == 3:
                a = Grading.calculate_grades(a)
            elif option2 == 4:
                a = Grading.update_marks(a)
            elif option2 == 5:
                a = Grading.remove_marks(a)
            elif option2 == 0:
                break
            
    elif option == 3:
        while True:
            print("Welcome to Student Analatycal Grades")
            option3 = int(input("1 : View Histogram of your Marks\n2 : View Leaderboard Based upon particular items\n0 : Exit\nEnter : "))
            if option3 == 1:
                a =  Analytics.Graph_Generator(a)
            elif option3 == 2:
                choice = int(input("1 : Based on CGPA\n2 : Based on Percentage\n3 : Based on Particular Subject Marks\n0 : Exit\n Enter : "))
                a =  Analytics.leaderboard(a,choice)

    elif option == 0:
        break
    



             