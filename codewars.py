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

def even_or_odd(number):
    pass
    if number % 2 == 0:
      return "Even"
    else:
      return "Odd"








