import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria])
    
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")
    
    return strength, feedback

def main():
    password = input("Enter a password to assess its strength: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    for tip in feedback:
        print(f"- {tip}")

if __name__ == "__main__":
    main()
