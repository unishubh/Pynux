import commands
from utils import InputParser


class Terminal:

    def __init__(self):
        self.history_stack = []
        self.last_command = None
        self.command = None
        self.options = []

    def set_last_command(self):
        self.last_command = self.command

    def push_to_history(self):
        self.history_stack.append(self.command)

    def get_last_command(self):
        return self.last_command

    def get_command(self):
        command = raw_input()
        return command

    def play(self):
        while True:
            try:
                self.command = self.get_command()
                self.command, self.options = InputParser.parse_input(self.command)
                executer = getattr(commands, self.command)
                executer().execute(self)

            except:
                print "The command is either invalid or not supported yet"
            self.set_last_command()
            self.push_to_history()
