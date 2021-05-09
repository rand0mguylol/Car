import datetime
from pretty_table import pretty_table
from format_file_list import format_file_list


# def payment_period():
# a = "2020/03/08 10:00:00"
# b = "2020/03/08 14:00:00"

# a_string = datetime.datetime.strptime(a, "%Y/%m/%d %H:%M:%S")
# print(a_string)
# b_string = datetime.datetime.strptime(b, "%Y/%m/%d %H:%M:%S")
# print(b_string)

# c = b_string - a_string
# print(c)

# if int(c.total_seconds()/3600) >= 24:
#   print(f"{c.days} days")
# else:
#   print(f"{int(c.seconds/3600)} hours")


# test_list = format_file_list("rentedcar2.txt")

def payment_period(rented_car_list):

    start_point = 1

    while start_point < len(rented_car_list):
      for col in range(len(rented_car_list[start_point])):
        pick_date = rented_car_list[start_point][5]
        drop_date = rented_car_list[start_point][6]
        pick_date_string = datetime.datetime.strptime(pick_date, "%Y/%m/%d %H:%M:%S")
        drop_date_string = datetime.datetime.strptime(drop_date, "%Y/%m/%d %H:%M:%S")
        payment_status = drop_date_string - pick_date_string
        
        return payment_status
        # if int(payment_status.total_seconds()/3600) >= 24:
        #   print(f"{payment_status.days} days")
        #   rented_car_list[start_point].append(f"{payment_status.days} DAYS")
        #   break
        # else:
        #   print(f"{int(payment_status.seconds/3600)} hours")
        #   rented_car_list[start_point].append(f"{int(payment_status.seconds/3600)} HOURS")
        #   break
      
      start_point += 1
      


  print(file_list)


