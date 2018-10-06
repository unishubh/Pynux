import os


class cd():
    def __init__(self):
        pass

    def execute(self, cls):
        data = cls.data[0]

        try:
            os.chdir(data)
        except:
        	print ("Please send in the correct path")

