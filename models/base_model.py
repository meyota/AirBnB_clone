#!usr/bin/python3
"""BaseModel class."""
import models
from datetime import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """initialize BaseModel class"""
        # public instance attributes
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # public instance methods
    def __str__(self):
        """return string repr of instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return my_dict
