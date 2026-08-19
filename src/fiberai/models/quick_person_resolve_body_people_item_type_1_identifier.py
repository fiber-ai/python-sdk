from enum import Enum


class QuickPersonResolveBodyPeopleItemType1Identifier(str, Enum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
