from enum import StrEnum


class GetTalentFlowBodyRenderImageType0Format(StrEnum):
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
