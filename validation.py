def postcode_validation():
    
    while True:
        postcode = input("Enter postcode:")
        if postcode.isdigit() and len(postcode) == 5:
            return
        else:
            print("Please enter valid postcode.")

# postcode_validation()


# def email_validation():

#     import re 
#     # import regular expression package
#     validemail = "[a-zA-Z0-9+-._]+@[a-zA-Z]+.(com|edu|net)"
#     # [match character, digit and symbol]@[matching characters].(matching character)

#     while True:
#         email = input("Enter Email:")
#         if re.search(validemail, email):
#             return
#         else:
#             print(("Please enter valid email"))      

# email_validation()


# def password_validation():
    
#     specialcharacter = ["!","#","$","^","&","*","()","=","[]","{}",":","|","<>",",","?","/","@","."]

#     while True:
#         password = str(input("Enter password: "))
#         if len(password)<8:
#             print("Must contain at least 8 characters!")
#         elif len(password)>16:
#             print("Maximum 16 characters!")
#         elif not any(character.isupper() for character in password):
#             print("Must contain at least one uppercase letter!")
#         elif not any(character.islower() for character in password):
#             print("Must contain at least one lowercase letter!")
#         elif not any(character.isdigit() for character in password):
#             print("Must contain at least one digit!")
#         elif not any(character in specialcharacter for character in password):
#             print("Must contain at least one special character!")
#         else:
#             return
# password_validation()