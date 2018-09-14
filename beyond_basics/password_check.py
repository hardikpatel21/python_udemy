correct_password = "python123"
name = input("Enter Name: ")
surname = input("Enter Surname")
password = input("Enter password: ")


while password != correct_password:
    password = input("Wrong Password! Enter again: ")

message="Hi %s %s, you are logged in to mapping" % (name,surname)

print(message)
