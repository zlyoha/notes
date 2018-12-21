#источник https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html
4 пробела
выравнивание по разделителю 
# Выровнено по открывающему разделителю
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
# Больше отступов включено для отличия его от остальных
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
# Нет необходимости в большем количестве отступов.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
#Закрывающие круглые/квадратные/фигурные скобки в многострочных конструкциях могут находиться под первым непробельным символом последней строки списка, например:
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
#либо быть под первым символом строки, начинающей многострочную конструкцию:
my_list = [
    1, 2, 3,
    4, 5, 6,
]
python -tt для ошибок в табуляции
maxline = 79, docline = 72
Предпочтительный способ переноса длинных строк является использование подразумеваемых продолжений строк Python внутри круглых, квадратных и фигурных скобок
перенос лучше после логического оператора, (\  возможна только для assert, with)
2 переноса, отделяя функции верхнего уровня и определения классов 
1 перенос, отделяя методы или лог. блоки, группы импорта
ctrl+L - незначащий пробел / разрыв строки
Кодировка Python должна быть UTF-8 (ASCII в Python 2).
Файлы в ASCII (Python 2) или UTF-8 (Python 3) не должны иметь объявления кодировки.
\x, \u, \U или \N - best
строки, идентификаторы, комментарии - ASCII английские слова
импорты отдельными строками (кроме from) до констант в начале файла (stdlib-external-current), после импортов __all__
реком. абсолютное импортирование
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
относительное только для оч. сложных пакетов
from . import sibling
from .sibling import example
Когда вы импортируете класс из модуля, вполне можно писать вот так:
from myclass import MyClass
from foo.bar.yourclass import YourClass
Если такое написание вызывает конфликт имен, тогда пишите:
import myclass
import foo.bar.yourclass
И используйте "myclass.MyClass" и "foo.bar.yourclass.YourClass".
from import * - не использовать
нет пробелов возле ()[]{};:, перед([
1 пробел вокруг = (кроме именованного аргумента или default) += -= == < > != <> <= >= in not in is is not and or not, но:
hypot2 = x*x + y*y
c = (a+b) * (a-b)
