import commands
from utils import InputParser
import logging
import os

log = logging.getLogger('terminal')


class Terminal:

    def __init__(self):
        self.history_stack = []
        self.last_command = None
        self.command = None
        self.data = None
        self.options = []

    def set_last_command(self):
        self.last_command = self.command

    def push_to_history(self):
        self.history_stack.append(self.command)

    def get_last_command(self):
        return self.last_command

    def get_command(self):
        show_path = os.getcwd()
        if os.name == 'nt':
            show_path = show_path.split('\\')
        else:
            show_path = show_path.split('/')
        show_path = show_path[-2:]
        show_path = "/".join(show_path)
        command = raw_input(show_path+'$ ')
        return command

    def play(self):
        while True:
            try:
                self.command = self.get_command()
                log.info(self.command)
                self.command, self.data, self.options = InputParser.parse_input(self.command)
                executer = getattr(commands, self.command)
                
            except:
                print ("The command is either invalid or not supported yet")
            executer().execute(self)
            self.set_last_command()
            self.push_to_history()
