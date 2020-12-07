#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import date
import sys
from typing import List
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class Train:
        name: str
        post: str
        year: int


@dataclass
class Staff:
    workers: List[Train] = field(default_factory=lambda: [])

    def add(self, name, post, year):
        self.workers.append(
            Train(
                name=name,
                post=post,
                year=year
            )
        )

        self.workers.sort(key=lambda worker: worker.name)

    def list(trains):
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
                    train.get('time', 0)
                )
            )

        print(line)


    def select(trains):
        count = 0
        for train in trains:
            if train.get('num') == number:
                count += 1
                print('Номер поезда:', train.get('num', ''))
                print('Пункт назначения:', train.get('name', ''))
                print('Время отправления:', train.get('time', ''))

        if count == 0:
            print("Таких поездов нет!")


    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = trains.read()

        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)

        self.trains = []
        for trains_element in tree:
            num, name, time = None, None, None


            for element in trains_element:
                if element.tag == 'num':
                    num = int(element.text)
                elif element.tag == 'name':
                    name = element.text
                elif element.tag == 'time':
                    time = (element.text)

                if num is not None and name is not None and time is not None:
                    self.trains.append(
                        Train(
                            num=num,
                            name=name,
                            time=time
                        )
                    )

    def save(self, filename):
        root = ET.Element('workers')
        for worker in self.workers:
            worker_element = ET.Element('worker')

            name_element = ET.SubElement(worker_element, 'num')
            name_element.text = worker.num

            post_element = ET.SubElement(worker_element, 'name')
            post_element.text = worker.name

            year_element = ET.SubElement(worker_element, 'time')
            year_element.text = str(worker.time)

            root.append(worker_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':

    staff = Staff()

    trains = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название пункта назначения: ")
            post = int(input("Номер поезда: "))
            year = input("Время отправления: ")

            add(self, name, post, year)

        elif command == 'list':
            print(list(trains))

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])
            select(trains)

        elif command.startswith('load '):
        # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
        # Загрузить данные из файла.
            staff.load(parts[1])

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            staff.save(parts[1])

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)