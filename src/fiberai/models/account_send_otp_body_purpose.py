from enum import Enum


class AccountSendOtpBodyPurpose(str, Enum):
    AGENT_API = "agent-api"
    SLUSHIE = "slushie"

    def __str__(self) -> str:
        return str(self.value)
