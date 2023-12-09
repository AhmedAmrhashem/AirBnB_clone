#!/usr/bin/python3
"""The Main Base Model"""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel():
    """The main Class that other classes will inherit from"""

    def __init__(self, *args, **kwargs):
        """The Constructor of BaseModel
        .........................
        args:
            ...
            self -> instance
            args -> variable number of variable in tuple
            kwargs -> key word argument to get dict
        """

        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """To String Method"""

        return "[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the time"""

        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Changes an Object to a dictonarie"""

        Updated_dict = self.__dict__.copy()
        Updated_dict["__class__"] = self.__class__.__name__
        Updated_dict["created_at"] = self.created_at.isoformat()
        Updated_dict["updated_at"] = self.updated.at.isoformat()

        return (Updated_dict)
