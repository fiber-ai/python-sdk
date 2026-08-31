from enum import StrEnum


class CardsAttachResponse400Type0Status(StrEnum):
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
