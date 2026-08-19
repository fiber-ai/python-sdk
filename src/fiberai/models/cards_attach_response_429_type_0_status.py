from enum import Enum


class CardsAttachResponse429Type0Status(str, Enum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
