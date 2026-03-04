from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_saved_search_run_status_response_200_output_run_status import GetSavedSearchRunStatusResponse200OutputRunStatus
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.get_saved_search_run_status_response_200_output_run_people_stats import GetSavedSearchRunStatusResponse200OutputRunPeopleStats
  from ..models.get_saved_search_run_status_response_200_output_run_companies_stats import GetSavedSearchRunStatusResponse200OutputRunCompaniesStats





T = TypeVar("T", bound="GetSavedSearchRunStatusResponse200OutputRun")



@_attrs_define
class GetSavedSearchRunStatusResponse200OutputRun:
    """ The saved search run details

        Attributes:
            id (str): The ID of the saved search run
            status (GetSavedSearchRunStatusResponse200OutputRunStatus): The status of the saved search run
            companies_stats (GetSavedSearchRunStatusResponse200OutputRunCompaniesStats): The companies stats. This includes
                the number of companies joined, departed, stayed, and returned so far.
            people_stats (GetSavedSearchRunStatusResponse200OutputRunPeopleStats): The people stats. This includes the
                number of people joined, departed, stayed, and returned so far.
            started_at (Union[None, Unset, str]): The date and time the run started (if started)
            completed_at (Union[None, Unset, str]): The date and time the run completed (if completed)
     """

    id: str
    status: GetSavedSearchRunStatusResponse200OutputRunStatus
    companies_stats: 'GetSavedSearchRunStatusResponse200OutputRunCompaniesStats'
    people_stats: 'GetSavedSearchRunStatusResponse200OutputRunPeopleStats'
    started_at: Union[None, Unset, str] = UNSET
    completed_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_saved_search_run_status_response_200_output_run_people_stats import GetSavedSearchRunStatusResponse200OutputRunPeopleStats
        from ..models.get_saved_search_run_status_response_200_output_run_companies_stats import GetSavedSearchRunStatusResponse200OutputRunCompaniesStats
        id = self.id

        status = self.status.value

        companies_stats = self.companies_stats.to_dict()

        people_stats = self.people_stats.to_dict()

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
            "companiesStats": companies_stats,
            "peopleStats": people_stats,
        })
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_saved_search_run_status_response_200_output_run_people_stats import GetSavedSearchRunStatusResponse200OutputRunPeopleStats
        from ..models.get_saved_search_run_status_response_200_output_run_companies_stats import GetSavedSearchRunStatusResponse200OutputRunCompaniesStats
        d = dict(src_dict)
        id = d.pop("id")

        status = GetSavedSearchRunStatusResponse200OutputRunStatus(d.pop("status"))




        companies_stats = GetSavedSearchRunStatusResponse200OutputRunCompaniesStats.from_dict(d.pop("companiesStats"))




        people_stats = GetSavedSearchRunStatusResponse200OutputRunPeopleStats.from_dict(d.pop("peopleStats"))




        def _parse_started_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))


        def _parse_completed_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        get_saved_search_run_status_response_200_output_run = cls(
            id=id,
            status=status,
            companies_stats=companies_stats,
            people_stats=people_stats,
            started_at=started_at,
            completed_at=completed_at,
        )


        get_saved_search_run_status_response_200_output_run.additional_properties = d
        return get_saved_search_run_status_response_200_output_run

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
