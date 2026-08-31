from enum import StrEnum


class SocialMediaLookupTriggerBodyPlatformsItem(StrEnum):
    INSTAGRAM = "INSTAGRAM"
    TWITTER = "TWITTER"

    def __str__(self) -> str:
        return str(self.value)
