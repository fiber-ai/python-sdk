from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_1_method import CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Method
from ..models.company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_1_period import CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Period
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1")



@_attrs_define
class CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1:
    """ 
        Attributes:
            method (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Method):
            period (CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Period):
            lower_bound (Union[None, Unset, float]):
            upper_bound (Union[None, Unset, float]):
     """

    method: CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Method
    period: CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Period
    lower_bound: Union[None, Unset, float] = UNSET
    upper_bound: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        period = self.period.value

        lower_bound: Union[None, Unset, float]
        if isinstance(self.lower_bound, Unset):
            lower_bound = UNSET
        else:
            lower_bound = self.lower_bound

        upper_bound: Union[None, Unset, float]
        if isinstance(self.upper_bound, Unset):
            upper_bound = UNSET
        else:
            upper_bound = self.upper_bound


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "period": period,
        })
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Method(d.pop("method"))




        period = CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType1Period(d.pop("period"))




        def _parse_lower_bound(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lower_bound = _parse_lower_bound(d.pop("lowerBound", UNSET))


        def _parse_upper_bound(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        upper_bound = _parse_upper_bound(d.pop("upperBound", UNSET))


        company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_1 = cls(
            method=method,
            period=period,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )


        company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_1.additional_properties = d
        return company_search_body_search_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_1

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
