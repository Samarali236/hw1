balance =[1000] 
choice=0
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
