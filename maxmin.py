def get_number_list_from_user():
    while True:
        user_input = input("Enter a list of numbers separated by commas (e.g., 1, 2, 3): ").strip()

        if not user_input:
            print("You didn't enter anything. Please try again.")
            continue

        parts = [part.strip() for part in user_input.split(",")]

        valid_numbers = []

        for part in parts:
            if part.lstrip('-').replace(".", "", 1).isdigit():
                valid_numbers.append(int(part))
            else:
                continue


        return valid_numbers


def max_min_without_lib_functions(number_list):
    maximum_num = number_list[0]
    minimum_num = number_list[0]

    for num in number_list:
        if num > maximum_num:
            maximum_num = num
        elif num < minimum_num:
            minimum_num = num

    return maximum_num, minimum_num


if __name__ == "__main__":
    numbers = get_number_list_from_user()
    max_num, min_num = max_min_without_lib_functions(numbers)
    print(f"The largest number in the array is {max_num} and the smallest number is {min_num}.")
