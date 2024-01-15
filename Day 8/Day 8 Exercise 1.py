# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print('Hello')
  print('How are you ?')
  print('Nice to meet you !!!')

def greet_with_name(Name):
    print(f'Hello {Name}')
    print('How are you ?')
    print('Nice to meet you !!!')

def full_greet(name,location):
    print(f'Hello {name}')
    print(f'How is weather in {location} ?')


greet()
name = input('Please enter your name : ')
greet_with_name(name)
loc = input('Please enter your location : ')
full_greet(name,loc)
print('----------------------------------')
full_greet(location=loc,name=name)
print('----------------------------------')
full_greet(location=loc,name=name)