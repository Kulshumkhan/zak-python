year=int(input("Enter years to check: "))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print(f"{year} is a leap yr.")
        else:
            print(f"{year} is not a leap year ")
    else:
        print(f"{year }is a leap yr.")
else:
    print(f"{year }is a  not leap yr.")
