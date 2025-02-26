#Некоторые функции, реализованные в процессе обучения на курсе "Основы Python" от Хекслет

"""ТЕМА: НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ ФУНКЦИЙ
Реализуйте функцию get_hidden_card(), которая подготавливает скрытую версию номера кредитной карты для отображения на сайте.
Функция принимает два параметра:
- Номер кредитки, состоящий из 16 цифр в виде строки
- Количество звездочек в скрытой версии карты, целое число. Этот параметр является не обязательным. Его значение по умолчанию равно 4
"""
def get_hidden_card(card_number,stars = 4):
    hidden_card = card_number[-4:]
    return f'{"*" * stars}{hidden_card}'
# Примеры вызова функции:
get_hidden_card('1234567812345678', 3)  # ***5678
get_hidden_card('1234567812345678')     # ****5678


"""ТЕМА: АННОТАЦИИ ТИПОВ
Реализуйте функцию letter_multiply(). Она должна принимать три параметра:
- Слово, тип данных строка
- Букву, тоже строка, но состоящая из одного символа
- Число, которое обозначает, сколько раз нужно повторить букву в слове
Функция должна возвращать строку — слово с повторенными символами
"""
def letter_multiply(word: str, letter: str, repeat: int) -> str:
    result:str = word.replace(letter , letter*repeat)
    return result
# Примеры вызова функции:
word = 'python'
print(letter_multiply(word, 'p', 2)) # ppython
print(letter_multiply(word, 'y', 3)) # pyyython
print(letter_multiply(word, 'n', 4)) # pythonnnn


"""ТЕМА: ЛОГИЧЕСКИЕ ОПЕРАЦИИ
Реализуйте функцию is_leap_year(), которая принимает год в качестве параметра и определяет, является ли этот год високосным. 
Функция должна вернуть True, если переданный год високосный и False, если нет.
Год будет високосным, если он делится без остатка на 400, или он одновременно делится без остатка на 4 и не делится на 100
"""
def is_leap_year(year):
    return (year % 400==0) or (year % 4==0 and (year % 100 !=0))
# Примеры вызова функции:
is_leap_year(2018)  # False
is_leap_year(2017)  # False
is_leap_year(2016)  # True


"""ТЕМА: УСЛОВНЫЕ КОНСТРУКЦИИ
Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. 
Она принимает адрес сайта и возвращает его с https:// в начале. Функция всегда возвращает адрес в виде https://АДРЕС.
Функция принимает адреса в виде:
АДРЕС
http://АДРЕС
https://АДРЕС (нормализованный)
"""
def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url
# Примеры вызова функции:
normalize_url('https://ya.ru')  # https://ya.ru
normalize_url('google.com')  # https://google.com
normalize_url('http://ai.fi')  # https://ai.fi


"""ТЕМА: ОПЕРАТОР MATCH
Реализуйте функцию get_number_explanation(), которая принимает на вход число и возвращает объяснение этого числа. 
Если для числа нет объяснения, то возвращается just a number. Объяснения есть только для следующих чисел:
* 666 - devil number
* 42 - answer for everything
* 7 - prime number
"""
def get_number_explanation(number):
    match number:
        case 666: 
            return 'devil number'
        case 42: 
            return 'answer for everything'
        case 7: 
            return 'prime number'
        case _: 
            return 'just a number'


"""ТЕМА: ОБХОД СТРОК
Реализуйте функцию get_substr(), которая извлекает из строки подстроку указанной длины. 
Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа.
Собирайте строку-результат в цикле, перебирая начальную строку до определенного момента. Предполагаем, что переданная длина не выходит за границы строки.
"""
def get_substr(string, length):
    i=0
    result=''
    while i < length:
      #current_char = string[i]
      result = f'{result}{string[i]}'
      i += 1
    return result
# Примеры вызова функции:
string = 'If I look back I am lost'
print(get_substr(string, 1))  # => 'I'
print(get_substr(string, 7))  # => 'If I lo'


"""ТЕМА: УСЛОВИЯ ВНУТРИ ТЕЛА ЦИКЛА
Реализуйте функцию has_char(). Она должна проверять, содержит ли строка указанную букву (вне зависимости от регистра).
ункция принимает два параметра:
- Строка
- Буква для поиска
И возвращает результат проверки – булево значение
"""
def has_char(string, char):
    i=0
    uppercase_char = char.upper()
    while i < len(string):
        if string[i].upper() == uppercase_char:
            return True
        i += 1
    return False
