#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на экран толь ко
# предложения, содержащие введенное с клавиатуры слово.

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()

    text = text.replace("!", ".")
    text = text.replace("?", ".")

    while ".." in text:
        text = text.replace("..", ".")

    sentences = text.split(".")

    word = input("Введите слово: ")

    for sentence in sentences:
        if word in sentence:
            if sentence in text:
                print(f'{sentence}{text[text.rfind(sentence) + len(sentence)]}')