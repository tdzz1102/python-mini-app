"""
    https://docs.python.org/ja/3/library/configparser.html
    configparserの使い方
"""

import configparser

config = configparser.ConfigParser()
with open('./config.ini') as f:
    config.read_file(f)

print(config.sections())

print(config['Waner'].get('position'))
print(config['Waner'].get('birthday', '03-27'))
print(config['Waner'].get('lover'))
print()

print(config.items('Luzao'))
print(config['Luzao'].get('birthday'))
print(config['Luzao'].get('lover'))
print()

print(config['Minuo'].get('country'))
print(config['Minuo'].getint('height'))
print()

print(config['Taffy'].get('country'))
print(config['Taffy'].getboolean('chinese'))
print('weight' in config['Taffy'])
print()