class InputParser():

    @staticmethod
    def parse_input(command):
        data = ''
        split_commands = []
        if command and len(command) > 1:
            split_commands = command.split()
            if split_commands[1][0] == '-':
                main_command = split_commands[0]
                split_commands = split_commands[1:]
            else :
                main_command = split_commands[0]
                data = split_commands[1]
                split_commands=split_commands[2:]
        else:
            main_command = command
        return main_command, data, []
