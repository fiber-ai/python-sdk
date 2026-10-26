from enum import StrEnum


class GetTalentFlowResponse200OutputGraphicType0Format(StrEnum):
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
