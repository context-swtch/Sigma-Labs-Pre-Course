from datetime import datetime


def run_age_calculator():
    dob = get_user_date_of_birth()
    today = datetime.now()

    # Calculate the age
    age = today.year - dob.year

    # Check if the birthday has occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print(f"Your age is {age}.")


def get_user_date_of_birth():
    while True:
        user_input = input("Please enter your date of birth in the format of DD-MM-YYYY: ")

        # Split the input by "-"
        parts = user_input.split("-")

        # Check if there are 3 parts (DD, MM, YYYY)
        if len(parts) != 3:
            print("Invalid format. Please use DD-MM-YYYY.")
            continue

        day, month, year = parts

        # Check if parts are of correct length and digits
        if not (day.isdigit() and len(day) == 2 and
                month.isdigit() and len(month) == 2 and
                year.isdigit() and len(year) == 4):
            print("Invalid format. Please make sure DD, MM, and YYYY are numeric and in the correct lengths.")
            continue

        try:
            # Verify the date is valid
            return datetime.strptime(user_input, "%d-%m-%Y")
        except ValueError:
            print("The date you entered does not exist. Please try again.")


if __name__ == "__main__":
    run_age_calculator()
