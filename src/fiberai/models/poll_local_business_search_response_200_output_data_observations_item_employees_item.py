from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_email_address_type_0 import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0,
    )
    from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_phone_number_type_0 import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0,
    )
    from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_social_media_links_item import (
        PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemSocialMediaLinksItem,
    )


T = TypeVar("T", bound="PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem")


@_attrs_define
class PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItem:
    """
    Attributes:
        name (str):
        social_media_links
            (list[PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemSocialMediaLinksItem]):
        role (None | str | Unset):
        other_info (Any | Unset):
        email_address (None | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0
            | Unset):
        phone_number (None | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0 |
            Unset):
    """

    name: str
    social_media_links: list[
        PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemSocialMediaLinksItem
    ]
    role: None | str | Unset = UNSET
    other_info: Any | Unset = UNSET
    email_address: (
        None | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0 | Unset
    ) = UNSET
    phone_number: (
        None | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_email_address_type_0 import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_phone_number_type_0 import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0,
        )

        name = self.name

        social_media_links = []
        for social_media_links_item_data in self.social_media_links:
            social_media_links_item = social_media_links_item_data.to_dict()
            social_media_links.append(social_media_links_item)

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        other_info = self.other_info

        email_address: dict[str, Any] | None | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        elif isinstance(
            self.email_address,
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0,
        ):
            email_address = self.email_address.to_dict()
        else:
            email_address = self.email_address

        phone_number: dict[str, Any] | None | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        elif isinstance(
            self.phone_number, PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0
        ):
            phone_number = self.phone_number.to_dict()
        else:
            phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "socialMediaLinks": social_media_links,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if other_info is not UNSET:
            field_dict["otherInfo"] = other_info
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_email_address_type_0 import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_phone_number_type_0 import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0,
        )
        from ..models.poll_local_business_search_response_200_output_data_observations_item_employees_item_social_media_links_item import (
            PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemSocialMediaLinksItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        social_media_links = []
        _social_media_links = d.pop("socialMediaLinks")
        for social_media_links_item_data in _social_media_links:
            social_media_links_item = (
                PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemSocialMediaLinksItem.from_dict(
                    social_media_links_item_data
                )
            )

            social_media_links.append(social_media_links_item)

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        other_info = d.pop("otherInfo", UNSET)

        def _parse_email_address(
            data: object,
        ) -> None | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                email_address_type_0 = PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0.from_dict(
                    data
                )

                return email_address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemEmailAddressType0
                | Unset,
                data,
            )

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_phone_number(
            data: object,
        ) -> None | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_0 = (
                    PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0.from_dict(
                        data
                    )
                )

                return phone_number_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PollLocalBusinessSearchResponse200OutputDataObservationsItemEmployeesItemPhoneNumberType0
                | Unset,
                data,
            )

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

        poll_local_business_search_response_200_output_data_observations_item_employees_item = cls(
            name=name,
            social_media_links=social_media_links,
            role=role,
            other_info=other_info,
            email_address=email_address,
            phone_number=phone_number,
        )

        poll_local_business_search_response_200_output_data_observations_item_employees_item.additional_properties = d
        return poll_local_business_search_response_200_output_data_observations_item_employees_item

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
