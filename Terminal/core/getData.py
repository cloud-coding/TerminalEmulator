class getData():
    def __init__(self, lang, version, user, cmd_user, cmd_apt, sys_path, word_system, terminal, plugin):
        self.lang = lang
        self.version = version
        self.user = user
        self.cmd_user = cmd_user
        self.cmd_apt = cmd_apt
        self.sys_path = sys_path
        self.word_system = word_system
        self.terminal = terminal
        self.plugin = plugin
        self.freedom = None #Придумать права. Где через плагин нельзя будет получить данные некоторые

    def getLang(self):
        return self.lang
    def getVersion(self):
        return self.version
    def getSysPath(self):
        return self.sys_path

    def getUser(self):
        return self.user
    def getTerminal(self):
        return self.terminal
    def getCmdApt(self):
        return self.cmd_apt
    def getWordSystem(self):
        return self.word_system
    def getPlugin(self):
        return self.plugin