import random
from itertools import zip_longest

def reverse_name(name):
  return name[::-1]

def intersperse_name(second_name, reversed_first_name):
  second_name_list = list(second_name)
  reversed_first_name_list = list(reversed_first_name)
  ans = list(sum(zip_longest(reversed_first_name_list,second_name_list, fillvalue=''),()))
  return ''.join(ans)

def capitalise_word(name):
  if not name:
    return name
  return name[:1].upper() + name[1:].lower()

def interpersed_username_based_on_name():
  first_name = input("Please input your first name: ")
  reversed_name = reverse_name(first_name)

  second_name = input("Please input your second name: ")
  interspersed_name = intersperse_name(second_name, reversed_name)

  return interspersed_name

def split_name_in_half(name):
  mid_index = len(name)//2
  first_half = capitalise_word(name[:mid_index])
  second_half = capitalise_word(name[mid_index:])

  return first_half, second_half

def generate_random_username():
  return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))

def prompt_for_choice():
  while True:
    print("Please choose one of the following options: ")
    print("1. Create a username based on a name.")
    print("2. Generate a random username.")
    user_choice = input("Enter 1 or 2: ").strip()
    if user_choice == '1':
      return 1
    elif user_choice == '2':
      return 2
    else:
      print("Invalid option. Please try again.")
  
# Entry Point ----------
print("Welcome to the username creator.")
chosen_option = prompt_for_choice()

if chosen_option == 1:
  name = interpersed_username_based_on_name()
elif chosen_option == 2:
  name = generate_random_username()
  
first_name, second_name = split_name_in_half(name)
print(f"Generated Username: {first_name} {second_name}")

