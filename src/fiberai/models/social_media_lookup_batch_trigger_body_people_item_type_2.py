from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.social_media_lookup_batch_trigger_body_people_item_type_2_input_type import (
    SocialMediaLookupBatchTriggerBodyPeopleItemType2InputType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialMediaLookupBatchTriggerBodyPeopleItemType2")


@_attrs_define
class SocialMediaLookupBatchTriggerBodyPeopleItemType2:
    """
    Attributes:
        input_type (SocialMediaLookupBatchTriggerBodyPeopleItemType2InputType):
        full_name (str): The full name of the person to look up.
        customer_provided_id (None | str | Unset): Your external ID for this person, echoed back in the response for
            joining results to your dataset.
        company (None | str | Unset): Current company, used to disambiguate common names.
        job_title (None | str | Unset): Current job title.
        work_email (None | str | Unset): Work email address.
        linkedin_url (None | str | Unset): LinkedIn profile URL for additional context (e.g.
            https://www.linkedin.com/in/karpathy).
    """

    input_type: SocialMediaLookupBatchTriggerBodyPeopleItemType2InputType
    full_name: str
    customer_provided_id: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    job_title: None | str | Unset = UNSET
    work_email: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_type = self.input_type.value

        full_name = self.full_name

        customer_provided_id: None | str | Unset
        if isinstance(self.customer_provided_id, Unset):
            customer_provided_id = UNSET
        else:
            customer_provided_id = self.customer_provided_id

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        job_title: None | str | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        else:
            job_title = self.job_title

        work_email: None | str | Unset
        if isinstance(self.work_email, Unset):
            work_email = UNSET
        else:
            work_email = self.work_email

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputType": input_type,
                "fullName": full_name,
            }
        )
        if customer_provided_id is not UNSET:
            field_dict["customerProvidedId"] = customer_provided_id
        if company is not UNSET:
            field_dict["company"] = company
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if work_email is not UNSET:
            field_dict["workEmail"] = work_email
        if linkedin_url is not UNSET:
            field_dict["linkedinUrl"] = linkedin_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_type = SocialMediaLookupBatchTriggerBodyPeopleItemType2InputType(d.pop("inputType"))

        full_name = d.pop("fullName")

        def _parse_customer_provided_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_provided_id = _parse_customer_provided_id(d.pop("customerProvidedId", UNSET))

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_work_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_email = _parse_work_email(d.pop("workEmail", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl", UNSET))

        social_media_lookup_batch_trigger_body_people_item_type_2 = cls(
            input_type=input_type,
            full_name=full_name,
            customer_provided_id=customer_provided_id,
            company=company,
            job_title=job_title,
            work_email=work_email,
            linkedin_url=linkedin_url,
        )

        social_media_lookup_batch_trigger_body_people_item_type_2.additional_properties = d
        return social_media_lookup_batch_trigger_body_people_item_type_2

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
