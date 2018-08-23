class InputParser():

    @staticmethod
    def parse_input(command):
        data = []
        split_commands = []
        options=[]
        if command and len(command.split()) > 1:
            split_commands = command.split()
            main_command = split_commands[0]
            split_commands = split_commands[1:]
            for option in split_commands:
                if option[0] == '-':
                    options.append(option)
                else:
                    data.append(option)
        else:
            main_command = command
        return main_command, data, split_commands
