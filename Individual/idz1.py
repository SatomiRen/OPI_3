#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

if __name__ == "__main__":
    with open('../Examples/text.txt', encoding='UTF') as f:
        while True:
            line = f.readline()
            if len(line) == 0:  # Нулевая длина обозначает конец файла
                break
            if not re.findall(r'\d{2}', line):
                print(line)
        f.close()  # закрываем файл
