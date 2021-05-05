import datetime
# with open("test.txt", "a") as rf:
#   rf.write("test")
  


# print(len(lines))


# user = input("Enter: ")

# while not "1" <= user <= "4":
#   print("Please enter valid option")
#   user = input("Enter: ")


# print(user)


test = "2020/5/3"

a = datetime.datetime.strptime(test, "%Y/%m/%d").date()

print(a)