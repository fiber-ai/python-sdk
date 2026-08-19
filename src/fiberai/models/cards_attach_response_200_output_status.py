from enum import Enum


class CardsAttachResponse200OutputStatus(str, Enum):
    ATTACHED = "attached"

    def __str__(self) -> str:
        return str(self.value)
