balance =[1000] 
choice=0
deposite=0
transcount=0
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
        print("Your balance is: "+str(balance[0])+"$")
    elif choice==2:
        deposite=float(input("Please enter the amount you would like to deposit: "))
        balance[0] += deposite
        transcount+=1
        print("Your current balance is: "+str(balance[0])+"$")
    elif choice==3:
        withdraw=float(input("Please enter the amount you would like to withdraw: "))
        if  withdraw<= balance[0]:
            balance[0]-=withdraw
            transcount+=1
            print("Your current balance is: "+str(balance[0])+"$")
        else:
            print("Dear user,you do not have enough funds for this withdrawal, please check your balance or try a smaller amount")
            
    elif choice==4:
        print(" Dear user, your total number of successfull transactions is : "+ str(transcount))
    elif choice==5:
        print("program ended, Thank you for using our ATM")
    else:
        print("Invalid number, Please choose between 1 and 5")


    
    
