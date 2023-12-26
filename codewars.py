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







































