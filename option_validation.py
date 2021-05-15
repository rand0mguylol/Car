text = "Please choose a filter option\n1.Days\n2.Hours"

def option_validation(min_option, max_option, text = None):
  
  if text != None:
    print(text)

  option = input("Please choose an option by entering a number: ")
  print("")

  if option == "":
    return
  
  while not option.isdigit() or not min_option <= int(option) <= max_option :
    print("Please enter a valid option\n")
    if text != None:
      print(text)
    option = input("Please choose an option by entering a number: ")
    print("")
    

  return int(option)


# a = option_validation(text, 1, 2)
# print(a)