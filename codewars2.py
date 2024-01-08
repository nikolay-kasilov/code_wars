
'''Вам будет предоставлен массив a и значение x. Все, что вам нужно сделать,
 это проверить, содержит ли предоставленный массив значение.
Массив может содержать числа или строки. X может быть любым из них.
Верните, true если массив содержит значение, false если нет.'''
def check(seq, elem):
     return elem in seq


'''Завершите функцию square sum так, чтобы она возводила в квадрат каждое переданное 
в нее число, а затем суммировала результаты вместе.
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



'''У меня есть кошка и собака.
Я получил их одновременно с котенком / щенком. Это было humanYears много лет назад.
Теперь возвращает их соответствующий возраст как [humanYears,catYears,dogYears]
Примечания:
Человеческих лет >= 1
Человеческие годы - это только целые числа
Кошачьи годы
15 cat years за первый год
+9 второй год обучения в cat years
+4 кошачьи годы за каждый последующий год
Собачьи годы'''
def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears += 15
        dogYears += 15
        return [human_years, catYears, dogYears]
    elif human_years == 2:
        catYears += 24
        dogYears += 24
        return [human_years, catYears, dogYears]
    elif human_years > 2:
        catYears += 24
        dogYears += 24
        years = human_years - 2
        catYears += years*4
        dogYears += years*5
        return [human_years, catYears, dogYears]
    return [0,0,0]
'''Нам нужна функция, которая может преобразовывать число (integer) в строку.

Какие способы достижения этого вы знаете?'''
def number_to_string(num):
    return str(num)

"""В этом небольшом задании вам дается строка чисел, разделенных пробелом,
 и вы должны вернуть наибольшее и наименьшее число.

Примеры
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Примечания
Все числа действительны Int32, нет необходимости их проверять.
Во входной строке всегда будет хотя бы одно число.
Выходная строка должна состоять из двух чисел, разделенных одним пробелом,
 и первым должно быть наибольшее число."""
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))

'''Напишите функцию, которая преобразует входную строку в верхний регистр.'''
def make_upper_case(s):
    return s.upper()
'''заправка находится в 50 милях отсюда! Вы знаете, что в среднем ваш 
автомобиль расходует около 25 миль на галлон. Остались 2 галлоны.
Учитывая эти факторы, напишите функцию, которая сообщает вам, возможно ли добраться 
до пампа или нет.
Функция должна возвращать данные, true если это возможно, и false если нет.'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

'''Завершите решение так, чтобы оно перевернуло переданную в него строку.
'world'  =>  'dlrow'
'word'   =>  'drow'
'''
def solution(string):
    text = string[::-1]
    return text

'''В этом ката вы создадите функцию, которая принимает список неотрицательных целых чисел и строк и возвращает новый список с отфильтрованными строками.
Пример  filter_list([1,2,'a','b']) == [1,2]'''
def filter_list(items):
    return [item for item in items if isinstance(item, int)]

'''Возвращает количество гласных в заданной строке.
Мы будем рассматривать a, e, i o, u y как гласные для этого ката (но не для этого).
Входная строка будет состоять только из строчных букв и / или пробелов.'''
def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for s in sentence:
        if s in vowels:
            total += 1
    return total

def getCount(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")

'''Банкоматы допускают использование 4-или 6-значных PIN-кодов, а PIN-коды не могут 
содержать ничего, кроме ровно 4 цифр или ровно 6 цифр.
Если функции передана допустимая строка PIN, верните true, иначе верните false.
Примеры (Ввод --> Вывод)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
'''
def validate_pin(pin):
    return len(pin) in [4 , 6] and pin.isdigit()




