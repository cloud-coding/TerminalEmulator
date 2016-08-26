from Terminal.core.plugin import Plugin


class HelloPlugin(Plugin):
    Name = 'HelloPlugin'

    def OnLoad(self):
        print('HelloPlugin 1.0 Loaded!')

    def OnCommand(self, cmd, args):
        if (cmd == 'hello' and len(args) > 0):
            print('Hello, {}'.format(args[0]))
            return True
        else:
            return False