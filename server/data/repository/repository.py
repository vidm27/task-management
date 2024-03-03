from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def get(self, **filters):
        NotImplemented

    @abstractmethod
    def list(self):
        NotImplemented

    @abstractmethod
    def add(self, **kwargs: object):
        NotImplemented

    @abstractmethod
    def delete(self, identifier: str, **kwargs: object):
        NotImplemented

    @abstractmethod
    def update(self, identifier: str, **kwargs: object):
        NotImplemented
