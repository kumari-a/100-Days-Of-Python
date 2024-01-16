from art import logo

print(logo)

num1 = int(input("What is your first number? : "))
op = input("What is your operation you want? \n + \n - \n * \n / \n Enter your inpur: ")
num2 = int(input("What is yout second number? : "))

while True:
    ans=0
    if op=='+':
        ans=num1+num2
    elif op == '-':
        ans=num1-num2
    elif op=='*':
        ans=num1*num2
    elif op=='/':
        ans=num1/num2
    else:
        print('Invalid operator')
        break
    print(f"{num1} {op} {num2} = {ans}")
    further = input("You want to continue with current operation or have new operation or exit? \n To continue with current output enter conti \n To start from again enter new \n To exit enter exit \n Enter your choice").lower()
    if further=='conti':
        num1=ans
        op = input("What is your operation you want? \n + \n - \n * \n / \n Enter your inpur: ")
        num2 = int(input("What is yout second number? : "))
    elif further =='new':
        num1 = int(input("What is your first number? : "))
        op = input("What is your operation you want? \n + \n - \n * \n / \n Enter your inpur: ")
        num2 = int(input("What is yout second number? : "))
    else:
        print("Thank You !!!")
        break;



