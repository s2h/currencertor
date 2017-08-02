#!/usr/bin/env python3
"""Converts currencies between each other"""
import sys
from lxml import etree
from colorama import Fore, Style

def main(args):
    """main function"""
    root = etree.parse('http://www.cbr.ru/scripts/XML_daily.asp').getroot()
    currencies = {}
    for child in root:
        if child.find('NumCode').text == '840':
            dollar = float(child.find('Value').text.replace(',', '.'))
            currencies[child.find('CharCode').text] = dollar
        if child.find('NumCode').text == '978':
            eur = float(child.find('Value').text.replace(',', '.'))
            currencies[child.find('CharCode').text] = eur
    print('Доллар: {}. Евро {}'.format(dollar, eur))
    if len(args) > 1:
        arg = args[1].replace(",", ".")
        for name in currencies:
            print('{} {} в рублях: {}. {} рублей в {}: {}.'.format(
                Fore.GREEN + arg + Style.RESET_ALL, name, Fore.RED + str(round(
                    float(arg) * currencies[name], 2)) + Style.RESET_ALL,
                Fore.GREEN + arg + Style.RESET_ALL, name, Fore.RED + str(round(
                    float(arg) / currencies[name], 2)) + Style.RESET_ALL))


if __name__ == '__main__':
    main(sys.argv)
