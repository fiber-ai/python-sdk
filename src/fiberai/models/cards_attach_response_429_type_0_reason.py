from enum import StrEnum


class CardsAttachResponse429Type0Reason(StrEnum):
    ALREADY_ATTACHED = "already_attached"
    ATTACH_IN_PROGRESS = "attach_in_progress"
    BILLING_PROFILE_CONFLICT = "billing_profile_conflict"
    CARD_DECLINED = "card_declined"
    INTERNAL_ERROR = "internal_error"
    NOT_CARDLESS_TRIAL = "not_cardless_trial"
    ORG_NOT_FOUND = "org_not_found"
    PAYMENT_PROVIDER_ERROR = "payment_provider_error"
    RATE_LIMITED = "rate_limited"
    SERVICE_UNAVAILABLE = "service_unavailable"
    SPT_INVALID = "spt_invalid"
    TRIAL_ENDED = "trial_ended"

    def __str__(self) -> str:
        return str(self.value)
