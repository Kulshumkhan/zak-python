print("Welcome to Love calculator Zakiya Website!")
your_name=input("Enter your name: ")
patner_name=input("Enter your patner name: ")
your_name.lower()
patner_name.lower()
fullmatch=your_name+patner_name
t=fullmatch.count('t')
r=fullmatch.count('r')
u=fullmatch.count('u')
e=fullmatch.count('e')
true = t+r+u+e

l=fullmatch.count('l')
o=fullmatch.count('o')
v=fullmatch.count('v')
e=fullmatch.count('e')
love=l+o+v+e
love_score= int(str(true)+str(love))
if love_score < 10 or love_score >90:
    print(f"your love score is {love_score} and you go like coke and mentos")
elif love_score >=40 and love_score<=50:
    print(f"your love score is {love_score}\n you both look good with each other ")
else:
    print(f"your love score is {love_score}\n you may be perfect husband wife!")

