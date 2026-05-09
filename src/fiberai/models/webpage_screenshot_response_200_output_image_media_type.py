from enum import Enum


class WebpageScreenshotResponse200OutputImageMediaType(str, Enum):
    IMAGEPNG = "image/png"

    def __str__(self) -> str:
        return str(self.value)
