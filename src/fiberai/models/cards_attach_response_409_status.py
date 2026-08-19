from enum import Enum


class CardsAttachResponse409Status(str, Enum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
