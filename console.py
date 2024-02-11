#!/usr/bin/python3
import cmd
#import re
#from shlex import split
#from models import storage
#from models.base_model import BaseModel
#from models.user import User
#from models.state import State
#from models.city import City
#from models.place import Place
#from models.amenity import Amenity
#from models.review import Review

class HBNBCommand(cmd.Cmd):
    """This class is the Base class that inherits from the Cmd class."""
    prompt = "(hbnb)"
    def __init__(self):
        """Initializing using the magic method"""
        super().__init__()

    def do_quit(self, line):
        """This method exits the Command line loop"""
        return True
    def do_EOF(self, line):
        print()
        """Exits the command interpreter"""
        return True
    def help(self):
        """Displays documentation of the commands and the commands"""
        return True
    def emptyline(self):
        """Returns an empty line when enter is pressed"""



if __name__ == "__main__":
    HBNBCommand().cmdloop()

