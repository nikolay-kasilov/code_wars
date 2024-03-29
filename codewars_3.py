'''Напишите функцию для разделения строки и преобразования ее в массив слов.
 "Robin Singh" ==> ["Robin", "Singh"]'''
def string_to_array(s):
    return s.split(' ')
'''Напишите программу, которая находит суммирование каждого числа от 1 до num. Число всегда будет
 положительным целым числом, большим 0. Вашей функции нужно только возвращать результат, в приведенном ниже
  примере между скобками показано, как вы достигаете этого результата, и это не является его частью, смотрите
Примеры тестов.  Например, (Ввод -> Вывод): 2 -> 3 (1 + 2)'''


def summation(num):
    return sum(range(1, num + 1))

def summation(num):
    return (1+num) * num / 2
'''Завершите функцию, которая принимает два целых числа (a, b, где a < b)
 и возвращает массив всех целых чисел между входными параметрами, включая их.'''
def between(a,b):
    return list(range(a,b+1))
 
def between(a,b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

'''Тролли атакуют ваш раздел комментариев!
Распространенный способ справиться с этой ситуацией - убрать все гласные из комментариев троллей, нейтрализуя угрозу.
Ваша задача - написать функцию, которая принимает строку и возвращает новую строку с удаленными всеми гласными.
Например, строка "Этот веб-сайт для неудачников, ЛОЛ!" станет "Ths wbst s fr lsrs LL!".
Примечание: для этого ката y не считается гласной.'''
def disemvowel(string_):
    text = list(string_)
    for i in text[::-1]:
        if i in 'aeiouAEIOU':
            text.remove(i)
    return str(''.join(text))

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
'''Нам нужна функция, которая может преобразовывать строку в число. Какие способы достижения этого вы знаете?
Примечание: Не волнуйтесь, все входные данные будут строками, и каждая строка является абсолютно корректным 
представлением целого числа.'''
def string_to_number(s):
    result = int(s)
    return  result

'''Камень ножницы Бумага
Давайте играть! Вы должны вернуть, какой игрок выиграл! В случае ничьей верните Draw!.
Примеры (Ввод1, Ввод2 --> Вывод):
«ножницы», «бумага» --> «Игрок 1 выиграл!»
«ножницы», «камень» --> «Игрок 2 выиграл!»
«бумага», «бумага» --> «Рисуй!»
 "scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"'''
def rps(p1, p2):
    if p1=="scissors" and p2== "paper":
        return "Player 1 won!"
    if p1=="scissors" and p2 =="rock":
        return "Player 2 won!"
    elif p1 == "paper"and p2 =="paper":
        return "Draw!"

'''Напишите функцию, которая всегда возвращает 5

Звучит просто, не так ли? Просто имейте в виду, что вы не можете 
использовать ни один из следующих символов: 0123456789*+-/'''
def unusual_five():
    return(len('aaaaa'))
'''В крокетном клубе Western Suburbs есть две категории членства: старшая и Открытая.
 Они хотели бы получить вашу помощь с формой заявки, в которой потенциальным членам
  будет указано, в какую категорию они будут отнесены.
Чтобы стать старшим участником, участнику должно быть не менее 55 лет и у него гандикап 
больше 7. В этом крокетном клубе гандикапы варьируются от -2 до + 26; чем лучше игрок, 
тем ниже гандикап.

Входные данные
Входные данные будут состоять из списка пар. Каждая пара содержит информацию об одном 
потенциальном участнике. Информация состоит из целого числа, обозначающего возраст 
человека, и целого числа, обозначающего его инвалидность.
Вывод
Выходные данные будут состоять из списка строковых значений (в Haskell и C: Open или 
Senior), указывающих, следует ли поместить соответствующего участника в категорию
 senior или open.
Пример'''
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res