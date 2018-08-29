import os


class cd():
    def __init__(self):
        pass

    def execute(self, cls):
        data = cls.data[0]

        try:
        	if data:
	            os.chdir(data)
	        else:
	            print ("Please send in the correct path")
        except:
        	print ("Please send in the correct path")

