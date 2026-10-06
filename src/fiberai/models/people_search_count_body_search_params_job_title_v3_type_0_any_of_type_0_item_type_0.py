from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0_mode_type_1 import (
    PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1,
)
from ..models.people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0_mode_type_2_type_1 import (
    PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1,
)
from ..models.people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0_mode_type_3_type_1 import (
    PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1,
)
from ..models.people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0_type import (
    PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0Type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0")


@_attrs_define
class PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0:
    """
    Attributes:
        type_ (PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0Type):
        term (str):
        exact (bool | None | Unset):
        mode (None | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1 |
            PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1 |
            PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1 | Unset):
        stemming (bool | None | Unset):
    """

    type_: PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0Type
    term: str
    exact: bool | None | Unset = UNSET
    mode: (
        None
        | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1
        | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1
        | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1
        | Unset
    ) = UNSET
    stemming: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        term = self.term

        exact: bool | None | Unset
        if isinstance(self.exact, Unset):
            exact = UNSET
        else:
            exact = self.exact

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1):
            mode = self.mode.value
        elif isinstance(self.mode, PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1):
            mode = self.mode.value
        elif isinstance(self.mode, PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1):
            mode = self.mode.value
        else:
            mode = self.mode

        stemming: bool | None | Unset
        if isinstance(self.stemming, Unset):
            stemming = UNSET
        else:
            stemming = self.stemming

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "term": term,
            }
        )
        if exact is not UNSET:
            field_dict["exact"] = exact
        if mode is not UNSET:
            field_dict["mode"] = mode
        if stemming is not UNSET:
            field_dict["stemming"] = stemming

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0Type(d.pop("type"))

        term = d.pop("term")

        def _parse_exact(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exact = _parse_exact(d.pop("exact", UNSET))

        def _parse_mode(
            data: object,
        ) -> (
            None
            | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1
            | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1
            | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_2_type_1 = PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1(
                    data
                )

                return mode_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_3_type_1 = PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1(
                    data
                )

                return mode_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType1
                | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType2Type1
                | PeopleSearchCountBodySearchParamsJobTitleV3Type0AnyOfType0ItemType0ModeType3Type1
                | Unset,
                data,
            )

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_stemming(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        stemming = _parse_stemming(d.pop("stemming", UNSET))

        people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0 = cls(
            type_=type_,
            term=term,
            exact=exact,
            mode=mode,
            stemming=stemming,
        )

        people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0.additional_properties = d
        return people_search_count_body_search_params_job_title_v3_type_0_any_of_type_0_item_type_0

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
