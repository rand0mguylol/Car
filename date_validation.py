import datetime

def date_validation(text, display_time = False):
  
  while True:
    try:
      user_input = input(f"{text}")
      
      if user_input == "":
        return 
        
      if display_time == False:
        user_date = datetime.datetime.strptime(user_input, "%Y/%m/%d").date()
      else: 
         user_date = datetime.datetime.strptime(user_input, "%Y/%m/%d %H:%M:%S")
      return user_date
    except:
      print("Please enter a valid date\n")
      continue



