student = {}

while True:
    print("\n------STUDENT MANAGER APP----- ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4.Exit")
    
    choice = input("Enter your choice: ")
    
    #Add Students
    if choice == "1":
        name = input("Enter Your Name: ")
        marks = int(input("Enter Marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")
        
        
    #View Students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name ,marks in student.items():
                print(name,":",marks)
                
                
    #Check Result
    elif choice == 3:
        name = input("Enter Student Name: ")
        if name in student:
            marks = student[name]
            
            if marks >= 40:
                print("PASS")
            
            else:
                print("FAIL")
                
        else:
            print("Student not found!")
            
        #EXIT
    elif choice == 4:
        print("---Exiting---")
        break
    
    
    else:
        print("Invalid Input!")