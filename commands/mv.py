import shutil

"""
-- MV COMMAND SYNTAX --
$ mv [options] source dest

-- MV COMMAND SYNTAX -- 

option	description
mv -f	force move by overwriting destination file without prompt
mv -i	interactive prompt before overwrite
mv -u	update - move when source is newer than destination
mv -v	verbose - print source and destination files
man mv	help manual

"""

class mv():

    def __init__(self):
        pass

    def execute(self, cls):
        try:
            shutil.move(cls.data[0], cls.data[1])   
            print 'File moved succesfully!' 
        except OSError as error:
            print error