from enum import Enum


class UpdateApiKeyLimitBodyOperation(str, Enum):
    DECREASE = "decrease"
    DIVIDE = "divide"
    INCREASE = "increase"
    MULTIPLY = "multiply"
    REMOVE = "remove"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
