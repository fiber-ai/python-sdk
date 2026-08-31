from enum import StrEnum


class AccountSendOtpResponse200OutputNextPath(StrEnum):
    VALUE_0 = "/v1/account/verify-otp"

    def __str__(self) -> str:
        return str(self.value)
