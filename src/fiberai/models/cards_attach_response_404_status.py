from enum import Enum


class CardsAttachResponse404Status(str, Enum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
