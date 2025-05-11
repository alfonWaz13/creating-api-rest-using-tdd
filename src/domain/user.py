from dataclasses import dataclass


@dataclass
class User:
    id: str
    name: str
    age: int

    def to_dict(self) -> dict:
        return self.__dict__
