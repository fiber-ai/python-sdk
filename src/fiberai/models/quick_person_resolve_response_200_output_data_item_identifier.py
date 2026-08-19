from enum import Enum


class QuickPersonResolveResponse200OutputDataItemIdentifier(str, Enum):
    ENTITYURN = "entityUrn"
    LINKEDINSLUG = "linkedinSlug"
    LINKEDINURL = "linkedinUrl"
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
