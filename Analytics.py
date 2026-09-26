def Graph_Generator(student_list):
    registration_number = input("Enter your Registration Number")
    if registration_number not in student_list:
        print("Specified student not Registered")
        return student_list
    student = student_list[registration_number]
    if not student.get("Marks"):
        print("Specified Student's marks not added!!")
        return student_list
    marks = student["Marks"]
    for a,b in marks.items():
        print(a.ljust(12),"|","* "*int(b//10),int(b))
    print("".ljust(12),"|_____________________________")
    return student_list

def Leaderboard(student_list,choice):
    if not student_list:
        print("There are not any Registered Students!")
        return student_list
    Leaderboard = []
    if choice == 3:
        choice1 = int(input("\n1 : English Marks Leaderboard\n2 : EVS Marks Leaderboard\n3 : Maths Marks Leaderboard\n4 : Course Subject Marks Leaderboard\n0 : Exit\nEnter : "))
        if choice1 == 0:
            return student_list
    for reg_no, Data in student_list.items():
        if choice ==1:
            for a,b in Data.items():
                if a == "CGPA":
                    ranking_manner = "CGPA"
                    Leaderboard.append([b,reg_no])
        if choice == 2:
            for a,b in Data.items():
                if a == "Percentage":
                    ranking_manner = "Percentage"
                    Leaderboard.append([b,reg_no]) 
        if choice == 3:
            if "Marks" in Data and Data["Marks"]:
                marks_dict = Data["Marks"]
                if choice1 == 1:
                    ranking_manner = "English"
                    if "English" in marks_dict:
                        Leaderboard.append([marks_dict["English"], reg_no]) 
                elif choice1 == 2:
                    ranking_manner = "EVS"
                    if "EVS" in marks_dict:
                        Leaderboard.append([marks_dict["EVS"], reg_no])
                elif choice1 == 3:
                    ranking_manner = "Maths"
                    if "Maths" in marks_dict:
                        Leaderboard.append([marks_dict["Maths"], reg_no]) 
                elif choice1 == 4:
                    for subject, score in marks_dict.items():
                        if subject not in ["English", "EVS", "Maths"]:
                            ranking_manner = subject
                            Leaderboard.append([score, reg_no])
    if len(Leaderboard) == 0:
        print("No CGPA data available yet!")
        return student_list

    Leaderboard.sort(reverse=True)
    print("*----------------LEADERBOARD---------------*")
    rank = 1
    for item in Leaderboard:
        score = item[0]
        reg = item[1]

        student = student_list[reg]
        name = student["First Name"] + " " + student["Last Name"]
        print(rank,"-->",name, "| Reg No.: ",reg, "|",ranking_manner,": ",score)
        rank +=1
    print("*------------------------------------------*")
    return student_list


