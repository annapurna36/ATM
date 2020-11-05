from time import sleep

def password():
    pin = int(input("please enter your account pin: "))
    if pin == 1234:
        print ("correct account, please wait we are fetching your account")
        sleep (2)
        return True
    else:
        print ("Incorrect password, Authentication failed")
        return False

def atm_start():
        balance = 0

        print ("Hello, Welcome to the My ATM")
        if password():

            while True:


                print("press '1' for checking balance")
                print("press '2' for Withdrawl")
                print("press '3' for Deposit")
                print("press '4' for Exit")

                choose = int(input("\nchoose which money transaction fits for your day: "))

                if choose == 1:
                    print("Please wait we are fetching your data ...")
                    sleep(2)
                    print("Hello, your account balance is: ",balance)


                elif choose == 2:
                    withdrawl = int(input("How much money you want to withdraw from your account: "))
                    balance = balance-withdrawl
                    print(f"You have successfully taken {withdrawl} money from your account")



                elif choose == 3:
                    deposit = int(input("How much money you want to deposit to your account: "))
                    balance = balance+deposit
                    print(f"You have successfully added {deposit} money to your account")



                elif choose == 4:
                    print("Thanks for using the ATM, Hope you have a great day")
                    break

atm_start()
