# Collect user input for categorizing and allocating departments to them
user_name = input("Enter your name: ").capitalize()
user_gender = input("Enter your gender (M/F): ").upper()
user_age = int(input("Enter your age: "))

# Department lists under Okoro and Sons where users would be placed into
CustomerCare = []
Engineering = [],
Admin = [],
Security = []

# This block of conditional statement checks for user qualifications
# Then matches an append them to the departments they belong to
if user_age >= 18 and user_age < 25 and user_gender == "M" or user_age < 31 and user_gender == "F":
    CustomerCare.append(user_name)
    print(f"{user_name}, you are qualified to join the Customer Care Department.")

elif user_age >= 25 and user_age < 45 and user_gender == "M":
    Engineering.append(user_name) 
    print(f"{user_name}, you are qualified to join the Engineering Department.")


elif user_gender == "F" and user_age <= 50:
    Admin.append(user_name)
    print(f"{user_name}, you're qualified to join the Admin Department.")

elif user_gender == "M" and user_age >= 45:
    Security.append(user_name)
    print(f"{user_name}, you're qualified to join the Security Department.")

# This prints the ineligibility output
else:
    print(f"Sorry, {user_name}, you're not eligible.")
    