from enum import StrEnum


class CardsAttachResponse409Status(StrEnum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
