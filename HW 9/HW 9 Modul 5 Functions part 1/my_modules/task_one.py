"""Задание 1. Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
                                        Bill Gates
"""


def display_text():
    print('“Don\'t compare yourself with anyone in this world…', 'if you do so, you are insulting yourself.”',
          sep='\n', end='\n' + '\t' * 10 + 'Bill Gates')
