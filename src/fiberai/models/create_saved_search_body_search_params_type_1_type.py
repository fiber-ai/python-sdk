from enum import Enum

class CreateSavedSearchBodySearchParamsType1Type(str, Enum):
    COMPANIES = "companies"

    def __str__(self) -> str:
        return str(self.value)
