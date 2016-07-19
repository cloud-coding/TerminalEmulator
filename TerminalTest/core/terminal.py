def log(string):
    print(string)

def joinPath(*a):
    from os import path
    s = ''
    for i in a:
        path.join(s, i)
    return s

class Terminal:
    def __init__(self, data, r_t):
        log('Загрузка терминала...')
        self.core_version = '1.0'
        self.r_t = r_t
        self.path = 'Terminal\\disk'
        self.warning = []
        log('Вход в систему')
        Terminal.__loginsystem__(self, data)
    def __loginsystem__(self, data):
        if data['user'] is None:
            self.group = 'guest'
            self.warning.append('Пользователь вошел как \"Гость\"')
            self.authorization = True
        else:
            import os
            user = os.path.join(self.path, 'system', 'users', data['user'])
            if os.path.exists(user):
                from hashlib import sha224
                from json import loads
                f = open(user)
                file = loads(f.read())
                if file['password'] == sha224(data['pass'].encode()).hexdigest():
                    self.group = file['group']
                    self.warning.append('Пользователь вошел как \"{}\"'.format(file['group']))
                    self.authorization = True
                else:
                    self.warning.append('Данный пароль неправильный')
                    self.authorization = False
            else:
                self.group = 'guest'
                self.warning.append('Данный аккаунт не существует. Пользователь вошел как \"Гость\"')
                self.authorization = True
    def getWarnings(self):
        for i in self.warning:
            log(i)
        self.warning.clear()

    def getData(self, string):
        list_data = {
            "auth": self.authorization,
            "group": self.group
        }
        try:
            mult = list_data[string]
            return mult
        except KeyError as e:
            log('Undefined unit: {}'.format(e.args[0]))
            return False
