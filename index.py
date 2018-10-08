from terminal import Terminal
import readline
import commands
import os

valid_commands = [command for command in commands.__dict__.keys()
                          if not command.startswith("__")]

# Given the query text and the current state, attempt to provide
# an autocompletion. This function will use the contents of the current
# directory as well as all valid commands as the possible results.
def completer(text, state):
    complete_corpus = valid_commands + os.listdir(".")
    options = [option for option in complete_corpus if option.startswith(text)]
    return options[state] if state < len(options) else None

def get_command():
    command = raw_input()
    return command


if __name__ == "__main__":
    print("Welcome to pylinux")

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")
    readline.parse_and_bind("bind ^I rl_complete")

    terminal = Terminal()
    terminal.play()
