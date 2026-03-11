from enum import Enum


class CreateAudienceBodyCreationMethodType2Type1(str, Enum):
    NORMAL = "NORMAL"
    START_FROM_PROSPECTS = "START_FROM_PROSPECTS"

    def __str__(self) -> str:
        return str(self.value)
