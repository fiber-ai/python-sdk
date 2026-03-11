from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.people_search_response_200_output_data_item_publications_type_0_item_collaborators_type_0_item import (
        PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item,
    )


T = TypeVar("T", bound="PeopleSearchResponse200OutputDataItemPublicationsType0Item")


@_attrs_define
class PeopleSearchResponse200OutputDataItemPublicationsType0Item:
    """
    Attributes:
        collaborators (list[PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item] | None |
            Unset):
        date (None | str | Unset):
        id (None | str | Unset):
        publisher (None | str | Unset):
        summary (None | str | Unset):
        title (None | str | Unset):
        url (None | str | Unset):
    """

    collaborators: (
        list[PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item] | None | Unset
    ) = UNSET
    date: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    publisher: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators: list[dict[str, Any]] | None | Unset
        if isinstance(self.collaborators, Unset):
            collaborators = UNSET
        elif isinstance(self.collaborators, list):
            collaborators = []
            for collaborators_type_0_item_data in self.collaborators:
                collaborators_type_0_item = collaborators_type_0_item_data.to_dict()
                collaborators.append(collaborators_type_0_item)

        else:
            collaborators = self.collaborators

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        from ..models.people_search_response_200_output_data_item_publications_type_0_item_collaborators_type_0_item import (
            PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item,
        )

        d = dict(src_dict)

        def _parse_collaborators(
            data: object,
        ) -> list[PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collaborators_type_0 = []
                _collaborators_type_0 = data
                for collaborators_type_0_item_data in _collaborators_type_0:
                    collaborators_type_0_item = (
                        PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item.from_dict(
                            collaborators_type_0_item_data
                        )
                    )

                    collaborators_type_0.append(collaborators_type_0_item)

                return collaborators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[PeopleSearchResponse200OutputDataItemPublicationsType0ItemCollaboratorsType0Item] | None | Unset,
                data,
            )

        collaborators = _parse_collaborators(d.pop("collaborators", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        people_search_response_200_output_data_item_publications_type_0_item = cls(
            collaborators=collaborators,
            date=date,
            id=id,
            publisher=publisher,
            summary=summary,
            title=title,
            url=url,
        )

        people_search_response_200_output_data_item_publications_type_0_item.additional_properties = d
        return people_search_response_200_output_data_item_publications_type_0_item

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
