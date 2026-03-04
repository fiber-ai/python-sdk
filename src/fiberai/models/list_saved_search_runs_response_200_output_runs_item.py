from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_saved_search_runs_response_200_output_runs_item_execution_mode import ListSavedSearchRunsResponse200OutputRunsItemExecutionMode
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ListSavedSearchRunsResponse200OutputRunsItem")



@_attrs_define
class ListSavedSearchRunsResponse200OutputRunsItem:
    """ 
        Attributes:
            id (str): The ID of the saved search run
            status (str): The status of the saved search run
            execution_mode (ListSavedSearchRunsResponse200OutputRunsItemExecutionMode): The execution mode of the saved
                search run. How the saved search run was triggered ("spawned"): automatically via the saved search's frequency,
                or manually through your team's actions
            started_at (Union[None, Unset, str]): The date and time the saved search run started
            completed_at (Union[None, Unset, str]): The date and time the saved search run completed (if completed)
     """

    id: str
    status: str
    execution_mode: ListSavedSearchRunsResponse200OutputRunsItemExecutionMode
    started_at: Union[None, Unset, str] = UNSET
    completed_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        execution_mode = self.execution_mode.value

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
            "executionMode": execution_mode,
        })
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        execution_mode = ListSavedSearchRunsResponse200OutputRunsItemExecutionMode(d.pop("executionMode"))




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


        list_saved_search_runs_response_200_output_runs_item = cls(
            id=id,
            status=status,
            execution_mode=execution_mode,
            started_at=started_at,
            completed_at=completed_at,
        )


        list_saved_search_runs_response_200_output_runs_item.additional_properties = d
        return list_saved_search_runs_response_200_output_runs_item

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
