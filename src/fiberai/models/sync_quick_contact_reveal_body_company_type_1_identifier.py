from enum import StrEnum


class SyncQuickContactRevealBodyCompanyType1Identifier(StrEnum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
