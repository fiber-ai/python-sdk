from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CreateCompanyExclusionListFromAudienceBody")



@_attrs_define
class CreateCompanyExclusionListFromAudienceBody:
    """ 
        Attributes:
            api_key (str): Your Fiber API key
            audience_id (str): Id of the audience to create exclusion list from
            name (Union[None, Unset, str]): Name of the company exclusion list. If not provided, defaults to 'Exclusion list
                from {audienceName}'
            is_organization_wide (Union[Unset, bool]): Is the company exclusion list organization wide Default: False.
     """

    api_key: str
    audience_id: str
    name: Union[None, Unset, str] = UNSET
    is_organization_wide: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        audience_id = self.audience_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_organization_wide = self.is_organization_wide


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
            "audienceId": audience_id,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if is_organization_wide is not UNSET:
            field_dict["isOrganizationWide"] = is_organization_wide

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        audience_id = d.pop("audienceId")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        is_organization_wide = d.pop("isOrganizationWide", UNSET)

        create_company_exclusion_list_from_audience_body = cls(
            api_key=api_key,
            audience_id=audience_id,
            name=name,
            is_organization_wide=is_organization_wide,
        )


        create_company_exclusion_list_from_audience_body.additional_properties = d
        return create_company_exclusion_list_from_audience_body

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
