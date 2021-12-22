for a in range (0,3):
    username = (input("enter username:"))
    password = (input("enter password:"))
    if username == str("facebook"):
        if int (password) == 9800000000:
            print("logged in succeccfully.")
            break
        else:
            print("invalid credentials")