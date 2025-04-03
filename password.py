
def check_password(password):
    special_characters = "!@#$%^&*()-+"

    if password == "":
        return "Password cannot be empty."
    
    try:
        with open("common_pass.txt", 'r') as file:
            for line in file:
                if password == line.strip():
                    return False
    except FileNotFoundError:
        return "Error: Common password file not found." 

    if len(password) < 16:
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char in special_characters for char in password):
        return False 
            
    return True


if __name__ == "__main__":
    print("Welcome to the password checker!")
    print("Based on your new knowledge of password best practices, try and create a password that meets the criteria!")
    print("\n")
    while True:
        password = input("Enter your password: ")
        if not check_password(password):
            print("Bad password, please try again.")
            print("\n")
        else:
            print("Password is valid, congrats!")
            break
    
