#!/usr/bin/python3
"""Module for the Custom command line for project"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    Class representing console for the project
    """
    prompt = '(hbnb) '
    cls_names = [
        "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
        ]

    def do_create(self, class_name):
        """
        Creates a new instance of Class name,
        saves it (to the JSON file) and prints the id
        """
        if (class_name == '' or class_name is None):
            print("** class name missing **")

        else:
            if class_name in self.cls_names:
                new_model = eval(class_name)()
                new_model.save()
                print(new_model.id)

            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Method that Prints the string representation of an instance
        based on the class name and id
        """
        if (line == '' or line is None):
            print("** class name missing **")
        else:
            commands = line.split(' ')
            if commands[0] not in self.cls_names:
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")

            else:
                objs = storage.all()
                key = "{}.{}".format(commands[0], commands[1])
                try:
                    print(objs[key])
                except KeyError:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        Method that destroys an instance based on the class name and id
        """
        if (line == '' or line is None):
            print("** class name missing **")
        else:
            commands = line.split(' ')
            if commands[0] not in self.cls_names:
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")

            else:
                key = "{}.{}".format(commands[0], commands[1])
                try:
                    del storage.all()[key]
                    storage.save()
                except KeyError:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Method that Prints all string representation of all instances
        based or not on the class name
        """
        commands = line.split(' ')
        if commands[0] in self.cls_names or commands[0] == '':
            objs = storage.all()
            print([str(obj) for obj in objs.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Method that Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON
        """
        commands = line.split(' ')

        if (line == '' or line is None):
            print("** class name missing **")
        else:
            if commands[0] not in self.cls_names:
                print("** class doesn't exist **")

            elif not self.is_valid_id(commands[1]):
                print("** instance id missing **")

            elif "{}.{}".format(commands[0], commands[1]) not in storage.all():
                print("** no instance found **")

            elif len(commands) < 3:
                print("** attribute name missing **")

            elif len(commands) < 4:
                print("** value missing **")

            else:
                key = "{}.{}".format(commands[0], commands[1])
                obj = storage.all()[key]
                value = commands[3].replace('"', '')
                attrs = obj.__class__.__dict__.keys()
                cast_type = self.get_type(obj, attrs, commands[2])

                try:
                    value = cast_type(value)
                except ValueError:
                    pass
                setattr(storage.all()[key], commands[2], value)
                storage.all()[key].save()

    def is_valid_id(self, id):
        """Helper method to validate uuid"""
        import uuid
        try:
            uuid.UUID(str(id))
            return True
        except ValueError:
            return False

    def get_type(self, value, attrs, attr):
        """Helper to get type of an attribute"""
        import re
        if attr in attrs:
            cast_type = type(value.__class__.__dict__[attr])
        elif re.match(r"^\d+$", value):
            cast_type = int
        elif re.match(r"^\d+\.\d+$", value):
            cast_type = float

        return cast_type

    def do_EOF(self, line):
        """
        Method to exit the console
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Doesn't do anything on empty line + ENTER.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
