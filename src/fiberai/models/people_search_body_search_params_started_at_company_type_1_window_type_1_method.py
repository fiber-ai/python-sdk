from enum import Enum


class PeopleSearchBodySearchParamsStartedAtCompanyType1WindowType1Method(str, Enum):
    WITHIN = "within"

    def __str__(self) -> str:
        return str(self.value)
