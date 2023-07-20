"""
Abstract class with DB CRUD abstract methods
"""
from abc import ABC, abstractmethod

from db.db_connection import get_db_connection


class CrudABC(ABC):

    def __init__(self):
        self.connection = get_db_connection()

    @abstractmethod
    def create(self, entry_to_create):
        pass

    @abstractmethod
    def read(self, id=None):
        pass

    @abstractmethod
    def update(self, entry_for_update):
        pass

    @abstractmethod
    def delete(self, id):
        pass
