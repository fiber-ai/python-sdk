from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_body_search_params_past_job_text_type_0_joiner import (
    PeopleSearchBodySearchParamsPastJobTextType0Joiner,
)

if TYPE_CHECKING:
    from ..models.people_search_body_search_params_past_job_text_type_0_criteria_item import (
        PeopleSearchBodySearchParamsPastJobTextType0CriteriaItem,
    )


T = TypeVar("T", bound="PeopleSearchBodySearchParamsPastJobTextType0")


@_attrs_define
class PeopleSearchBodySearchParamsPastJobTextType0:
    """
    Attributes:
        joiner (PeopleSearchBodySearchParamsPastJobTextType0Joiner):
        criteria (list[PeopleSearchBodySearchParamsPastJobTextType0CriteriaItem]):
    """

    joiner: PeopleSearchBodySearchParamsPastJobTextType0Joiner
    criteria: list[PeopleSearchBodySearchParamsPastJobTextType0CriteriaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        joiner = self.joiner.value

        criteria = []
        for criteria_item_data in self.criteria:
            criteria_item = criteria_item_data.to_dict()
            criteria.append(criteria_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "joiner": joiner,
                "criteria": criteria,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_body_search_params_past_job_text_type_0_criteria_item import (
            PeopleSearchBodySearchParamsPastJobTextType0CriteriaItem,
        )

        d = dict(src_dict)
        joiner = PeopleSearchBodySearchParamsPastJobTextType0Joiner(d.pop("joiner"))

        criteria = []
        _criteria = d.pop("criteria")
        for criteria_item_data in _criteria:
            criteria_item = PeopleSearchBodySearchParamsPastJobTextType0CriteriaItem.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        people_search_body_search_params_past_job_text_type_0 = cls(
            joiner=joiner,
            criteria=criteria,
        )

        people_search_body_search_params_past_job_text_type_0.additional_properties = d
        return people_search_body_search_params_past_job_text_type_0

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
