from enum import StrEnum


class SocialMediaLookupBatchTriggerBodyPeopleItemType1InputType(StrEnum):
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
