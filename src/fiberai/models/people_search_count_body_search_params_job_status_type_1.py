from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.people_search_count_body_search_params_job_status_type_1_status import PeopleSearchCountBodySearchParamsJobStatusType1Status
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.people_search_count_body_search_params_job_status_type_1_left_at_type_1 import PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1
  from ..models.people_search_count_body_search_params_job_status_type_1_left_at_type_0 import PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0





T = TypeVar("T", bound="PeopleSearchCountBodySearchParamsJobStatusType1")



@_attrs_define
class PeopleSearchCountBodySearchParamsJobStatusType1:
    """ 
        Attributes:
            status (PeopleSearchCountBodySearchParamsJobStatusType1Status):
            left_at (Union['PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0',
                'PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1', None, Unset]):
     """

    status: PeopleSearchCountBodySearchParamsJobStatusType1Status
    left_at: Union['PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0', 'PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.people_search_count_body_search_params_job_status_type_1_left_at_type_1 import PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1
        from ..models.people_search_count_body_search_params_job_status_type_1_left_at_type_0 import PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0
        status = self.status.value

        left_at: Union[None, Unset, dict[str, Any]]
        if isinstance(self.left_at, Unset):
            left_at = UNSET
        elif isinstance(self.left_at, PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0):
            left_at = self.left_at.to_dict()
        elif isinstance(self.left_at, PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1):
            left_at = self.left_at.to_dict()
        else:
            left_at = self.left_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })
        if left_at is not UNSET:
            field_dict["leftAt"] = left_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_search_count_body_search_params_job_status_type_1_left_at_type_1 import PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1
        from ..models.people_search_count_body_search_params_job_status_type_1_left_at_type_0 import PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0
        d = dict(src_dict)
        status = PeopleSearchCountBodySearchParamsJobStatusType1Status(d.pop("status"))




        def _parse_left_at(data: object) -> Union['PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0', 'PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_at_type_0 = PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0.from_dict(data)



                return left_at_type_0
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                left_at_type_1 = PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1.from_dict(data)



                return left_at_type_1
            except: # noqa: E722
                pass
            return cast(Union['PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType0', 'PeopleSearchCountBodySearchParamsJobStatusType1LeftAtType1', None, Unset], data)

        left_at = _parse_left_at(d.pop("leftAt", UNSET))


        people_search_count_body_search_params_job_status_type_1 = cls(
            status=status,
            left_at=left_at,
        )


        people_search_count_body_search_params_job_status_type_1.additional_properties = d
        return people_search_count_body_search_params_job_status_type_1

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
