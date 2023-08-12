#!/usr/bin/python3
"""Defines Console Module."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


def handle_error(line, args_number):
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Place",
               "Amenity",
               "Review"]
    errors = ["** class name missing **",
              "** class doesn't exist **",
              "** instance id missing **",
              "** no instance found **",
              "** attribute name missing **",
              "** value missing **"]

    if not line:
        print(errors[0])
        return 1

    args = line.split(" ")
    if args_number >= 1 and args[0] not in classes:
        print(errors[1])
        return 1
    elif args_number == 1:
        return 0

    if args_number >= 2 and len(args) < 2:
        print(errors[2])
        return 1

    data = storage.all()
    for i in range(len(args)):
        if args[i][0] == '"':
            args[i] = args[i].replace('"', "")

    key = args[0] + '.' + args[1]
    if args_number >= 2 and key not in data:
        print(errors[3])
        return 1
    elif args_number == 2:
        return 0

    if args_number >= 4 and len(args) < 3:
        print(errors[4])
        return 1
    elif len(args) < 4:
        print(errors[5])
    elif args_number == 4:
        obj = data.get(key)
        setattr(obj, args[2], parse_str(args[3]))
        storage.save()
        return 0

def parse_str(str):
    if is_int(str):
        return int(str)
    elif is_float(str):
        return float(str)
    else:
        return str

def is_int(num):
    try:
        a = float(num)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

def is_float(num):
    try:
        a = float(num)
    except (TypeError, ValueError):
        return False
    else:
        return True

class HBNBCommand(cmd.Cmd):
    """Console command interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """skip emptyline"""
        pass

    def do_quit(self, arg):
        """Quit from command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit from command interpreter."""
        return True

    def do_create(self, arg):
        """Create an instance of an object."""
        if handle_error(arg, 1) == 1:
            return
        line = arg.split()

        obj = eval(line[0])()
        storage.new(obj)
        print(obj.id)
        obj.save()

    def do_show(self, arg):
        """Show object based on the class and the id."""
        if handle_error(arg, 2) == 1:
            return
        args = arg.split(" ")
        key = args[0] + '.' + args[1]
        data = storage.all()
        print(data.get(key))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if handle_error(arg, 2) == 1:
            return
        args = arg.split()
        key = args[0] + '.' + args[1]
        data = storage.all()
        data.pop(key)
        storage.save()

    def do_all(self, arg):
        """Prints string representation of
        all instances based or not on the
        class name."""
        if arg:
            args = arg.split()
            if args[0] not in ["BaseModel",
                               "User",
                               "State",
                               "City",
                               "Place",
                               "Amenity",
                               "Review"]:
                print("** class doesn't exist **")
            else:
                all_obj = []
                for obj in storage.all().values():
                    if obj.__class__.__name__ == args[0]:
                        all_obj.append(obj.__str__())
                print(all_obj)
        else:
            all_obj = []
            for obj in storage.all().values():
                all_obj.append(obj.__str__())
            print(all_obj)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating an attribute."""
        if handle_error(arg, 4) == 1:
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
