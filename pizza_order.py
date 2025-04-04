print("Welcome to zakiya's pizza! ")
pizza=input("What type of pizza do you want?\n small\nmedium\nlarge ")
bill=0
if pizza == 'small':
    bill+=100
    print("you have to pay 100 rupees")
elif pizza =='medium':
    bill+=200
    print("you have to pay 200 rupees")
elif pizza =='large':
    bill+=300
    print("you have to pay 300 rupees")
pepparoni=input("Do you want peporoni? ")
if pepparoni=='y' or pepparoni=='Y':
    if pizza=='small':
        bill=bill+30
        print("your have to pay 30 rupees extra")
    elif pizza == 'medium':
         bill=bill+50
         print("you have to pay 50 rupees extra")
    elif pizza=='large':
         bill=bill+60
         print("you have to pay 60 rupees extra")
extra_chees=input("do you want extra chese? ")
if extra_chees=='y' or extra_chees=='Y':
    bill+=20
    print(f"your total bill is{bill}")
print("enjoy your pizza!")
