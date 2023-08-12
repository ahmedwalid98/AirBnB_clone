#!/usr/bin/python3
"""
    Storage class Module.
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    Custom class for file storage
    """

    __file_path = '../AirBnB_clone/file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
        Returns dictionary representation of all objects
        """
        return FileStorage.__objects

    def new(self, object):
        """sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write

        """
        key = "{}.{}".format(type(object).__name__, object.id)
        FileStorage.__objects[key] = object

    def save(self):
        """
        serializes __objects to the JSON file
        (path: __file_path)
        """

        with open(FileStorage.__file_path, 'w+') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
