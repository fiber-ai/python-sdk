from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0_period import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Period
from typing import cast

if TYPE_CHECKING:
  from ..models.create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0_range import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Range





T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0")



@_attrs_define
class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0:
    """ 
        Attributes:
            range_ (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Range):
            period (CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Period):
     """

    range_: 'CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Range'
    period: CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0_range import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Range
        range_ = self.range_.to_dict()

        period = self.period.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "range": range_,
            "period": period,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0_range import CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Range
        d = dict(src_dict)
        range_ = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Range.from_dict(d.pop("range"))




        period = CreateSavedSearchBodySearchParamsType0ProfileSearchParamsStealthV2Type1StealthDurationType0Period(d.pop("period"))




        create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0 = cls(
            range_=range_,
            period=period,
        )


        create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_0_profile_search_params_stealth_v2_type_1_stealth_duration_type_0

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
