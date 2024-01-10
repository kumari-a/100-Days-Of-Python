# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first,second=0,0
check1=['t','r','u','e']
check2=['l','o','v','e']
name1 = name1.lower()
name2 = name2.lower()

for ch in check1:
    first=first + name1.count(ch) + name2.count(ch)


for ch in check2:
    second=second + name1.count(ch) + name2.count(ch)

score = first*10+second
if(score<=10 or score>=90):
    print(f'Your score is {score}, you go together like coke and mentos.')
elif (40<=score<=50):
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')



