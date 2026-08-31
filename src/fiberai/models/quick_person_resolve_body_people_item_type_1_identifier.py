from enum import StrEnum


class QuickPersonResolveBodyPeopleItemType1Identifier(StrEnum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
