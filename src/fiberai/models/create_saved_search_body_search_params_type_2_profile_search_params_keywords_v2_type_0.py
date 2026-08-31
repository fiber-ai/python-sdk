from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0_operator import (
    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0_clauses_item import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0ClausesItem,
    )
    from ..models.create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0_options_type_0 import (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0")


@_attrs_define
class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0:
    """
    Attributes:
        clauses (list[CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0ClausesItem]):
        operator (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator | Unset):  Default:
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator.AND.
        options (CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0 | None | Unset):
    """

    clauses: list[CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0ClausesItem]
    operator: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator | Unset = (
        CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator.AND
    )
    options: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0_options_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0,  # noqa: PLC0415
        )

        clauses = []
        for clauses_item_data in self.clauses:
            clauses_item = clauses_item_data.to_dict()
            clauses.append(clauses_item)

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(
            self.options, CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0
        ):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clauses": clauses,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0_clauses_item import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0ClausesItem,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0_options_type_0 import (
            CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        clauses = []
        _clauses = d.pop("clauses")
        for clauses_item_data in _clauses:
            clauses_item = (
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0ClausesItem.from_dict(
                    clauses_item_data
                )
            )

            clauses.append(clauses_item)

        _operator = d.pop("operator", UNSET)
        operator: CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0Operator(_operator)

        def _parse_options(
            data: object,
        ) -> CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = (
                    CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0.from_dict(data)
                )

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType2ProfileSearchParamsKeywordsV2Type0OptionsType0 | None | Unset,
                data,
            )

        options = _parse_options(d.pop("options", UNSET))

        create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0 = cls(
            clauses=clauses,
            operator=operator,
            options=options,
        )

        create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_2_profile_search_params_keywords_v2_type_0

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
