from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.poll_batch_live_enrich_response_200_output_results_item_status import (
    PollBatchLiveEnrichResponse200OutputResultsItemStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_batch_live_enrich_response_200_output_results_item_company_type_0 import (
        PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0,
    )
    from ..models.poll_batch_live_enrich_response_200_output_results_item_profile_type_0 import (
        PollBatchLiveEnrichResponse200OutputResultsItemProfileType0,
    )


T = TypeVar("T", bound="PollBatchLiveEnrichResponse200OutputResultsItem")


@_attrs_define
class PollBatchLiveEnrichResponse200OutputResultsItem:
    """
    Attributes:
        identifier (str): The raw identifier that was submitted.
        status (PollBatchLiveEnrichResponse200OutputResultsItemStatus): The enrichment status for this identifier.
        profile (None | PollBatchLiveEnrichResponse200OutputResultsItemProfileType0 | Unset): Enriched profile data.
            Present only when type is profile and status is COMPLETED.
        company (None | PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0 | Unset): Enriched company data.
            Present only when type is company and status is COMPLETED.
    """

    identifier: str
    status: PollBatchLiveEnrichResponse200OutputResultsItemStatus
    profile: None | PollBatchLiveEnrichResponse200OutputResultsItemProfileType0 | Unset = UNSET
    company: None | PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_batch_live_enrich_response_200_output_results_item_company_type_0 import (
            PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0,  # noqa: PLC0415
        )
        from ..models.poll_batch_live_enrich_response_200_output_results_item_profile_type_0 import (
            PollBatchLiveEnrichResponse200OutputResultsItemProfileType0,  # noqa: PLC0415
        )

        identifier = self.identifier

        status = self.status.value

        profile: dict[str, Any] | None | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, PollBatchLiveEnrichResponse200OutputResultsItemProfileType0):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        company: dict[str, Any] | None | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        elif isinstance(self.company, PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0):
            company = self.company.to_dict()
        else:
            company = self.company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "status": status,
            }
        )
        if profile is not UNSET:
            field_dict["profile"] = profile
        if company is not UNSET:
            field_dict["company"] = company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_batch_live_enrich_response_200_output_results_item_company_type_0 import (
            PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0,  # noqa: PLC0415
        )
        from ..models.poll_batch_live_enrich_response_200_output_results_item_profile_type_0 import (
            PollBatchLiveEnrichResponse200OutputResultsItemProfileType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        identifier = d.pop("identifier")

        status = PollBatchLiveEnrichResponse200OutputResultsItemStatus(d.pop("status"))

        def _parse_profile(data: object) -> None | PollBatchLiveEnrichResponse200OutputResultsItemProfileType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_0 = PollBatchLiveEnrichResponse200OutputResultsItemProfileType0.from_dict(data)

                return profile_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollBatchLiveEnrichResponse200OutputResultsItemProfileType0 | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        def _parse_company(data: object) -> None | PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PollBatchLiveEnrichResponse200OutputResultsItemCompanyType0 | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        poll_batch_live_enrich_response_200_output_results_item = cls(
            identifier=identifier,
            status=status,
            profile=profile,
            company=company,
        )

        poll_batch_live_enrich_response_200_output_results_item.additional_properties = d
        return poll_batch_live_enrich_response_200_output_results_item

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
