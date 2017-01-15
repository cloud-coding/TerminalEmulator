def cls():
    from sys import platform
    from os import system
    system('cls' if platform == 'win32' else 'clear')