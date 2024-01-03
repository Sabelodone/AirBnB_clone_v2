#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        
        Args:
            cls (class, optional): If specified, filters the result to include
                only objects of the specified class.
        
        Returns:
            dict: A dictionary containing objects in storage.
        """
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls and issubclass(cls, BaseModel):
                cls_dict = {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
                return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file."""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    try:
                        class_name = val['__class__']
                        if class_name in classes:
                            self.all()[key] = classes[class_name](**val)
                    except KeyError:
                        # Handle missing '__class__' attribute gracefully
                        print(f"Warning: Missing '__class__' attribute for {key}")
                    except Exception as e:
                        # Handle other exceptions gracefully
                        print(f"Error loading object {key}: {e}")
        except FileNotFoundError:
            # Handle file not found exception
            pass
        except json.decoder.JSONDecodeError:
            # Handle JSON decode error
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside - if obj is equal to None,
        the method should not do anything
        """
        if obj is None:
            return
        obj_to_del = f"{obj.__class__.__name__}.{obj.id}"
        try:
            del FileStorage.__objects[obj_to_del]
        except AttributeError:
            pass
        except KeyboardInterrupt:
            pass

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
