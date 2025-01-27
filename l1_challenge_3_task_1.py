def input_validation_check_for_int(to_check):
  try:
    i = int(to_check)
  except ValueError:
     print("You did not enter a valid number.")
     return None
  else:
    return i

def ask_user_for_a_number():
  while True:
    ans = input("Please enter a number: ")
    x = input_validation_check_for_int(ans)
    if x:
      return x

def ask_user_sum_or_product():
  while True:
    selection = input("Type '1' to calculate the sum to your number, or '2' to calculate the product: ")
    x = input_validation_check_for_int(selection)
    if x in [1,2]:
      return x
    else:
      print("Please enter 1 or 2.")

def sum_nums_to_n(n):
  x = 0
  for i in range(1, n+1):
    x += i

  return x

def sum_multiples_of_three_or_five(n):
  x = 0
  for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
      x += i

  return x

def product_nums_to_n(n):
  x = 1
  for i in range(1, n+1):
    x *= i

  return x
  

def main():
  x = ask_user_for_a_number()
  y = ask_user_sum_or_product()
  ans = 0
  if y == 1:
      ans = sum_multiples_of_three_or_five(x)  
    # ans = sum_nums_to_n(x) for all numbers.
  elif y == 2:
      ans = product_nums_to_n(x)

  print(f"Result: {ans}")

if __name__ == "__main__":
  main()