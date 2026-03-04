from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1_strategy import CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1Strategy
from typing import cast






T = TypeVar("T", bound="CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1")



@_attrs_define
class CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1:
    """ 
        Attributes:
            strategy (CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1Strategy):
            batches (list[str]):
     """

    strategy: CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1Strategy
    batches: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        batches = self.batches




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "strategy": strategy,
            "batches": batches,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy = CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1Strategy(d.pop("strategy"))




        batches = cast(list[str], d.pop("batches"))


        company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1 = cls(
            strategy=strategy,
            batches=batches,
        )


        company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1.additional_properties = d
        return company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1

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
