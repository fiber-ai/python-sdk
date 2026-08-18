from enum import Enum


class AccountSendOtpResponse200OutputNextMethod(str, Enum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
