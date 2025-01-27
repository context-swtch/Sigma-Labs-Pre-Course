def print_hr_data_readably(person_data):
    # Print the selected entries data readably on screen
    print(
        f"Name: {person_data['first_name']} {person_data['last_name']}\n\nAge: {person_data['age']} \n\nEmployed: {person_data['employed']}\n\n")


def prompt_user_for_hr_action(people_list):
    # Options menu for the program user to manipulate the list of people and view it
    while True:
        user_choice = input(
            "What action would you like to do? Choose 'Add', 'Remove', 'View' or 'Quit': ").rstrip().lower()
        if 'add' in user_choice:
            add_user_to_hr_list(people_list, collect_user_data())
            view_persons_data(people_list)
        elif 'remove' in user_choice:
            remove_user_data(people_list)
            view_persons_data(people_list)
        elif 'view' in user_choice:
            view_persons_data(people_list)
        elif 'quit' in user_choice:
            return False
        else:
            print("I'm not sure what you meant.")


def initialise_hr_dictionaries():
    # Initialise the list of dictionaries with the supplied HR data
    return [{'first_name': 'Jane', 'last_name': 'Doe', 'age': 42, 'employed': True},
            {'first_name': 'Tom', 'last_name': 'Smith', 'age': 18, 'employed': True},
            {'first_name': 'Mariam', 'last_name': 'Coulter', 'age': 66, 'employed': False},
            {'first_name': 'Gregory', 'last_name': 'Tims', 'age': 8, 'employed': False}]


def collect_user_data():
    # Collect new user data via prompts and create a new entry in the list
    return create_hr_entry(
        first_name=input("Please enter the user's first name: "),
        last_name=input("Please enter the user's last name: "),
        age=input("Please enter the user's age: "),
        employment_status=parse_employment_status(
            input("Is the user employed? Type 'Yes' or 'No': ").lower())
    )


def parse_employment_status(status):
    # Parse employment status from user input
    return True if 'yes' in status else False


def add_user_to_hr_list(people_list, user):
    # Add a new user to the list
    people_list.append(user)
    print(f"User added.")


def create_hr_entry(first_name, last_name, age, employment_status):
    # Create a dictionary containing user data
    return {'first_name': first_name, 'last_name': last_name, 'age': age, 'employed': employment_status}


def remove_user_data(people_list):
    # Remove a user from the list
    selected_user_name = input("Enter the name of the user to remove: ").rstrip().lower()
    words = selected_user_name.split(' ')

    for person in people_list:
        if person.get('first_name').lower() in words or person.get('last_name').lower() in words:
            people_list.remove(person)
            print(f"User {person['first_name']} {person['last_name']} has been removed.")
            return

    print("No matching user found.")


def view_persons_data(people_list):
    # View all users in the list
    if not people_list:
        print("No users found.")
    for person in people_list:
        print_hr_data_readably(person)


def main():
    # Program entry point
    people_list = initialise_hr_dictionaries()
    while True:
        if not prompt_user_for_hr_action(people_list):
            break


if __name__ == "__main__":
    main()
