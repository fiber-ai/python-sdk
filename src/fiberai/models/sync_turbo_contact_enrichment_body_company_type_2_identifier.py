from enum import StrEnum


class SyncTurboContactEnrichmentBodyCompanyType2Identifier(StrEnum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
