from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item_functions_type_1 import TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1
from ..models.text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item_functions_type_2_type_1 import TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1
from ..models.text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item_functions_type_3_type_1 import TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item_changes_type_0_item import TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item





T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0Item")



@_attrs_define
class TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0Item:
    """ 
        Attributes:
            functions (Union[None,
                TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1,
                TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1,
                TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1, Unset]):
            current_count (Union[None, Unset, float]):
            changes (Union[None, Unset,
                list['TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item']]):
     """

    functions: Union[None, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1, Unset] = UNSET
    current_count: Union[None, Unset, float] = UNSET
    changes: Union[None, Unset, list['TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item_changes_type_0_item import TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item
        functions: Union[None, Unset, str]
        if isinstance(self.functions, Unset):
            functions = UNSET
        elif isinstance(self.functions, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1):
            functions = self.functions.value
        elif isinstance(self.functions, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1):
            functions = self.functions.value
        elif isinstance(self.functions, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1):
            functions = self.functions.value
        else:
            functions = self.functions

        current_count: Union[None, Unset, float]
        if isinstance(self.current_count, Unset):
            current_count = UNSET
        else:
            current_count = self.current_count

        changes: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.to_dict()
                changes.append(changes_type_0_item)


        else:
            changes = self.changes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if functions is not UNSET:
            field_dict["functions"] = functions
        if current_count is not UNSET:
            field_dict["current_count"] = current_count
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item_changes_type_0_item import TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item
        d = dict(src_dict)
        def _parse_functions(data: object) -> Union[None, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functions_type_1 = TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1(data)



                return functions_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functions_type_2_type_1 = TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1(data)



                return functions_type_2_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functions_type_3_type_1 = TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1(data)



                return functions_type_3_type_1
            except: # noqa: E722
                pass
            return cast(Union[None, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType1, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType2Type1, TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemFunctionsType3Type1, Unset], data)

        functions = _parse_functions(d.pop("functions", UNSET))


        def _parse_current_count(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        current_count = _parse_current_count(d.pop("current_count", UNSET))


        def _parse_changes(data: object) -> Union[None, Unset, list['TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in (_changes_type_0):
                    changes_type_0_item = TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item.from_dict(changes_type_0_item_data)



                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['TextToCombinedSearchResponse200OutputDataCompaniesItemEmployeeTrendsType0ItemChangesType0Item']], data)

        changes = _parse_changes(d.pop("changes", UNSET))


        text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item = cls(
            functions=functions,
            current_count=current_count,
            changes=changes,
        )


        text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item.additional_properties = d
        return text_to_combined_search_response_200_output_data_companies_item_employee_trends_type_0_item

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
