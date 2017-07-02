from sys import stdin # функция ввода данных


def parse(robot, line): # новая функция
    command = line.split() # разделение строки по пробелам
    length = len(command) # вычисление количества аргументов

    if length == 1: # если команда состоит из одного слова
         if command[0] == 'distance': # если это команда - distance
             print(round((robot['x'] ** 2 + robot['y'] ** 2) ** 0.5)) # расчет расстояния

    elif length == 2: # если команда состоит из двух слов
        direction, amount = command[0], int(command[1]) # то разделяю её на направление и количество метров
                                                        # если вместо числа вторым доводом приходит просто строка, то выкидывается исключение ValueError
                                                        # исключение обрабатывается в главном цикле

        if direction == 'right': # если робот идет вправо
            robot['x'] += amount # добавляю то число к его координате x
        elif direction == 'left': # аналогично
            robot['x'] -= amount
        elif direction == 'forward':
            robot['y'] += amount
        elif direction == 'backward':
            robot['y'] -= amount

if __name__ == '__main__': # если запуск из консоли, а не подключается с помощью import
                           # то следующие действия
    robot = {'x': 0, 'y': 0} # новый робот

    for line in stdin: # читаю по одной строке из потока ввода
        try: # попытка выполнить какие-то действия
            parse(robot, line) # распарсить команду
        except ValueError: # если во время выполнения действий выкинулось исключение

            pass # бездействие

