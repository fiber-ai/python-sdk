from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0
  from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_lte_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0





T = TypeVar("T", bound="JobPostingSearchResponse200OutputDataItemCompensationRangeType0")



@_attrs_define
class JobPostingSearchResponse200OutputDataItemCompensationRangeType0:
    """ Structured compensation range with currency and period

        Attributes:
            lte (Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0', None, Unset]):
            gte (Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0', None, Unset]):
     """

    lte: Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0', None, Unset] = UNSET
    gte: Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_lte_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0
        lte: Union[None, Unset, dict[str, Any]]
        if isinstance(self.lte, Unset):
            lte = UNSET
        elif isinstance(self.lte, JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0):
            lte = self.lte.to_dict()
        else:
            lte = self.lte

        gte: Union[None, Unset, dict[str, Any]]
        if isinstance(self.gte, Unset):
            gte = UNSET
        elif isinstance(self.gte, JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0):
            gte = self.gte.to_dict()
        else:
            gte = self.gte


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if lte is not UNSET:
            field_dict["lte"] = lte
        if gte is not UNSET:
            field_dict["gte"] = gte

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_gte_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0
        from ..models.job_posting_search_response_200_output_data_item_compensation_range_type_0_lte_type_0 import JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0
        d = dict(src_dict)
        def _parse_lte(data: object) -> Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lte_type_0 = JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0.from_dict(data)



                return lte_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0', None, Unset], data)

        lte = _parse_lte(d.pop("lte", UNSET))


        def _parse_gte(data: object) -> Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gte_type_0 = JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0.from_dict(data)



                return gte_type_0
            except: # noqa: E722
                pass
            return cast(Union['JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0', None, Unset], data)

        gte = _parse_gte(d.pop("gte", UNSET))


        job_posting_search_response_200_output_data_item_compensation_range_type_0 = cls(
            lte=lte,
            gte=gte,
        )


        job_posting_search_response_200_output_data_item_compensation_range_type_0.additional_properties = d
        return job_posting_search_response_200_output_data_item_compensation_range_type_0

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
