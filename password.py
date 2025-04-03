
def check_password(password):
    special_characters = "!@#$%^&*()-+"

    if password == "":
        return "Password cannot be empty."
    
    try:
        with open("common_pass.txt", 'r') as file:
            for line in file:
                if password == line.strip():
                    return "Password is too common."
    except FileNotFoundError:
        return "Error: Common password file not found." 

    if len(password) < 16:
        return "Password must be at least 16 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."  
            
    return None


if __name__ == "__main__":
    
    while True:
        password = input("Enter your password: ")
        problem = check_password(password)
        if problem:
            print(problem)
            print("\n")
        else:
            print("Password is valid, congrats!")
            break
    
