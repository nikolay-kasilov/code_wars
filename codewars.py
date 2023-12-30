# #вариант  1
def remainder(a,b):
    if min(a, b) == 0:
        return None
    elif a > b:
        return a % b
    else:
        return b % a
#вариант 2
def remainder1(a,b):
    if min(a,b)!=0: return max(a,b)%min(a,b)
#вариант 3
def remainder3(a,b):
    return max(a, b) % min(a, b) if min(a, b) else None
#вариант 4
def remainder4(a:int, b:int)->int:
    '''Returns remainder of the larger of two numbers
    being divided by the smaller of two numbers.
    Returns None for divide by zero.'''
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        return None

def even_or_odd(number):
    pass
    if number % 2 == 0:
      return "Even"
    else:
      return "Odd"

def lovefunc(flower1, flower2):
    if flower1  % 2 == 0 and flower2 % 2 == 0:
        return False
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    elif flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    else:
        return False

def find_smallest_int(arr):           # 8 уровень
    return min(arr)
def disenvowe(string):
    return '' .join(i for i in string if i not in 'aeuyAEYUO')   # 7 уровень
def square_digits(num):
    return int("".join([str(int(n)**2) for n in str(num)]))     # 7уровень

text = ['hello', 'world', 'this', 'is', 'great']
def smash(words):
    return ' '.join(words)     # 8 уровень

def digitize(n):

    return [int(x) for x in str(n)[::-1]]

def get_grade(s1, s2, s3):                  #7 уровень
    mean = sum([s1, s2, s3]) / 3
    if mean >= 90: return 'A'
    if mean >= 80: return 'B'
    if mean >= 70: return 'C'
    if mean >= 60: return 'D'
    return 'F'

''' Вы должны возвращать false, ни разу на самом деле не используя слово false...'''
def ifChuckSaysSo():
    return 0

'''Учитывая массив целых чисел, верните новый массив с удвоением каждого значения.'''

a= [1,2,10]
def maps(a):
    return [2 * x for x in a]
print(maps(a))

'''Ваша задача - создать функцию, которая выполняет четыре основных математических операции.

Функция должна принимать три аргумента - operation(строка /символ), value1(число),
 value2(число).
Функция должна возвращать результат чисел после применения выбранной операции.

Примеры(Operator, value1, value2) --> вывод
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
'''

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1- value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1/value2
    else:
        return 'неизвестная операция'

'''Это ката о умножении данного числа на восемь, если оно четное,
 и на девять в противном случае.'''

def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9


'''Создайте функцию, которая принимает строку и одиночный символ и возвращает
 целое число от количества вхождений, второй аргумент которого находится в первом.

Если не удается найти ни одного вхождения, должно быть возвращено значение 0.'''

def str_count(strng, letter):
    return (strng.count(letter))


def str_count(strng, letter):
    counter = 0

    for chr in strng:
        if chr == letter:
            counter += 1

    return counter

'''Создайте функцию, которая выдает персонализированное приветствие.
 Эта функция принимает два параметра: name и owner.

Используйте условные обозначения, чтобы вернуть правильное сообщение:'''
def greet(name, owner):

    if name == owner:
        return 'Hello, boss'
    else:
        return 'Hello,guest'

'''Ваша задача - создать две функции (max и min, или maximum и minimum и т.д.,
 В зависимости от языка), которые получают список целых чисел в качестве 
 входных данных и возвращают наибольшее и наименьшее число 
 в этом списке соответственно.'''


def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)

'''Учитывая непустой массив целых чисел, верните результат умножения значений по порядку.
 Пример: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24'''

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product


'''Бобу нужен быстрый способ вычислить объем кубоида с тремя значениями:
 length, width и height кубоида.
 Напишите функцию, которая поможет Бобу с этим вычислением.'''


def get_volume_of_cuboid(length, width, height):
    s = length * width * height
    return s

'''Напишите функцию bmi, которая вычисляет индекс массы тела (bmi = вес / рост2).

если ИМТ <= 18,5, возвращаем "Недостаточный вес"

если ИМТ <= 25,0 возвращает значение "Нормальный"

если ИМТ <= 30,0, возвращается "Избыточный вес"

если ИМТ > 30, возвращается "Ожирение"'''
def bmi(weight, height):
    bmi = weight/height**2
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <=25.0:
        return 'Normal'
    elif bmi <=30.0:
        return 'Overweight'
    elif bmi > 30:
        return 'Obese'



























