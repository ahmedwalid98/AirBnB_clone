#!/usr/bin/python3
"""
    Base class Module.
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Base calss representation

    Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
    """

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    continue
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a Human readable string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of an instance."""
        my_objects = {}

        for key, value in self.__dict__.items():
            if key == 'created_at' or key == "updated_at":
                my_objects.update({key: value.isoformat()})
            else:
                my_objects.update({key: value})

        my_objects.update({'__class__': self.__class__.__name__})
        return my_objects
