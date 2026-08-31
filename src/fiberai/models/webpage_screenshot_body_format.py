from enum import StrEnum


class WebpageScreenshotBodyFormat(StrEnum):
    DESKTOP = "desktop"
    MOBILE = "mobile"

    def __str__(self) -> str:
        return str(self.value)
