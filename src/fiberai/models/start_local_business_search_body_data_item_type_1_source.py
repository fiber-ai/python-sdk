from enum import Enum


class StartLocalBusinessSearchBodyDataItemType1Source(str, Enum):
    GOOGLE_MAPS = "google-maps"

    def __str__(self) -> str:
        return str(self.value)
