from enum import StrEnum


class AccountVerifyOtpResponse200OutputStatus(StrEnum):
    CREATED = "created"

    def __str__(self) -> str:
        return str(self.value)
