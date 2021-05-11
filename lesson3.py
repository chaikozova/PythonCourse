import random


def test():
    result = 0
    answer = input('3 + 2 = \n')
    if answer == '5':
        result += 1
    answer = input('4 + 5 = \n')
    if answer == '9':
        result += 1
    return 'Your score is '+str(result)


print(test())

def market(money):
    apple = 5
    banana = 3
    pineapple = 45
    soda = 25
    sum = apple + banana + pineapple + soda

    if money >= sum:
        print('You are able to buy')
        print('Your change is ', money-sum)
    else:
        print('You do not have enough money')


market(400)


def guess_number():
    number = input('Guess a number from 0 to 100\n')
    num = random.randint(0, 100)
    print('num =', num, 'number =',number)
    if number == num:
        print('Congratulations! You are winner')
    else:
        print('Try again')


for i in range(3):
    print(i)
    guess_number()


x = 0
while x < 3:
    x = x + 1
    guess_number()
    print(x)
