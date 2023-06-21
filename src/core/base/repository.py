
from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def add(self, entity):
        """Add an entity to the repository."""
        raise NotImplementedError("add method must be defined in a concrete implementation")

    @abstractmethod
    def get(self, id):
        """Get an entity by its ID."""
        raise NotImplementedError("get method must be defined in a concrete implementation")

    @abstractmethod
    def update(self, entity):
        """Update an entity in the repository."""
        raise NotImplementedError("update method must be defined in a concrete implementation")

    @abstractmethod
    def delete(self, id):
        """Delete an entity from the repository by its ID."""
        raise NotImplementedError("delete method must be defined in a concrete implementation")
