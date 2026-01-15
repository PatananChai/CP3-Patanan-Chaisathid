username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Admin" and password == "1234":
    print("----------------")
    print("Welcome Shopping Online Catalogue")
    print("Please select items from the list")
    print("1. Apple  50 THB")
    print("2. Mango  30 THB")
    print("3. Banana 20 THB")
    print("----------------")
    apple = input("DO you want Apple? (Y/N)")
    mango = input("DO you want Mango? (Y/N)")
    banana = input("DO you want Banana? (Y/N)")

    if apple == "Y":
        appleNumber = int(input("How many apple do you want?"))
    else :
        appleNumber = 0

    if mango == "Y":
        mangoNumber = int(input("How many mango do you want?"))
    else :
        mangoNumber = 0

    if banana == "Y":
        bananaNumber = int(input("How many banana do you want?"))
    else :
        bananaNumber = 0

    print("Total Price:", appleNumber*50 + mangoNumber*30 + bananaNumber*20,"THB")
