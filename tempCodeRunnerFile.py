import random
import string

passwords = {}


#load existing pswd file
try:
    with open("passwords.txt","r") as file:
        for line in file:
            website,pswd = line.strip().split(":")
            passwords[website] = pswd
            
except FileNotFoundError:
    print("No saved passwords yet.")
     

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#%^&*^"
    password = "".join(random.choice(chars) for _ in range(8))
    return password


while True:
    print("\n ---Personal Password Manager---")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")
    
    choice = input("Enter Your Choice: ")
    
    if choice == "1":
        site = input("Enter Website: ")
        pswd = input("Enter Password: ")
        
        passwords[site] = pswd
        
        with open("passwords.txt","a") as file:
            file.write(f"{site}:{pswd}\n")
            
            
        print("Saved")
        
        
    elif choice == "2":
        if not passwords:
            print("No Data!")
            
        else:
            for site,pswd in passwords.items():
                print(site ,":",pswd)
                
    
    elif choice == "3":
        print("Generated Password",generate_password())
        
    elif choice == "4":
        print("Ok Byeeee!")
        break
        
        
    else:
         print("Invalid Input!")