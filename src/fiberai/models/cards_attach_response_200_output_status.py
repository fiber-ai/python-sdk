from enum import StrEnum


class CardsAttachResponse200OutputStatus(StrEnum):
    ATTACHED = "attached"

    def __str__(self) -> str:
        return str(self.value)
