import operator


operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

str = input()
stack=[]

assert str[0] in operators, 'Неправильная операция'

for token in str.split(" "):

    if token in operators:
        oper = token
    else:
        stack.append(token)


rezult=0
kol = 0
try:
    if len(stack) < 2:
        raise SyntaxError
    for i in stack:
        if kol == 0:
            rezult = int(i)
        else:
            if oper == '*':
                rezult = rezult * int(i)
            if oper == '+':
                rezult = rezult + int(i)
            if oper == '-':
                rezult = rezult - int(i)
            if oper == '/':
                rezult = rezult / int(i)
        kol = kol+1
except ValueError:
    print('Введено не число')
except ZeroDivisionError:
    print ('Деление на ноль ')
except SyntaxError:
    print ('Мало операндов')
except Exception:
    print ('Произошла ошибка')
else:
    print ( 'Ответ: ',rezult)



