import json
import os

from collections import defaultdict

class DB:
    def __init__(self, db_loc:str=None, autoload:bool=False) -> None:
        self._cache = defaultdict(dict)
        self.db_loc = db_loc

        if autoload:
            self.load_db_from_file(db_loc)

    # Load Database from file
    def load_db_from_file(self, file_name:str=None):
        if not file_name:
            file_name = self.db_loc

        # Check whether file exists or not-- if it doesn't, create it
        if not os.path.isfile(file_name):
            with open(file_name, 'w') as file:
                file.write('')
        
        # Read data from file to cache
        with open(file_name, 'r') as file:
            data = json.load(file)

            self._cache = data

    # Store Cache to Database
    def save_db_to_file(self, file_name:str=None):
        if not file_name:
            file_name = self.db_loc
        
        # Write data from cache to file
        with open(file_name, 'w') as file:
            json.dump(self._cache, file, indent=4)
    
    # Set value in cache
    def set(self, name: str, value: any) -> None:
        self._cache[name] = value

    # Update value in cache
    def update(self, name: str, value: dict) -> None:
        self._cache[name].update(value)

    # Get value from cache
    def get(self, name: str) -> any:
        return self._cache[name]
