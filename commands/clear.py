from os import system,name


class clear():

    def __init__(self):
        pass

    def execute(self,cls):

        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
