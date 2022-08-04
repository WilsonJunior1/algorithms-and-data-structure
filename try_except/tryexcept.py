while True:
  try:
    number_1 = int(input("Enter a number:"))
  except:
    print("Please, enter a valid value.")
  else:
    print(f"The number is {number_1}")
    break