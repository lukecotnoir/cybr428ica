
def check_password_easy(password):
    import re 

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
            
    return True


def check_password_hard(password):
    import re 

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

    digits_sum = sum(int(char) for char in password if char.isdigit())
    if digits_sum % 2 != 0:
        return "Sum of digits in the password must be even."

    vowels = re.findall(r'[aeiouAEIOU]', password)
    if len(vowels) != 3:
        return "Password must contain exactly 3 vowels."
    
    found_palindrome = False
    for i in range(len(password)):
        for j in range(i + 3, len(password) + 1):
            substr = password[i:j]
            if substr == substr[::-1]:
                found_palindrome = True
                break
        if found_palindrome:
            break
    if not found_palindrome:
        return "Password must include a palindrome of at least 3 characters."
    
    repeated_twice = any(password.count(c) == 2 for c in set(password))
    if not repeated_twice:
        return "Password must have at least one character that repeats exactly twice. (e.g., aa but not aaa)"
    
    if not (password[0].isupper() and password[-1].isdigit()):
        return "Password must start with a capital letter and end with a digit."
    
    for i in range(len(password) - 2):
        if password[i].isalpha() and password[i+1].isalpha() and password[i+2].isalpha():
            a, b, c = ord(password[i]), ord(password[i+1]), ord(password[i+2])
            if b == a + 1 and c == b + 1:
                return "Password cannot contain 3+ consecutive letters in alphabetical order. (e.g., abc is not allowed)"
            
    return True


def check_password_evil(password):
    import re 

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

    digits_sum = sum(int(char) for char in password if char.isdigit())
    if digits_sum % 2 != 0:
        return "Sum of digits in the password must be even."

    vowels = re.findall(r'[aeiouAEIOU]', password)
    if len(vowels) != 3:
        return "Password must contain exactly 3 vowels."
    
    found_palindrome = False
    for i in range(len(password)):
        for j in range(i + 3, len(password) + 1):
            substr = password[i:j]
            if substr == substr[::-1]:
                found_palindrome = True
                break
        if found_palindrome:
            break
    if not found_palindrome:
        return "Password must include a palindrome of at least 3 characters."
    
    repeated_twice = any(password.count(c) == 2 for c in set(password))
    if not repeated_twice:
        return "Password must have at least one character that repeats exactly twice. (e.g., aa but not aaa)"
    
    if not (password[0].isupper() and password[-1].isdigit()):
        return "Password must start with a capital letter and end with a digit."
    
    for i in range(len(password) - 2):
        if password[i].isalpha() and password[i+1].isalpha() and password[i+2].isalpha():
            a, b, c = ord(password[i]), ord(password[i+1]), ord(password[i+2])
            if b == a + 1 and c == b + 1:
                return "Password cannot contain 3+ consecutive letters in alphabetical order. (e.g., abc is not allowed)"

    greek_gods = [
        'zeus', 'hera', 'poseidon', 'demeter', 'ares', 'athena',
        'apollo', 'artemis', 'hephaestus', 'aphrodite', 'hermes', 'hades', 'dionysus'
    ]
    lower_pass = password.lower()
    if not any(god in lower_pass for god in greek_gods):
        return "Password must include the name of a Greek god."

    # ASCII sum must be prime
    ascii_sum = sum(ord(c) for c in password)
    def is_prime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True

    if not is_prime(ascii_sum):
        return f"The sum of ASCII values ({ascii_sum}) must be a prime number."    
            
    return True


# if __name__ == "__main__":
#     print("Welcome to the password checker!")
#     print("Based on your new knowledge of password best practices, try and create a password that meets the criteria!")
#     print("\n")
#     while True:
#         password = input("Enter your password: ")
#         if not check_password(password):
#             print("Bad password, please try again.")
#             print("\n")
#         else:
#             print("Password is valid, congrats!")
#             break
    
