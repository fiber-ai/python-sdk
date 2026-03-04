from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="KitchenSinkCompanyResponse200OutputDataItemEmployeeCountConsensusType0")



@_attrs_define
class KitchenSinkCompanyResponse200OutputDataItemEmployeeCountConsensusType0:
    """ 
        Attributes:
            gte (Union[None, Unset, float]):
            lte (Union[None, Unset, float]):
     """

    gte: Union[None, Unset, float] = UNSET
    lte: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        gte: Union[None, Unset, float]
        if isinstance(self.gte, Unset):
            gte = UNSET
        else:
            gte = self.gte

        lte: Union[None, Unset, float]
        if isinstance(self.lte, Unset):
            lte = UNSET
        else:
            lte = self.lte


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gte is not UNSET:
            field_dict["gte"] = gte
        if lte is not UNSET:
            field_dict["lte"] = lte

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_gte(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        gte = _parse_gte(d.pop("gte", UNSET))


        def _parse_lte(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lte = _parse_lte(d.pop("lte", UNSET))


        kitchen_sink_company_response_200_output_data_item_employee_count_consensus_type_0 = cls(
            gte=gte,
            lte=lte,
        )


        kitchen_sink_company_response_200_output_data_item_employee_count_consensus_type_0.additional_properties = d
        return kitchen_sink_company_response_200_output_data_item_employee_count_consensus_type_0

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
