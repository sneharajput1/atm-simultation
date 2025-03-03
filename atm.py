

print("Please insert Your CARD")

password= 132004

#taking atm pin from user
pin= int(input("enter your atm pin "))

#user account balance
balance = 45005

#checking pin is valid or not 
if pin== password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == balance
			2 == withdraw balance
			3 == deposit balance
			4 == exit
			"""
              )

        try:    
             #taking an option from user to select the choice
            option = int(input("Please enter your choice "))
        except:
            print("Please enter valid option")
        
        #for option 1 the action will perform       
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("please enter withdraw amount "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")

            

        if option == 3:

            deposit_amount = int(input("please enter deposit amount"))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")

            print(f"your updated balance is {balance}")

        if option == 4:

            break


else:
    print("SORRY!TRY AGAIN LATER")