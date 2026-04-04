from enum import Enum


class SocialMediaLookupTriggerBodyPlatformsItem(str, Enum):
    INSTAGRAM = "INSTAGRAM"
    TWITTER = "TWITTER"

    def __str__(self) -> str:
        return str(self.value)
