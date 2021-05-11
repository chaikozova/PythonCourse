
def hello(name):
    if len(name) > 3:
        print('Hello, ' + str(name) + '!')
        return 'Hello, ' + str(name) + '!'
    else:
        print(name, 'is too short name')


hello('Jyldyz')
hello('Adilet')
hello('Rus')
hello('abc')
hello('Ro')


def lastDigit(number):
    if len(str(number)) < 3:
        print(number, 'is too small')
    else:
        print('Last digit is', number % 10)


lastDigit(123)
lastDigit(12)
lastDigit(12334)
lastDigit(1)


# def math_formula(x ,y, z):
#     result1 = x ** 2 + y * z
#     result2 = x + y * z
#     print('result1 =', result1)
#     print('result2 =', result2)
#     return x + y +z
#
#
# print(math_formula(34, 456, 234))
# math_formula(45, 234, 234)