from enum import StrEnum


class CardsAttachResponse404Status(StrEnum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
