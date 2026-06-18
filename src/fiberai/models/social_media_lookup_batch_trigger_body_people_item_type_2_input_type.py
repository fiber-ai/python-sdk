from enum import Enum


class SocialMediaLookupBatchTriggerBodyPeopleItemType2InputType(str, Enum):
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
