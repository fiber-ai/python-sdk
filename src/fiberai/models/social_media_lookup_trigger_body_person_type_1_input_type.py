from enum import Enum


class SocialMediaLookupTriggerBodyPersonType1InputType(str, Enum):
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
