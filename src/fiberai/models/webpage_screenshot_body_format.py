from enum import Enum


class WebpageScreenshotBodyFormat(str, Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"

    def __str__(self) -> str:
        return str(self.value)
