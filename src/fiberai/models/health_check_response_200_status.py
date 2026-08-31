from enum import StrEnum


class HealthCheckResponse200Status(StrEnum):
    HEALTHY = "healthy"

    def __str__(self) -> str:
        return str(self.value)
