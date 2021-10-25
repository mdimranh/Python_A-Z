class Pycharm:

    def execute(self):
        print('Compiling')
        print('Running')

class Mycharm:

    def execute(self):
        print('Spell check')
        print('Convention check')
        print('Compiling')
        print('Running')

class laptop:

    def code(self, ide):
        ide.execute()

ide = Mycharm()

lap1 = laptop()
lap1.code(ide)