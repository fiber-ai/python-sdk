from enum import StrEnum


class AccountSendOtpBodyPurpose(StrEnum):
    AGENT_API = "agent-api"
    SLUSHIE = "slushie"

    def __str__(self) -> str:
        return str(self.value)
