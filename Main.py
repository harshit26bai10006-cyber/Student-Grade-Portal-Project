import Records

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
    a = {}
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



             