from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookalikes_single_response_200_output_company import LookalikesSingleResponse200OutputCompany
    from ..models.lookalikes_single_response_200_output_results_item import LookalikesSingleResponse200OutputResultsItem


T = TypeVar("T", bound="LookalikesSingleResponse200Output")


@_attrs_define
class LookalikesSingleResponse200Output:
    """
    Attributes:
        company (LookalikesSingleResponse200OutputCompany): The company you asked about, as we identified it.
        results (list[LookalikesSingleResponse200OutputResultsItem]): Similar companies, best first.
        notice (None | str | Unset): Present when results could not be produced right now; retrying shortly usually
            works. You are not charged for such a response.
    """

    company: LookalikesSingleResponse200OutputCompany
    results: list[LookalikesSingleResponse200OutputResultsItem]
    notice: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        notice: None | str | Unset
        if isinstance(self.notice, Unset):
            notice = UNSET
        else:
            notice = self.notice

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "results": results,
            }
        )
        if notice is not UNSET:
            field_dict["notice"] = notice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookalikes_single_response_200_output_company import LookalikesSingleResponse200OutputCompany  # noqa: PLC0415
        from ..models.lookalikes_single_response_200_output_results_item import (
            LookalikesSingleResponse200OutputResultsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        company = LookalikesSingleResponse200OutputCompany.from_dict(d.pop("company"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = LookalikesSingleResponse200OutputResultsItem.from_dict(results_item_data)

            results.append(results_item)

        def _parse_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notice = _parse_notice(d.pop("notice", UNSET))

        lookalikes_single_response_200_output = cls(
            company=company,
            results=results,
            notice=notice,
        )

        lookalikes_single_response_200_output.additional_properties = d
        return lookalikes_single_response_200_output

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
