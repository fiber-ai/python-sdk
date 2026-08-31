from enum import StrEnum


class AccountSendOtpResponse200OutputStatus(StrEnum):
    OTP_SENT = "otp_sent"

    def __str__(self) -> str:
        return str(self.value)
