bad_pass = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while (True):
    passwd = str(input("Enter your pass: "))
    num = len(passwd)
    if passwd in bad_pass:
        print("Password to common! \nTry Again!")
        continue
    else:
        if num > 8 and num <= 12:
            print("password verified")   
            break
        else:
            print("password must be between 8 and 12 characters! \nTry Again!")
            continue