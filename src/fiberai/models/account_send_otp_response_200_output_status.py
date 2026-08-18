from enum import Enum


class AccountSendOtpResponse200OutputStatus(str, Enum):
    OTP_SENT = "otp_sent"

    def __str__(self) -> str:
        return str(self.value)
