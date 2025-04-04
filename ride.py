height =int(input("Enter your height: "))
bill=0
if height >=3:
    print("You can ride")
    age=int(input("Enter your age : "))
    if age<=10:
        bill=250
        print("You have to pay 250")
    elif age<=20:
        bill=300
        print("You have to pay 300")
    elif age<=30:
        bill=500
        print("You have to pay 500")
    want_photo=input("Do you want photo? ")
    if want_photo=='y' or want_photo=='Y':
        bill=bill+50
        print(f"Your total bill is {bill}")
    print("Thank you ...\n Enjoy your ride")
else:
    print(" Sorry! \nYou can not ride")
