#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read()

    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")

    # Удалить все многоточия.
    while ".." in text:
        text = text.replace("..", ".")

    # Разбить текст на предложения.
    sentences = text.split(".")

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if "," in sentence:
            with open('text.txt', 'r') as i:
                new_text = i.read()
                if sentence in new_text:
                    print(f'{sentence}{new_text[new_text.rfind(sentence) + len(sentence)]}')