import re

def check_password_strength(password):
    strength_score = 0
    feedback = []
  
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
        
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")
  
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")
   
    if strength_score == 5:
        feedback.append("Password is Strong!")
    elif strength_score >= 3:
        feedback.append("Password is Moderate.")
    else:
        feedback.append("Password is Weak.")
   
    print("\n".join(feedback))
user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)
