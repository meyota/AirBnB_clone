#!usr/bin/python3
"""Define BaseModel class"""
import json
from  models.base_model import BaseModel


class FileStorage:
    # private instance attributes
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_copy = FileStorage.__objects
        objects_dict = {
            obj: objects_copy[obj].to_dict() for obj in objects_copy.keys()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f)

            my_dict = {}
            for obj_name, obj_details in objects_dict.items():
                class_name = obj_name.split(".")[0]
                obj = eval(class_name)(**obj_details)
                my_dict[obj_name] = obj

            FileStorage.__objects = my_dict
        except FileNotFoundError:
            pass
