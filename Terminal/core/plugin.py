import os
import sys

Plugins = []


class Plugin(object):
    Name = 'undefined'
    File = 'example.py'
    commands = []

    def OnLoad(self):
        pass

    def OnCommand(self, cmd, args):
        pass



def LoadPlugins():
    path = os.path.join('Terminal', 'disk', 'system', 'plugins')
    ss = os.listdir(path)
    sys.path.insert(0, path)

    for s in ss:
        try:
            __import__(os.path.splitext(s)[0], None, None, [''])
        except:
            print('Не удалось загрузить плагин {}'.format(s.split('.')[0]))

    for plugin in Plugin.__subclasses__():
        try:
            p = plugin()
            Plugins.append(p)
            p.OnLoad()
        except:
            print('Не удалось загрузить плагин {}'.format(p.Name))

    return
