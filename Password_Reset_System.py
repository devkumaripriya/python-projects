users={}

def register():
    username=input("Enter username: ")
    if username in users:
        print("Username already exists!")
    else:
        password=input("Enter Password: ")
        users[username]=password
        print("Registration Successful!")
def login():
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    if username in users and users[username]==password:
        print("Login Successful!")
        
    else:
        print("Invalid Credentials!")

def reset_password():
    username=input("Enter Username")
    if username in users:
        old_password=input("Enter old password: ")
        
        if users[username]==old_password:
            new_password=input("Enter new password")
            users[username]=new_password
            print("Password Reset Successfully!")
        else:
            print("Incorrect Old Password !")
    else:
        print("Username not Found !")
def main():
    while True:
        print("\n1.Register")
        print("2.Login")
        print("3.Reset Password")
        print("4.Exit")
        
        choice=input("Enter choice:")
        
        if choice== "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            print("Existing...")
            break
        else:
            print("Invalid Choice !")
        
main()