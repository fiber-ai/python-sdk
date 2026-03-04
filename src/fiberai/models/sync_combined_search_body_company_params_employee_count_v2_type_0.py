from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_1 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_2 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_3 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_4 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_5 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_6 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_7 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_lower_bound_exclusive_type_8 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_0 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_1 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_2 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_3 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_4 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_5 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_6 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_7 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7
from ..models.sync_combined_search_body_company_params_employee_count_v2_type_0_upper_bound_inclusive_type_8 import SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0:
    """ 
        Attributes:
            lower_bound_exclusive (Union[None,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8, Unset]):
            upper_bound_inclusive (Union[None,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7,
                SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8, Unset]):
     """

    lower_bound_exclusive: Union[None, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8, Unset] = UNSET
    upper_bound_inclusive: Union[None, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        lower_bound_exclusive: Union[None, Unset, int]
        if isinstance(self.lower_bound_exclusive, Unset):
            lower_bound_exclusive = UNSET
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(self.lower_bound_exclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        else:
            lower_bound_exclusive = self.lower_bound_exclusive

        upper_bound_inclusive: Union[None, Unset, int]
        if isinstance(self.upper_bound_inclusive, Unset):
            upper_bound_inclusive = UNSET
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(self.upper_bound_inclusive, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        else:
            upper_bound_inclusive = self.upper_bound_inclusive


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if lower_bound_exclusive is not UNSET:
            field_dict["lowerBoundExclusive"] = lower_bound_exclusive
        if upper_bound_inclusive is not UNSET:
            field_dict["upperBoundInclusive"] = upper_bound_inclusive

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_lower_bound_exclusive(data: object) -> Union[None, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_0 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0(data)



                return lower_bound_exclusive_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_1 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1(data)



                return lower_bound_exclusive_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_2 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2(data)



                return lower_bound_exclusive_type_2
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_3 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3(data)



                return lower_bound_exclusive_type_3
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_4 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4(data)



                return lower_bound_exclusive_type_4
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_5 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5(data)



                return lower_bound_exclusive_type_5
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_6 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6(data)



                return lower_bound_exclusive_type_6
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_7 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7(data)



                return lower_bound_exclusive_type_7
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_8 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8(data)



                return lower_bound_exclusive_type_8
            except: # noqa: E722
                pass
            return cast(Union[None, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType0, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType1, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType3, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType4, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType5, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType6, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType7, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0LowerBoundExclusiveType8, Unset], data)

        lower_bound_exclusive = _parse_lower_bound_exclusive(d.pop("lowerBoundExclusive", UNSET))


        def _parse_upper_bound_inclusive(data: object) -> Union[None, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_0 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0(data)



                return upper_bound_inclusive_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_1 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1(data)



                return upper_bound_inclusive_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_2 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2(data)



                return upper_bound_inclusive_type_2
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_3 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3(data)



                return upper_bound_inclusive_type_3
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_4 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4(data)



                return upper_bound_inclusive_type_4
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_5 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5(data)



                return upper_bound_inclusive_type_5
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_6 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6(data)



                return upper_bound_inclusive_type_6
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_7 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7(data)



                return upper_bound_inclusive_type_7
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_8 = SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8(data)



                return upper_bound_inclusive_type_8
            except: # noqa: E722
                pass
            return cast(Union[None, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType0, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType1, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType2, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType3, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType4, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType5, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType6, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType7, SyncCombinedSearchBodyCompanyParamsEmployeeCountV2Type0UpperBoundInclusiveType8, Unset], data)

        upper_bound_inclusive = _parse_upper_bound_inclusive(d.pop("upperBoundInclusive", UNSET))


        sync_combined_search_body_company_params_employee_count_v2_type_0 = cls(
            lower_bound_exclusive=lower_bound_exclusive,
            upper_bound_inclusive=upper_bound_inclusive,
        )


        sync_combined_search_body_company_params_employee_count_v2_type_0.additional_properties = d
        return sync_combined_search_body_company_params_employee_count_v2_type_0

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
