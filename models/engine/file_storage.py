#!/usr/bin/python3

"""
File storage class for serialization and
deserialization of files and objects
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review

class FileStorage:
    """
    Private attributes:
    __file_path: String- path to JSON file.
    __objects: dictionary(empty) later storing objects.
    """

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User
        }

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        """serializes __object to JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the Json file to __ojects.
        Only if the json file(__file_path) exists; otherwise do nothing.
        No exception raised if file do not exist.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    self.__objects[key] = obj_instance

