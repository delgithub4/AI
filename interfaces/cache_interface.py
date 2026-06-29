from abc import ABC, abstractmethod


class CacheInterface(ABC):

    @abstractmethod
    def get(self, key):
        ...

    @abstractmethod
    def set(
        self,
        key,
        value,
    ):
        ...

    @abstractmethod
    def clear(self):
        ...
