from terminal import Terminal
import readline

def get_command():
    command = raw_input()
    return command


if __name__ == "__main__":
    print "Welcome to pylinux"
    terminal = Terminal()
    terminal.play()
