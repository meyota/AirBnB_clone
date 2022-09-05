#!/usr/bin/python3
"""Module containing the entry point of the command interpreter."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

avaliable_classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity, 'City': City, 'State': State,'Place': Place, 'Review': Review}

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

    def do_create(self, arg):
        """Creates a new instance.
        """
        args = arg.split()
        if not check_classname(args):
            return

    new_obj = avaliable_classes[args[0]]()
    new_obj.save()
    print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = arg.split()
        if not check_classname(args, id=True):
            return

    instance_objs = storage.all()
    key = "{}.{}".format(args[0], args[1])
    req_instance = instance_objs.get(key, None)
    if req_instance is None:
        print("** no instance found **")
        return
    print(req_instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not check_classname(args, id=True):
            return
    instance_objs = storage.all()
    key = "{}.{}".format(args[0], args[1])
    req_instance = instance_objs.get(key, None)
    if req_instance is None:
        print("** no instance found **")
        return

        del instance_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances.
        """
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in avaliable_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg: str):
        """Updates an instance based on the class name and id.
        """
        args = arg.split()
        if not check_classname(args, id=True):
            return
        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        setattr(req_instance, args[2], args[3])
        req_instance.save()


    def check_classname(args, id=False):
        """Runs checks on args to validate classname entry.
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in avaliable_classes.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and id:
            print("** instance id missing **")
            return False
        return True


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
