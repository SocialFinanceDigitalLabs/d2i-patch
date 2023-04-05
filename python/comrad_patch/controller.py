from abc import ABC, abstractmethod
from .components import Component
from typing import Optional


class Controller:
    def __init__(self, previous: Optional[str] = None, next: Optional[str] = None):
        self.__next = next
        self.__previous = previous

    @property
    def next(self):
        return self.__next

    @property
    def previous(self):
        return self.__previous

    def export(self) -> dict:
        """returns a dict representation of the controller"""
        return {"next": self.__next, "previous": self.__previous}
