from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.check_google_maps_results_response_200_output_status import CheckGoogleMapsResultsResponse200OutputStatus






T = TypeVar("T", bound="CheckGoogleMapsResultsResponse200Output")



@_attrs_define
class CheckGoogleMapsResultsResponse200Output:
    """ 
        Attributes:
            status (CheckGoogleMapsResultsResponse200OutputStatus):
            total_places_found (int): The total number of places found
            total_places_requested (int): The total number of places requested
            percentage_completed (float): The percentage of places found
     """

    status: CheckGoogleMapsResultsResponse200OutputStatus
    total_places_found: int
    total_places_requested: int
    percentage_completed: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        total_places_found = self.total_places_found

        total_places_requested = self.total_places_requested

        percentage_completed = self.percentage_completed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "totalPlacesFound": total_places_found,
            "totalPlacesRequested": total_places_requested,
            "percentageCompleted": percentage_completed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = CheckGoogleMapsResultsResponse200OutputStatus(d.pop("status"))




        total_places_found = d.pop("totalPlacesFound")

        total_places_requested = d.pop("totalPlacesRequested")

        percentage_completed = d.pop("percentageCompleted")

        check_google_maps_results_response_200_output = cls(
            status=status,
            total_places_found=total_places_found,
            total_places_requested=total_places_requested,
            percentage_completed=percentage_completed,
        )


        check_google_maps_results_response_200_output.additional_properties = d
        return check_google_maps_results_response_200_output

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
