from enum import StrEnum


class AccountSendOtpResponse200OutputNextMethod(StrEnum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
