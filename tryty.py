balance = 1000
transactions = []
choice = 0
password = "qwerty"
userpass = ""
transcount = 0
faildwithcount = 0

while choice !=6:
    userpass = input("Please enter your password: ")
    if userpass == password :
     choice = 0
     print("login successfully! ")
     while choice !=5 :
        print("""
        Welcome to the ATM
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        4. Transaction History
        5. Logout
        6. Exit System
            """)
        choice = int(input("please enter your choice: "))
        if choice == 1:
            print("Your balance is: "+str(balance)+"$")
        elif choice == 2:
            depositeAmount = float(input("Please enter the amount you would like to deposit: "))
            if depositeAmount > 0:
                balance += depositeAmount
                transcount += 1
                transactions.append("+" + str(depositeAmount))
                print("Your current balance is: "+str(balance)+"$")
            else:
                print("Please enter a valid deposite amount!")
        elif choice==3:
            withdrawalAmount = float(input("Please enter the amount you would like to withdraw: "))
            if withdrawalAmount > 0 and withdrawalAmount <= balance:
                balance -= withdrawalAmount
                transactions.append("-" + str(withdrawalAmount))
                transcount += 1
                print("Your current balance is: "+str(balance)+"$")
            else:
                faildwithcount+=1
                if withdrawalAmount > balance:
                    print("Dear user,you do not have enough funds for this withdrawal, please check your balance or try a smaller amount")
                if withdrawalAmount < 0:
                    print("Dear User, Please enter a valid amount for withdrawwal process")
                if faildwithcount>3:
                    print("WARNING! more than 3 failed withdrawals were attempted")
        elif choice==4:
            print(" Dear user, your total number of successfull transactions is : "+ str(transcount))
        elif choice==5:
            print("Logging out")
            break
        elif choice == 6:
            print("program ended, Thank you for using our ATM")
            break
        else:
            print("Invalid number, Please choose between 1 and 5")
    else:
     print("Incorrect password, try another password")