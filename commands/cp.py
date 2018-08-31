import shutil

class cp():
    def __init__(self):
        pass

    def execute(self, cls):
        data = cls.data
        try:
            src = data[0]
            destination = data[1]
        except:
            print("Invalid syntax of cp command")
        shutil.copy(src, destination)