from abc import ABC
from abc import abstractmethod


class AbstractUserRepository(ABC):
    @abstractmethod
    def insert(self, user_payload): ...

    @abstractmethod
    def update(self, user_payload): ...

    @abstractmethod
    def get_by_id(self, user_id): ...

    @abstractmethod
    def delete(self, user_id): ...

    @abstractmethod
    def list(self): ...
