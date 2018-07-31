class InputParser():

    @staticmethod
    def parse_input(command):
        if command and len(command) > 1:
            split_commands = command.split()
            main_command = split_commands[0]
            return main_command, split_commands[1:]
        else:
            return command, []
