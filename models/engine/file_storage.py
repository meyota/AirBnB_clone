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
=======
#!/usr/bin/python3
"""File system engin module"""
import os
from json import JSONDecoder, JSONEncoder
from importlib import import_module

class FileStorage:
   """
   serializes instances to a JSON file and deserializes JSON file to instances
   """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance."""
        self.model_classes = {
                'BaseModel': import_module('models.base_model').BaseModel,
                'User': import_module('models.user').User,
                'State': import_module('models.state').State,
                'City': import_module('models.city').City,
                'Amenity': import_module('models.amenity').Amenity,
                'Place': import_module('models.place').Place,
                'Review': import_module('models.review').Review

                }

        def all(self):
            """Returns dictionary representation"""
            return FileStorage.__objects

        def new(self, obj):
            """sets __objects the obj with key"""
            dict_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[dict_key] = obj

        def save(self):
            """serializes __objects to the JSON file"""

            with open(FileStorage.__file_path, mode='w') as file:
                json_format = {}
                for key, value in FileStorage.__objects.items():

                    json_format[key] = value.to_dict()
                file.write(JSONEncoder().encode(json_format))

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON file exists
        """
        if os.path.isfile(self.__file_path):
            file_lines = []
            with open(self.__file_path, mode='r') as file:
                file_lines = file.readlines()
            file_txt = ''.join(file_lines) if len(file_lines) > 0 else '{}'
            json_objs = JSONDecoder().decode(file_txt)
            base_model_objs = dict()
            classes = self.model_classes
            for key, value in json_objs.items():
                class_name = value['__class__']
                if class_name in classes.keys():
                  base_model_objs[key] = classes[class_name](**value)
           self.__objects = base_models_objs
>>>>>>> 77e688d2c7c9f950a709428abf09467bba745af5
