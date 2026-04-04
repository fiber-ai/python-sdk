from enum import Enum


class GetCompanyRevenueResponse200ChargeInfoType3Method(str, Enum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
