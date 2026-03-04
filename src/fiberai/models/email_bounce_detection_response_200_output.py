from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.email_bounce_detection_response_200_output_verdict import EmailBounceDetectionResponse200OutputVerdict






T = TypeVar("T", bound="EmailBounceDetectionResponse200Output")



@_attrs_define
class EmailBounceDetectionResponse200Output:
    """ 
        Attributes:
            email (str): The email to validate
            is_catch_all (bool): If true, is a catch-all email address
            is_role_based (bool): If true, is like 'sales@' or 'hello@' instead of an actual person's email
            is_disposable (bool): If true, uses a disposable email provider like temp-mail.org
            is_consumer (bool): If true, uses a public email service like Gmail, Outlook, or Protonmail, rather than a
                commercial service like Google Workspace
            email_provider (str): The email provider
            verdict (EmailBounceDetectionResponse200OutputVerdict): Our AI's final estimate of whether the email is likely
                to be correct and deliverable
            deliverability_score (int): The deliverability score out of 100; higher scores are better
     """

    email: str
    is_catch_all: bool
    is_role_based: bool
    is_disposable: bool
    is_consumer: bool
    email_provider: str
    verdict: EmailBounceDetectionResponse200OutputVerdict
    deliverability_score: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        is_catch_all = self.is_catch_all

        is_role_based = self.is_role_based

        is_disposable = self.is_disposable

        is_consumer = self.is_consumer

        email_provider = self.email_provider

        verdict = self.verdict.value

        deliverability_score = self.deliverability_score


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
            "is_catch_all": is_catch_all,
            "is_role_based": is_role_based,
            "is_disposable": is_disposable,
            "is_consumer": is_consumer,
            "email_provider": email_provider,
            "verdict": verdict,
            "deliverability_score": deliverability_score,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        is_catch_all = d.pop("is_catch_all")

        is_role_based = d.pop("is_role_based")

        is_disposable = d.pop("is_disposable")

        is_consumer = d.pop("is_consumer")

        email_provider = d.pop("email_provider")

        verdict = EmailBounceDetectionResponse200OutputVerdict(d.pop("verdict"))




        deliverability_score = d.pop("deliverability_score")

        email_bounce_detection_response_200_output = cls(
            email=email,
            is_catch_all=is_catch_all,
            is_role_based=is_role_based,
            is_disposable=is_disposable,
            is_consumer=is_consumer,
            email_provider=email_provider,
            verdict=verdict,
            deliverability_score=deliverability_score,
        )


        email_bounce_detection_response_200_output.additional_properties = d
        return email_bounce_detection_response_200_output

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
