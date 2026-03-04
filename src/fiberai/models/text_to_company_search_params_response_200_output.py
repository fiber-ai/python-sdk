from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.text_to_company_search_params_response_200_output_search_params import TextToCompanySearchParamsResponse200OutputSearchParams





T = TypeVar("T", bound="TextToCompanySearchParamsResponse200Output")



@_attrs_define
class TextToCompanySearchParamsResponse200Output:
    """ 
        Attributes:
            search_params (TextToCompanySearchParamsResponse200OutputSearchParams):
     """

    search_params: 'TextToCompanySearchParamsResponse200OutputSearchParams'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_company_search_params_response_200_output_search_params import TextToCompanySearchParamsResponse200OutputSearchParams
        search_params = self.search_params.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "searchParams": search_params,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_company_search_params_response_200_output_search_params import TextToCompanySearchParamsResponse200OutputSearchParams
        d = dict(src_dict)
        search_params = TextToCompanySearchParamsResponse200OutputSearchParams.from_dict(d.pop("searchParams"))




        text_to_company_search_params_response_200_output = cls(
            search_params=search_params,
        )


        text_to_company_search_params_response_200_output.additional_properties = d
        return text_to_company_search_params_response_200_output

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
