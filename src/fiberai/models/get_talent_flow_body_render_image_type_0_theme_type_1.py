from enum import StrEnum


class GetTalentFlowBodyRenderImageType0ThemeType1(StrEnum):
    DEFAULT = "default"
    FOREST = "forest"
    MONO = "mono"
    OCEAN = "ocean"
    SUNSET = "sunset"

    def __str__(self) -> str:
        return str(self.value)
