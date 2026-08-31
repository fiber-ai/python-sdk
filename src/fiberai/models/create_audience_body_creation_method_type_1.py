from enum import StrEnum


class CreateAudienceBodyCreationMethodType1(StrEnum):
    NORMAL = "NORMAL"
    START_FROM_PROSPECTS = "START_FROM_PROSPECTS"

    def __str__(self) -> str:
        return str(self.value)
