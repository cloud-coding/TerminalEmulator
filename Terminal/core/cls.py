def cls():
    from sys import platform
    from os import system
    if platform == 'win32' or platform == 'win64':
        system('cls')
    else:
        system('clear')