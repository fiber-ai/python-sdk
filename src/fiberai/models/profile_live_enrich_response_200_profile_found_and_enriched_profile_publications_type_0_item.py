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
  from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile_publications_type_0_item_collaborators_type_0_item import ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item





T = TypeVar("T", bound="ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0Item")



@_attrs_define
class ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0Item:
    """ 
        Attributes:
            collaborators (Union[None, Unset,
                list['ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item']]):
            date (Union[None, Unset, str]):
            id (Union[None, Unset, str]):
            publisher (Union[None, Unset, str]):
            summary (Union[None, Unset, str]):
            title (Union[None, Unset, str]):
            url (Union[None, Unset, str]):
     """

    collaborators: Union[None, Unset, list['ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item']] = UNSET
    date: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    publisher: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile_publications_type_0_item_collaborators_type_0_item import ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item
        collaborators: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.collaborators, Unset):
            collaborators = UNSET
        elif isinstance(self.collaborators, list):
            collaborators = []
            for collaborators_type_0_item_data in self.collaborators:
                collaborators_type_0_item = collaborators_type_0_item_data.to_dict()
                collaborators.append(collaborators_type_0_item)


        else:
            collaborators = self.collaborators

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        publisher: Union[None, Unset, str]
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_live_enrich_response_200_profile_found_and_enriched_profile_publications_type_0_item_collaborators_type_0_item import ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item
        d = dict(src_dict)
        def _parse_collaborators(data: object) -> Union[None, Unset, list['ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collaborators_type_0 = []
                _collaborators_type_0 = data
                for collaborators_type_0_item_data in (_collaborators_type_0):
                    collaborators_type_0_item = ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item.from_dict(collaborators_type_0_item_data)



                    collaborators_type_0.append(collaborators_type_0_item)

                return collaborators_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfilePublicationsType0ItemCollaboratorsType0Item']], data)

        collaborators = _parse_collaborators(d.pop("collaborators", UNSET))


        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_publisher(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))


        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))


        profile_live_enrich_response_200_profile_found_and_enriched_profile_publications_type_0_item = cls(
            collaborators=collaborators,
            date=date,
            id=id,
            publisher=publisher,
            summary=summary,
            title=title,
            url=url,
        )


        profile_live_enrich_response_200_profile_found_and_enriched_profile_publications_type_0_item.additional_properties = d
        return profile_live_enrich_response_200_profile_found_and_enriched_profile_publications_type_0_item

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
