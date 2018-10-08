import os

class mkdir():
    def __create_folder(self, path):
        try:
            os.mkdir(path, )
        except OSError:
            print('The folder already exist')

    def execute(self, terminal):
        path_to_create = terminal.data
        if path_to_create:
            self.__create_folder(path_to_create[0])
        else:
            print('Syntax error')
