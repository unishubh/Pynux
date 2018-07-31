import os


class pwd():
    def __init__(self):
        print "In init"

    def execute(self, cls):
        print os.getcwd()