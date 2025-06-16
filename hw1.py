balance =[1000] 
choice=0
deposite=0
while choice !=4 :
    print("""
    Welcome to the ATM
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
          """)
    choice=int(input("please enter your choice: "))
    if choice ==1:
        print("Your balance is: "+str(balance[0])+"$")
    elif choice==2:
        deposite=float(input("Please enter the amount you would like to deposit: "))
        balance[0] += deposite
        print("Your current balance is: "+str(balance[0])+"$")
