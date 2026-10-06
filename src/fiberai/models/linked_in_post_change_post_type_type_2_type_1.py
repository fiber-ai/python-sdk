from enum import StrEnum


class LinkedInPostChangePostTypeType2Type1(StrEnum):
    ORIGINAL = "original"
    REPOST = "repost"
    REPOST_WITH_COMMENTARY = "repost_with_commentary"

    def __str__(self) -> str:
        return str(self.value)
