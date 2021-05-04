name = input('What is your name? - ')
print(name)

try:
    age = int(input(name+', how old are you? - '))
    print(age / 2)
except ValueError as e:
    print(str(e))

if age < 18:
    print('Your age is less than 18')

