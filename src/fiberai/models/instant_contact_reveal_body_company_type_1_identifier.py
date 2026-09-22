from enum import StrEnum


class InstantContactRevealBodyCompanyType1Identifier(StrEnum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
