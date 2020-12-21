#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.

import sys
import json
import xml.etree.ElementTree as ET


if __name__ == '__main__':

    trains = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = input("Номер поезда: ")
            time = input("Время отправления: ")

            train = {
                'name': name,
                'num': num,
                'time': time,
            }

            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('num', 0))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 17
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        train.get('name', ''),
                        train.get('num', ''),
                        train.get('time', '')
                    )
                )

            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])

            count = 0
            for train in trains:
                if train.get('num') == number:
                    count += 1
                    print('Номер поезда:', train.get('num', 0))
                    print('Пункт назначения:', train.get('name', ''))
                    print('Время отправления:', train.get('time', ''))

            if count == 0:
                print("Таких поездов нет!")


        elif command.startswith('load '):

            # Разбить команду на части для выделения имени файла.

            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла xml.

            tree = ET.parse(f'{parts[1]}')

            root = tree.getroot()

            for item in root.iterfind('train'):
                temp = {

                    'name': str(item[0].text),

                    'num': str(item[1].text),

                    'time': str(item[2].text),

                }

                trains.append(temp)


        elif command.startswith('save '):

            # Разбить команду на части для выделения имени файла.

            parts = command.split(' ', maxsplit=1)

            temp = 0

            # Сохранить данные в файл xml.

            root = ET.Element('trains')

            for i, item in enumerate(trains):
                train = ET.SubElement(root, 'train', id=f'{i}')

                name = ET.SubElement(train, 'name')

                name.text = (trains[i].get('name'))

                num = ET.SubElement(train, 'num')

                num.text = (trains[i].get('num'))

                time = ET.SubElement(train, 'time')

                time.text = (trains[i].get('time'))


            # print(ET.tostring(root, encoding="utf-8", method="xml").decode(encoding="utf-8"))

            tree = ET.ElementTree(root)

            tree.write(f'{parts[1]}')

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
