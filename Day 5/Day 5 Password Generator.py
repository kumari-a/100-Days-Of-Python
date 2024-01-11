# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
import string

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? "))
alpha_numeric = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))
ans=''
for i in range(letters):
    ans+=random.choice(string.ascii_letters)

for i in range(alpha_numeric):
    ans+=random.choice(string.punctuation)

for i in range(numbers):
    ans+=random.choice(string.digits)

ans = ''.join(random.sample(ans,len(ans)))

print(f"Your password is : {ans}")