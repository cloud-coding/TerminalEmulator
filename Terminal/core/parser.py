class parser:
    def __init__(self, line = ''):
        if line.find(' ') > -1:
            pass
        else:
            if line == 'help':
                print('help')
            elif line == 'q':
                exit()