from enum import StrEnum


class PersonStealthChangedDirection(StrEnum):
    EITHER = "either"
    ENTERED = "entered"
    EXITED = "exited"

    def __str__(self) -> str:
        return str(self.value)
