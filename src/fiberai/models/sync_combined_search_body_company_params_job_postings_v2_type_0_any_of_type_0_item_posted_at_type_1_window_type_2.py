from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_2_method import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Method
from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_2_period import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Period
from ..models.sync_combined_search_body_company_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_2_which import SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Which






T = TypeVar("T", bound="SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2")



@_attrs_define
class SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2:
    """ 
        Attributes:
            method (SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Method):
            which (SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Which):
            period (SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Period):
     """

    method: SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Method
    which: SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Which
    period: SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Period
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        which = self.which.value

        period = self.period.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method": method,
            "which": which,
            "period": period,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Method(d.pop("method"))




        which = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Which(d.pop("which"))




        period = SyncCombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Period(d.pop("period"))




        sync_combined_search_body_company_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_2 = cls(
            method=method,
            which=which,
            period=period,
        )


        sync_combined_search_body_company_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_2.additional_properties = d
        return sync_combined_search_body_company_params_job_postings_v2_type_0_any_of_type_0_item_posted_at_type_1_window_type_2

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
