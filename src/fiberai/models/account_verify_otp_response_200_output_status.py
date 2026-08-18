from enum import Enum


class AccountVerifyOtpResponse200OutputStatus(str, Enum):
    CREATED = "created"

    def __str__(self) -> str:
        return str(self.value)
