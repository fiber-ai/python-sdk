from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemIdentifier(StrEnum):
    ENTITYURN = "entityUrn"
    LINKEDINSLUG = "linkedinSlug"
    LINKEDINURL = "linkedinUrl"
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
