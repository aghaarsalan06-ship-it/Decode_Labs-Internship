password = input("Enter your password: ")
has_number = False
has_upper = False
has_lower = False
has_special = False
score = 0
tips = []
for character in password:
    if character.isdigit():
        has_number = True
    elif character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif not character.isalnum():
        has_special = True
if len(password) >= 8:
    score += 1
else:
    tips.append("make it at least 8 characters long")
if has_number:
    score += 1
else:
    tips.append("add a number")
if has_upper:
    score += 1
else:
    tips.append("add an uppercase letter")
if has_lower:
    score += 1
else:
    tips.append("add a lowercase letter")
if has_special:
    score += 1
else:
    tips.append("add a special character")
if score == 5:
    print("Password is STRONG")
elif score >= 3:
    print("Password is MEDIUM")
else:
    print("Password is WEAK")
if tips:
    print("Suggestions:", ", ".join(tips))