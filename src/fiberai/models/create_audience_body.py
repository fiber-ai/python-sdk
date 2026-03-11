from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_audience_body_creation_method_type_1 import CreateAudienceBodyCreationMethodType1
from ..models.create_audience_body_creation_method_type_2_type_1 import CreateAudienceBodyCreationMethodType2Type1
from ..models.create_audience_body_creation_method_type_3_type_1 import CreateAudienceBodyCreationMethodType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAudienceBody")


@_attrs_define
class CreateAudienceBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        name (str): Name for the audience (e.g., 'Fintech VPs in NYC')
        creation_method (CreateAudienceBodyCreationMethodType1 | CreateAudienceBodyCreationMethodType2Type1 |
            CreateAudienceBodyCreationMethodType3Type1 | None | Unset): How the audience will be created. NORMAL: search
            companies then prospects. START_FROM_PROSPECTS: search prospects only. Default:
            CreateAudienceBodyCreationMethodType1.NORMAL.
    """

    api_key: str
    name: str
    creation_method: (
        CreateAudienceBodyCreationMethodType1
        | CreateAudienceBodyCreationMethodType2Type1
        | CreateAudienceBodyCreationMethodType3Type1
        | None
        | Unset
    ) = CreateAudienceBodyCreationMethodType1.NORMAL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        name = self.name

        creation_method: None | str | Unset
        if isinstance(self.creation_method, Unset):
            creation_method = UNSET
        elif isinstance(self.creation_method, CreateAudienceBodyCreationMethodType1):
            creation_method = self.creation_method.value
        elif isinstance(self.creation_method, CreateAudienceBodyCreationMethodType2Type1):
            creation_method = self.creation_method.value
        elif isinstance(self.creation_method, CreateAudienceBodyCreationMethodType3Type1):
            creation_method = self.creation_method.value
        else:
            creation_method = self.creation_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "name": name,
            }
        )
        if creation_method is not UNSET:
            field_dict["creationMethod"] = creation_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        name = d.pop("name")

        def _parse_creation_method(
            data: object,
        ) -> (
            CreateAudienceBodyCreationMethodType1
            | CreateAudienceBodyCreationMethodType2Type1
            | CreateAudienceBodyCreationMethodType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_method_type_1 = CreateAudienceBodyCreationMethodType1(data)

                return creation_method_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_method_type_2_type_1 = CreateAudienceBodyCreationMethodType2Type1(data)

                return creation_method_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_method_type_3_type_1 = CreateAudienceBodyCreationMethodType3Type1(data)

                return creation_method_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateAudienceBodyCreationMethodType1
                | CreateAudienceBodyCreationMethodType2Type1
                | CreateAudienceBodyCreationMethodType3Type1
                | None
                | Unset,
                data,
            )

        creation_method = _parse_creation_method(d.pop("creationMethod", UNSET))

        create_audience_body = cls(
            api_key=api_key,
            name=name,
            creation_method=creation_method,
        )

        create_audience_body.additional_properties = d
        return create_audience_body

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
