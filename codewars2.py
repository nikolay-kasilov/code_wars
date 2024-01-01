
'''Вам будет предоставлен массив a и значение x. Все, что вам нужно сделать,
 это проверить, содержит ли предоставленный массив значение.

Массив может содержать числа или строки. X может быть любым из них.

Верните, true если массив содержит значение, false если нет.'''
def check(seq, elem):
     return elem in seq


'''Завершите функцию square sum так, чтобы она возводила в квадрат каждое переданное в нее число, а затем суммировала результаты вместе.

Например, для [1, 2, 2] оно должно возвращать результат 9, потому что 
1
 '''                    # 1 вариант
def square_sum(numbers):
     return sum(x ** 2 for x in numbers)
                        # 2 вариант
def square_sum(numbers):
    out = []
    for i in numbers:
        out.append(i**2)
    return sum(out)
'''"Я люблю тебя"
"немного"
"очень"
"страстно"
"безумно"
"совсем не так"
Если лепестков больше 6, вы начинаете сначала с "I love you" для 7 лепестков,
 "a little" для 8 лепестков и так далее.'''
def how_much_i_love_you(nb_petals):
    n = nb_petals % 6
    if n == 1:
        return "I love you"
    if n == 2:
        return "a little"
    if n == 3:
        return "a lot"
    if n == 4:
        return "passionately"
    if n == 5:
        return "madly"
    if n == 0:
        return "not at all"

'''Если указано число от 0 до 9, верните его прописью.

Ввод :: 1

Вывод :: "One".

Если ваш язык поддерживает это, попробуйте использовать оператор switch.'''
  # 1 вариант

def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number ==1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
       # 2 вариант
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]


'''Поскольку Натан знает, как важно поддерживать уровень гидратации, он выпивает
 0,5 литра воды в час езды на велосипеде.

Вам дается время в часах, и вам нужно вернуть количество литров, которое выпьет Натан,
 округленное до наименьшего значения.'''
def litres(time):
    return int(time//2)




