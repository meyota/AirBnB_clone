#!/usr/bin/python3
"""Module containing the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class represents the command interpreter of this project."""

    prompt = '(hbnb) '

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Executes some actions when the command line is empty.
        """
        return False

    def do_EOF(self, line):
        """Quit command to exit the program"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
