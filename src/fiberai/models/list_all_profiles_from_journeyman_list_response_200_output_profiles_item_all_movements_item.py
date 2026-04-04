from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_all_profiles_from_journeyman_list_response_200_output_profiles_item_all_movements_item_movement import (
    ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItemMovement,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem")


@_attrs_define
class ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItem:
    """
    Attributes:
        discovered_at (str):
        movement (ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItemMovement):
        new_company_name (None | str | Unset):
        new_company_logo_url (None | str | Unset):
        new_company_org_id (None | str | Unset):
        new_company_li_slug (None | str | Unset):
        new_company_domain (None | str | Unset):
        new_job_title (None | str | Unset):
        old_company_name (None | str | Unset):
        old_company_logo_url (None | str | Unset):
        old_company_org_id (None | str | Unset):
        old_company_li_slug (None | str | Unset):
        old_company_domain (None | str | Unset):
        old_job_title (None | str | Unset):
        started_in_role_at (None | str | Unset):
        started_at_company_at (None | str | Unset):
    """

    discovered_at: str
    movement: ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItemMovement
    new_company_name: None | str | Unset = UNSET
    new_company_logo_url: None | str | Unset = UNSET
    new_company_org_id: None | str | Unset = UNSET
    new_company_li_slug: None | str | Unset = UNSET
    new_company_domain: None | str | Unset = UNSET
    new_job_title: None | str | Unset = UNSET
    old_company_name: None | str | Unset = UNSET
    old_company_logo_url: None | str | Unset = UNSET
    old_company_org_id: None | str | Unset = UNSET
    old_company_li_slug: None | str | Unset = UNSET
    old_company_domain: None | str | Unset = UNSET
    old_job_title: None | str | Unset = UNSET
    started_in_role_at: None | str | Unset = UNSET
    started_at_company_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discovered_at = self.discovered_at

        movement = self.movement.value

        new_company_name: None | str | Unset
        if isinstance(self.new_company_name, Unset):
            new_company_name = UNSET
        else:
            new_company_name = self.new_company_name

        new_company_logo_url: None | str | Unset
        if isinstance(self.new_company_logo_url, Unset):
            new_company_logo_url = UNSET
        else:
            new_company_logo_url = self.new_company_logo_url

        new_company_org_id: None | str | Unset
        if isinstance(self.new_company_org_id, Unset):
            new_company_org_id = UNSET
        else:
            new_company_org_id = self.new_company_org_id

        new_company_li_slug: None | str | Unset
        if isinstance(self.new_company_li_slug, Unset):
            new_company_li_slug = UNSET
        else:
            new_company_li_slug = self.new_company_li_slug

        new_company_domain: None | str | Unset
        if isinstance(self.new_company_domain, Unset):
            new_company_domain = UNSET
        else:
            new_company_domain = self.new_company_domain

        new_job_title: None | str | Unset
        if isinstance(self.new_job_title, Unset):
            new_job_title = UNSET
        else:
            new_job_title = self.new_job_title

        old_company_name: None | str | Unset
        if isinstance(self.old_company_name, Unset):
            old_company_name = UNSET
        else:
            old_company_name = self.old_company_name

        old_company_logo_url: None | str | Unset
        if isinstance(self.old_company_logo_url, Unset):
            old_company_logo_url = UNSET
        else:
            old_company_logo_url = self.old_company_logo_url

        old_company_org_id: None | str | Unset
        if isinstance(self.old_company_org_id, Unset):
            old_company_org_id = UNSET
        else:
            old_company_org_id = self.old_company_org_id

        old_company_li_slug: None | str | Unset
        if isinstance(self.old_company_li_slug, Unset):
            old_company_li_slug = UNSET
        else:
            old_company_li_slug = self.old_company_li_slug

        old_company_domain: None | str | Unset
        if isinstance(self.old_company_domain, Unset):
            old_company_domain = UNSET
        else:
            old_company_domain = self.old_company_domain

        old_job_title: None | str | Unset
        if isinstance(self.old_job_title, Unset):
            old_job_title = UNSET
        else:
            old_job_title = self.old_job_title

        started_in_role_at: None | str | Unset
        if isinstance(self.started_in_role_at, Unset):
            started_in_role_at = UNSET
        else:
            started_in_role_at = self.started_in_role_at

        started_at_company_at: None | str | Unset
        if isinstance(self.started_at_company_at, Unset):
            started_at_company_at = UNSET
        else:
            started_at_company_at = self.started_at_company_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discoveredAt": discovered_at,
                "movement": movement,
            }
        )
        if new_company_name is not UNSET:
            field_dict["newCompanyName"] = new_company_name
        if new_company_logo_url is not UNSET:
            field_dict["newCompanyLogoUrl"] = new_company_logo_url
        if new_company_org_id is not UNSET:
            field_dict["newCompanyOrgId"] = new_company_org_id
        if new_company_li_slug is not UNSET:
            field_dict["newCompanyLiSlug"] = new_company_li_slug
        if new_company_domain is not UNSET:
            field_dict["newCompanyDomain"] = new_company_domain
        if new_job_title is not UNSET:
            field_dict["newJobTitle"] = new_job_title
        if old_company_name is not UNSET:
            field_dict["oldCompanyName"] = old_company_name
        if old_company_logo_url is not UNSET:
            field_dict["oldCompanyLogoUrl"] = old_company_logo_url
        if old_company_org_id is not UNSET:
            field_dict["oldCompanyOrgId"] = old_company_org_id
        if old_company_li_slug is not UNSET:
            field_dict["oldCompanyLiSlug"] = old_company_li_slug
        if old_company_domain is not UNSET:
            field_dict["oldCompanyDomain"] = old_company_domain
        if old_job_title is not UNSET:
            field_dict["oldJobTitle"] = old_job_title
        if started_in_role_at is not UNSET:
            field_dict["startedInRoleAt"] = started_in_role_at
        if started_at_company_at is not UNSET:
            field_dict["startedAtCompanyAt"] = started_at_company_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discovered_at = d.pop("discoveredAt")

        movement = ListAllProfilesFromJourneymanListResponse200OutputProfilesItemAllMovementsItemMovement(
            d.pop("movement")
        )

        def _parse_new_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_company_name = _parse_new_company_name(d.pop("newCompanyName", UNSET))

        def _parse_new_company_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_company_logo_url = _parse_new_company_logo_url(d.pop("newCompanyLogoUrl", UNSET))

        def _parse_new_company_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_company_org_id = _parse_new_company_org_id(d.pop("newCompanyOrgId", UNSET))

        def _parse_new_company_li_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_company_li_slug = _parse_new_company_li_slug(d.pop("newCompanyLiSlug", UNSET))

        def _parse_new_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_company_domain = _parse_new_company_domain(d.pop("newCompanyDomain", UNSET))

        def _parse_new_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_job_title = _parse_new_job_title(d.pop("newJobTitle", UNSET))

        def _parse_old_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_company_name = _parse_old_company_name(d.pop("oldCompanyName", UNSET))

        def _parse_old_company_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_company_logo_url = _parse_old_company_logo_url(d.pop("oldCompanyLogoUrl", UNSET))

        def _parse_old_company_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_company_org_id = _parse_old_company_org_id(d.pop("oldCompanyOrgId", UNSET))

        def _parse_old_company_li_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_company_li_slug = _parse_old_company_li_slug(d.pop("oldCompanyLiSlug", UNSET))

        def _parse_old_company_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_company_domain = _parse_old_company_domain(d.pop("oldCompanyDomain", UNSET))

        def _parse_old_job_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_job_title = _parse_old_job_title(d.pop("oldJobTitle", UNSET))

        def _parse_started_in_role_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_in_role_at = _parse_started_in_role_at(d.pop("startedInRoleAt", UNSET))

        def _parse_started_at_company_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at_company_at = _parse_started_at_company_at(d.pop("startedAtCompanyAt", UNSET))

        list_all_profiles_from_journeyman_list_response_200_output_profiles_item_all_movements_item = cls(
            discovered_at=discovered_at,
            movement=movement,
            new_company_name=new_company_name,
            new_company_logo_url=new_company_logo_url,
            new_company_org_id=new_company_org_id,
            new_company_li_slug=new_company_li_slug,
            new_company_domain=new_company_domain,
            new_job_title=new_job_title,
            old_company_name=old_company_name,
            old_company_logo_url=old_company_logo_url,
            old_company_org_id=old_company_org_id,
            old_company_li_slug=old_company_li_slug,
            old_company_domain=old_company_domain,
            old_job_title=old_job_title,
            started_in_role_at=started_in_role_at,
            started_at_company_at=started_at_company_at,
        )

        list_all_profiles_from_journeyman_list_response_200_output_profiles_item_all_movements_item.additional_properties = d
        return list_all_profiles_from_journeyman_list_response_200_output_profiles_item_all_movements_item

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
