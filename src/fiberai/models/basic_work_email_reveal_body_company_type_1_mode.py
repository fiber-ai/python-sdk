from enum import StrEnum


class BasicWorkEmailRevealBodyCompanyType1Mode(StrEnum):
    IDENTIFIER = "identifier"

    def __str__(self) -> str:
        return str(self.value)
