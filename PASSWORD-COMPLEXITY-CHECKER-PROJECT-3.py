import string

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)

    # Assess overall strength
    if (length_criteria and uppercase_criteria and lowercase_criteria
        and digit_criteria and special_char_criteria):
        return "Strong"
    elif (length_criteria and uppercase_criteria and lowercase_criteria
          and digit_criteria):
        return "Moderate"
    elif (length_criteria and uppercase_criteria and lowercase_criteria):
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    # Example passwords to test
    passwords = [
        "Password123!",
        "pass123!",
        "Password",
        "12345678",
        "!@#$%^&*",
        "Abcd1234"
    ]

    # Assess strength of each password and provide feedback
    for password in passwords:
        strength = assess_password_strength(password)
        print(f"Password: {password} \t Strength: {strength}")
