a=float(input('Введите число:'))
b=float(input('Введите второе число:'))
c=int(input('Нажмите 1 если хотите посчитать эти два числа, нажмите 0 для того чтобы добавить число:'))
e = '+'
i = '-'
f = '/'
g = '*'
if c==1:
    print('Вы не добавили новое число, тогда давайте начнём считать первые два числа! ')
    d=input('Какое действие вы хотите совершить? + , - , / , *')

    if d==e:
        result1=a+b
        print(result1)
    if d==i:
        result2=a-b
        print(result2)
    if d==f:
        result3=a/b
        print(result3)
    if d==g:
        result4=a*b
        print(result4)
if c==0:

    v = float(input('Введите число:'))
    d = input('Какое действие вы хотите совершить? + , - , / , *')
    if d == e:
            result1 = a + b + v
            print(result1)
    if d == i:
            result2 = a - b - v
            print(result2)
    if d == f:
            result3 = a / b / v
            print(result3)
    if d == g:
            result4 = a * b * v
            print(result4)
else:
    print('Конец')


