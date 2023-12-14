# #вариант  1
# def remainder(a,b):
#     if min(a, b) == 0:
#         return None
#     elif a > b:
#         return a % b
#     else:
#         return b % a
# #вариант 2
# def remainder1(a,b):
#     if min(a,b)!=0: return max(a,b)%min(a,b)
# #вариант 3
# def remainder3(a,b):
#     return max(a, b) % min(a, b) if min(a, b) else None
# #вариант 4
# def remainder4(a:int, b:int)->int:
#     '''Returns remainder of the larger of two numbers
#     being divided by the smaller of two numbers.
#     Returns None for divide by zero.'''
#     try:
#         return max(a, b) % min(a, b)
#     except ZeroDivisionError:
#         return None

# def even_or_odd(number):
#     pass
#     if number % 2 == 0:
#       return "Even"
#     else:
#       return "Odd"

flower1 = 5
flower2 = 8
def lovefunc(flower1, flower2):
    while \
    flower1 % 2 ==0 and flower2 % 2 != 0:
        return True
    else:
        return False

"""
Сделайте функцию, которая создаст новый список из этого, заменив None на 0
"""

test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]
for i in range(len(test_lst)):
    for j in range(len(test_lst[i])):
        if test_lst[i][j] == None:
            test_lst[i][j] = 0



print (test_lst)












