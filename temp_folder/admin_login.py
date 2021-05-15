
from login_validation import login_validation


def admin_login():
  id = input("Please enter ID: ").strip()
  email = input("Please enter email: ").strip()
  password = input("Please enter password: ").strip()

  is_login = login_validation("admin.txt", id, email, password)

  if is_login == True:
    admin_main_2()
  elif is_login == False:
    print("Enter 0 to retry. Enter 1 to exit")
    user_option = ""
    while not user_option.isdigit() or not 0 <= int(user_option) <= 1:
      user_option = input("Please choose an option: ")
      while not user_option.isdigit() or not 0 <= int(user_option) <= 1:
        print("Please enter a valid option\n")
        print("Enter 0 to retry. Enter 1 to exit")
        user_option = ""
        
  
    user_option = int(user_option)
    if user_option == 0:
      login_admin()
    else:
      exit()

