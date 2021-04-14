import random


database = {}


currentBalance = random.randrange(0,1000000)
def init():


    print('Welcome to Maple Bank')


    haveAcct = int(input('Do you have an account with us? : (1) yes (2) no \n'))

    if(haveAcct == 1):
        print(logIn())
    elif(haveAcct == 2):
        print(register())
    else:
        print('You have selected an invalid option')
        init()
def logIn():
    print('*******LogIn*******')
    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')
    for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
    print('Invalid account number or password')
    logIn()
def register():
    print('*******Create One*******')
    email = input(('What is your email address? \n'))
    firstName = input(('What is your first name? \n'))
    lastName = input(('What is your last name \n'))
    password = input(('Create a password \n'))

    accountNumber = generateAccountNumber()

    
    database[accountNumber] = [firstName, lastName, email, password, currentBalance]

    print('Your Account has been created')
    print('='*30)
    print('Your Account Number is %d' % accountNumber)
    print('Please keep it safe')
    print('='*30)

    print('Your account has been created')
    print('You can log in now')
    logIn()

def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))
    option = int(input('What would you like to do? \n (1) withdrawal \n (2) deposit \n (3) check balance \n (4) complaint \n (5) logout \n (6) exit \n'))
    if(option == 1):
      withdrawal()
    elif(option == 2):
      deposit()
    elif(option == 3):
        checkBalance()
    elif(option == 4):
        complaint = input('What issue would you like to report? \n')
        print('Thank you for contacting us')
        logIn()
    elif(option == 5):
        logOut()
    elif(option == 6):
        exit()
    else:
        print('invalid option selected')
        bankOperation(user)
def generateAccountNumber():
    return random.randrange(2000000000,2099999999)
def withdrawal():
     withdraw = int(input('how much would you like to withdraw? \n'))
     if(withdraw > currentBalance):
           print('insufficient funds')
           print('Your current balance is %d' %currentBalance)
           withdrawal()
     elif(withdraw <= currentBalance):
           print('Take your cash')
           logIn()
     else:
           print('error')
           withdrawal()
def deposit():
    deposit = int(input('how much would you like to ? \n'))
    newBalance = currentBalance + deposit
    print('Your new balance is %d' % newBalance)
    logIn()
def checkBalance():
    print('Your current balance is %d' %currentBalance)
    logIn()
def logOut():
    logIn()
init()