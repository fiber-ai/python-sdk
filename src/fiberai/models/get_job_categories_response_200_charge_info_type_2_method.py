from enum import StrEnum


class GetJobCategoriesResponse200ChargeInfoType2Method(StrEnum):
    CHARGED_FOR_ASYNC_PROCESS = "charged-for-async-process"

    def __str__(self) -> str:
        return str(self.value)
