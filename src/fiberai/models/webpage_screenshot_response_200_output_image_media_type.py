from enum import StrEnum


class WebpageScreenshotResponse200OutputImageMediaType(StrEnum):
    IMAGEPNG = "image/png"

    def __str__(self) -> str:
        return str(self.value)
