user_name = input("Enter your name: ").capitalize()
user_gender = input("Enter your gender (M/F): ").upper()
user_age = int(input("Enter your age: "))

if user_age >= 18 and user_age < 25 and user_gender == "M" or user_age < 31 and user_gender == "F":
    print(f"{user_name}, you are qualified to join the Customer Care Department.")
elif user_age >= 25 and user_age < 45 and user_gender == "M":
    print(f"{user_name}, you are qualified to join the Engineering Department.")
elif user_gender == "F" and user_age <= 50:
    print(f"{user_name}, you're qualified to join the Admin Department.")
elif user_gender == "M" and user_age >= 45:
    print(f"{user_name}, you're qualified to join the Security Department.")
else:
    print(f"Sorry, {user_name}, you're not eligible. ")