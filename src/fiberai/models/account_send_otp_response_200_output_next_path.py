from enum import Enum


class AccountSendOtpResponse200OutputNextPath(str, Enum):
    VALUE_0 = "/v1/account/verify-otp"

    def __str__(self) -> str:
        return str(self.value)
