from enum import StrEnum


class QuickPersonResolveBodyPeopleItemType3Identifier(StrEnum):
    ENTITYURN = "entityUrn"

    def __str__(self) -> str:
        return str(self.value)
