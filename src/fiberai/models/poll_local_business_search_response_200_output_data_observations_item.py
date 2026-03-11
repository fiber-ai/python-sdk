from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_local_business_search_response_200_output_data_observations_item_business_emails_item import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem,
    )
    from ..models.poll_local_business_search_response_200_output_data_observations_item_business_phones_item import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem,
    )
    from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem,
    )
    from ..models.poll_local_business_search_response_200_output_data_observations_item_local_business import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness,
    )
    from ..models.poll_local_business_search_response_200_output_data_observations_item_social_media_links_item import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem,
    )


T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItem")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItem:
    """
    Attributes:
        research_run_id (str):
        website_urls (list[str]):
        local_business (PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness):
        business_emails (list[PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem]):
        business_phones (list[PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem]):
        social_media_links (list[PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem]):
        employees (list[PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem]):
        rationale (Any | Unset):
    """

    research_run_id: str
    website_urls: list[str]
    local_business: PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness
    business_emails: list[PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem]
    business_phones: list[PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem]
    social_media_links: list[PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem]
    employees: list[PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem]
    rationale: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        research_run_id = self.research_run_id

        website_urls = self.website_urls

        local_business = self.local_business.to_dict()

        business_emails = []
        for business_emails_item_data in self.business_emails:
            business_emails_item = business_emails_item_data.to_dict()
            business_emails.append(business_emails_item)

        business_phones = []
        for business_phones_item_data in self.business_phones:
            business_phones_item = business_phones_item_data.to_dict()
            business_phones.append(business_phones_item)

        social_media_links = []
        for social_media_links_item_data in self.social_media_links:
            social_media_links_item = social_media_links_item_data.to_dict()
            social_media_links.append(social_media_links_item)

        employees = []
        for employees_item_data in self.employees:
            employees_item = employees_item_data.to_dict()
            employees.append(employees_item)

        rationale = self.rationale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "researchRunId": research_run_id,
                "websiteUrls": website_urls,
                "localBusiness": local_business,
                "businessEmails": business_emails,
                "businessPhones": business_phones,
                "socialMediaLinks": social_media_links,
                "employees": employees,
            }
        )
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_local_business_search_response_200_output_data_observations_item_business_emails_item import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_business_phones_item import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_local_business import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_social_media_links_item import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem,
        )

        d = dict(src_dict)
        research_run_id = d.pop("researchRunId")

        website_urls = cast(list[str], d.pop("websiteUrls"))

        local_business = PollLocalBusinessSearchResponse200OutputDataObservationsItemLocalBusiness.from_dict(
            d.pop("localBusiness")
        )

        business_emails = []
        _business_emails = d.pop("businessEmails")
        for business_emails_item_data in _business_emails:
            business_emails_item = (
                PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessEmailsItem.from_dict(
                    business_emails_item_data
                )
            )

            business_emails.append(business_emails_item)

        business_phones = []
        _business_phones = d.pop("businessPhones")
        for business_phones_item_data in _business_phones:
            business_phones_item = (
                PollLocalBusinessSearchResponse200OutputDataObservationsItemBusinessPhonesItem.from_dict(
                    business_phones_item_data
                )
            )

            business_phones.append(business_phones_item)

        social_media_links = []
        _social_media_links = d.pop("socialMediaLinks")
        for social_media_links_item_data in _social_media_links:
            social_media_links_item = (
                PollLocalBusinessSearchResponse200OutputDataObservationsItemSocialMediaLinksItem.from_dict(
                    social_media_links_item_data
                )
            )

            social_media_links.append(social_media_links_item)

        employees = []
        _employees = d.pop("employees")
        for employees_item_data in _employees:
            employees_item = PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem.from_dict(
                employees_item_data
            )

            employees.append(employees_item)

        rationale = d.pop("rationale", UNSET)

        poll_local_business_search_response_200_output_data_observations_item = cls(
            research_run_id=research_run_id,
            website_urls=website_urls,
            local_business=local_business,
            business_emails=business_emails,
            business_phones=business_phones,
            social_media_links=social_media_links,
            employees=employees,
            rationale=rationale,
        )

        poll_local_business_search_response_200_output_data_observations_item.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item

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
