from enum import StrEnum


class CompanySearchResponse200ChargeInfoType0Method(StrEnum):
    CHARGED_NOW = "charged-now"

    def __str__(self) -> str:
        return str(self.value)
