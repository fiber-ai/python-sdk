from enum import StrEnum


class GoogleMapsPlaceResponse200ChargeInfoType2Method(StrEnum):
    CHARGED_FOR_ASYNC_PROCESS = "charged-for-async-process"

    def __str__(self) -> str:
        return str(self.value)
