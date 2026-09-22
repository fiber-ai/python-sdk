from enum import StrEnum


class LiteContactRevealBodyCompanyType1Identifier(StrEnum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
