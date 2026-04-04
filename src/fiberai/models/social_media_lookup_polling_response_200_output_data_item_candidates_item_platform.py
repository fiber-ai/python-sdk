from enum import Enum


class SocialMediaLookupPollingResponse200OutputDataItemCandidatesItemPlatform(str, Enum):
    ASK_FM = "ASK_FM"
    BLUESKY = "BLUESKY"
    DISCORD = "DISCORD"
    FACEBOOK = "FACEBOOK"
    INSTAGRAM = "INSTAGRAM"
    LINKEDIN = "LINKEDIN"
    MEDIUM = "MEDIUM"
    OTHER = "OTHER"
    PINTEREST = "PINTEREST"
    STEAM = "STEAM"
    THREADS = "THREADS"
    TIKTOK = "TIKTOK"
    TRIPADVISOR = "TRIPADVISOR"
    TWITCH = "TWITCH"
    TWITTER = "TWITTER"
    YELP = "YELP"
    YOUTUBE = "YOUTUBE"

    def __str__(self) -> str:
        return str(self.value)
