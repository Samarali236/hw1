balance =1000
choice=0
deposite=0
transcount=0
faildwithcount=0
password= "qwerty"
userpass=""

while True:
    userpass=input("Please enter your password: ")
    if userpass == password :
     print("login successfully! ")
     break
    else:
     print("Incorrect password, try another password")

while choice !=5 :
    print("""
    Welcome to the ATM
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Transaction count
    5. Exit
          """)
    choice=int(input("please enter your choice: "))
    if choice ==1:
        print("Your balance is: "+str(balance)+"$")
    elif choice==2:
        deposite= float(input("Please enter the amount you would like to deposit: "))
        if deposite > 0:
            balance += deposite
            transcount+=1
            print("Your current balance is: "+str(balance)+"$")
        else:
            print("Please enter a valid deposite amount!")
    elif choice==3:
        withdraw = float(input("Please enter the amount you would like to withdraw: "))
        if withdraw > 0 and withdraw <= balance:
            balance -= withdraw
            transcount += 1
            print("Your current balance is: "+str(balance)+"$")
        else:
            faildwithcount+=1
            if withdraw > balance:
                 print("Dear user,you do not have enough funds for this withdrawal, please check your balance or try a smaller amount")
            if withdraw < 0:
                 print("Dear User, Please enter a valid amount for withdrawwal process")
            if faildwithcount>3:
                    print("WARNING! more than 3 failed withdrawals were attempted")
    elif choice==4:
        print(" Dear user, your total number of successfull transactions is : "+ str(transcount))
    elif choice==5:
        print("program ended, Thank you for using our ATM")
    else:
        print("Invalid number, Please choose between 1 and 5")


    
    
