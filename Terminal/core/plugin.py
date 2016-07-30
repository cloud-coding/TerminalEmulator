import os
import sys

Plugins = []


class Plugin(object):
    Name = 'undefined'

    def OnLoad(self):
        pass

    def OnCommand(self, cmd, args):
        pass


def LoadPlugins():
    path = os.path.join('Terminal', 'disk', 'system', 'plugins')
    ss = os.listdir(path)
    sys.path.insert(0, path)

    for s in ss:
        __import__(os.path.splitext(s)[0], None, None, [''])

    for plugin in Plugin.__subclasses__():
        p = plugin()
        Plugins.append(p)
        p.OnLoad()

    return