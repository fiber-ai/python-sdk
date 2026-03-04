from enum import Enum

class HealthCheckResponse200Status(str, Enum):
    HEALTHY = "healthy"

    def __str__(self) -> str:
        return str(self.value)
