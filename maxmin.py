def get_number_list_from_user():
    while True:
        # Prompt the user for input and strip leading/trailing whitespace
        user_input = input("Enter a list of numbers separated by commas (e.g., 1, 2, 3): ").strip()

        # Check if the input is empty
        if not user_input:
            print("You didn't enter anything. Please try again.")
            continue

        # Split the input by commas and strip whitespace from each part
        parts = [part.strip() for part in user_input.split(",")]

        valid_numbers = []

        # Validate each part of the input
        for part in parts:
            # Check if the part is a valid number (including negative numbers and integers)
            if part.lstrip('-').replace(".", "", 1).isdigit():
                # Convert the valid part to an integer and add it to the list
                valid_numbers.append(int(part))
            else:
                # Skip invalid parts (non-numeric input)
                continue

        # Return the list of valid numbers
        return valid_numbers


def max_min_without_lib_functions(number_list):
    # Initialize max and min with the first element of the list
    maximum_num = number_list[0]
    minimum_num = number_list[0]

    # Iterate through the list to find the max and min values
    for num in number_list:
        if num > maximum_num:
            maximum_num = num  # Update max if current number is greater
        elif num < minimum_num:
            minimum_num = num  # Update min if current number is smaller

    # Return the max and min values as a tuple
    return maximum_num, minimum_num


if __name__ == "__main__":
    # Get a list of numbers from the user
    numbers = get_number_list_from_user()

    # Find the largest and smallest numbers in the list
    max_num, min_num = max_min_without_lib_functions(numbers)

    # Print the results
    print(f"The largest number in the array is {max_num} and the smallest number is {min_num}.")