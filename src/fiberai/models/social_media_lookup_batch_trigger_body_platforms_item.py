from enum import StrEnum


class SocialMediaLookupBatchTriggerBodyPlatformsItem(StrEnum):
    INSTAGRAM = "INSTAGRAM"
    TWITTER = "TWITTER"

    def __str__(self) -> str:
        return str(self.value)
