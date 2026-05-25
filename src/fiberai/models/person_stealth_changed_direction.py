from enum import Enum


class PersonStealthChangedDirection(str, Enum):
    EITHER = "either"
    ENTERED = "entered"
    EXITED = "exited"

    def __str__(self) -> str:
        return str(self.value)
