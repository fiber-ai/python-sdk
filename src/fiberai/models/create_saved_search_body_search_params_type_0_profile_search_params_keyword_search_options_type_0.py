from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_0_profile_search_params_keyword_search_options_type_0_fields_to_search_over_type_0 import (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0")


@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0:
    """
    Attributes:
        fields_to_search_over
            (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0 |
            None | Unset):
    """

    fields_to_search_over: (
        CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_keyword_search_options_type_0_fields_to_search_over_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0,
        )

        fields_to_search_over: dict[str, Any] | None | Unset
        if isinstance(self.fields_to_search_over, Unset):
            fields_to_search_over = UNSET
        elif isinstance(
            self.fields_to_search_over,
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0,
        ):
            fields_to_search_over = self.fields_to_search_over.to_dict()
        else:
            fields_to_search_over = self.fields_to_search_over

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields_to_search_over is not UNSET:
            field_dict["fieldsToSearchOver"] = fields_to_search_over

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_keyword_search_options_type_0_fields_to_search_over_type_0 import (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0,
        )

        d = dict(src_dict)

        def _parse_fields_to_search_over(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_to_search_over_type_0 = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0.from_dict(
                    data
                )

                return fields_to_search_over_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordSearchOptionsType0FieldsToSearchOverType0
                | None
                | Unset,
                data,
            )

        fields_to_search_over = _parse_fields_to_search_over(d.pop("fieldsToSearchOver", UNSET))

        create_saved_search_body_search_params_type_0_profile_search_params_keyword_search_options_type_0 = cls(
            fields_to_search_over=fields_to_search_over,
        )

        create_saved_search_body_search_params_type_0_profile_search_params_keyword_search_options_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_keyword_search_options_type_0

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
