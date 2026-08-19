from enum import Enum


class CardsAttachResponse500Type0Status(str, Enum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
