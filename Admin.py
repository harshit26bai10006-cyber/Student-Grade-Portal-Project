def Dashboard(student_list):
    admin = "Harshit"
    password = "Harshit123"


    for i in range(3):
        admin_enter = input("Enter the Admin Username : ")
        pass_enter = input("Enter the Admin Password : ")
        login_check = False
        if admin_enter == admin and pass_enter == password:
            print("Successfully Logged in!")
            login_check = True
            break
        else:
            print("Login Attempt Failed! You have",2-i,"attempts left!!")

    if not login_check:
        print("Maximum attempts reached Returning to previous page.!")
        return student_list

    while True:
        choice = int(input("1 : View Global Database Statistics\n2 : Emergency Database Deletion\n0 : Exit\n Enter : "))
        if choice == 1:
            total_students = len(student_list)
            print("[SYSTEM LOG] : Total Registered Students : ",total_students)
            grade_count = 0
            for reg, data in student_list.items():
                if "CGPA" in data:
                    grade_count += 1
            print("[SYSTEM LOG] : Total Graded Students : ",grade_count)
        elif choice == 2:
            confirmation = int(input("Are You sure want to delete the Registered Students Database?\n1 : Yes\n2 : NO\nEnter : "))
            if confirmation == 1:
                student_list.clear()
                print("[SYSTEM LOG] Student Database has been completely Wiped Out!!")
            else : 
                print("Operation Cancelled!!")

        elif choice == 0:
            print("Returning to main page")
            return student_list
        else :
            print("Invalid Option Choice!!")
    return student_list