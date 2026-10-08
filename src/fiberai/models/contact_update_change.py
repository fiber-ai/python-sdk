from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_update_change_contact_change_kind import ContactUpdateChangeContactChangeKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revealed_email import RevealedEmail


T = TypeVar("T", bound="ContactUpdateChange")


@_attrs_define
class ContactUpdateChange:
    """
    Attributes:
        contact_change_kind (ContactUpdateChangeContactChangeKind): What triggered this update: a detected job change,
            or newly found contact info.
        linkedin_company_id (None | str | Unset): LinkedIn company ID
        company_name (None | str | Unset): Company name
        company_linkedin_url (None | str | Unset): Company LinkedIn URL
        linkedin_company_slug (None | str | Unset): LinkedIn company vanity slug
        company_domains (list[str] | None | Unset): Known company domains
        crunchbase_slug (None | str | Unset): Crunchbase organization slug — permalink
            https://www.crunchbase.com/organization/{slug}. Null when not known.
        title (None | str | Unset): Job title
        is_current (bool | Unset): Whether this is a current position
        start_date (None | str | Unset): ISO start date
        end_date (None | str | Unset): ISO end date
        location (None | str | Unset): Position location
        employment_type (None | str | Unset): Employment type
        seniority (None | str | Unset): Seniority level
        new_emails (list[RevealedEmail] | None | Unset): Newly found work email addresses. On a job change item, only
            addresses at that item's company; addresses that can't be tied to a specific new position are delivered in a
            separate new contact info item. Null when none were found.
    """

    contact_change_kind: ContactUpdateChangeContactChangeKind
    linkedin_company_id: None | str | Unset = UNSET
    company_name: None | str | Unset = UNSET
    company_linkedin_url: None | str | Unset = UNSET
    linkedin_company_slug: None | str | Unset = UNSET
    company_domains: list[str] | None | Unset = UNSET
    crunchbase_slug: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    is_current: bool | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    employment_type: None | str | Unset = UNSET
    seniority: None | str | Unset = UNSET
    new_emails: list[RevealedEmail] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_change_kind = self.contact_change_kind.value

        linkedin_company_id: None | str | Unset
        if isinstance(self.linkedin_company_id, Unset):
            linkedin_company_id = UNSET
        else:
            linkedin_company_id = self.linkedin_company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_linkedin_url: None | str | Unset
        if isinstance(self.company_linkedin_url, Unset):
            company_linkedin_url = UNSET
        else:
            company_linkedin_url = self.company_linkedin_url

        linkedin_company_slug: None | str | Unset
        if isinstance(self.linkedin_company_slug, Unset):
            linkedin_company_slug = UNSET
        else:
            linkedin_company_slug = self.linkedin_company_slug

        company_domains: list[str] | None | Unset
        if isinstance(self.company_domains, Unset):
            company_domains = UNSET
        elif isinstance(self.company_domains, list):
            company_domains = self.company_domains

        else:
            company_domains = self.company_domains

        crunchbase_slug: None | str | Unset
        if isinstance(self.crunchbase_slug, Unset):
            crunchbase_slug = UNSET
        else:
            crunchbase_slug = self.crunchbase_slug

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        is_current = self.is_current

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        employment_type: None | str | Unset
        if isinstance(self.employment_type, Unset):
            employment_type = UNSET
        else:
            employment_type = self.employment_type

        seniority: None | str | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        else:
            seniority = self.seniority

        new_emails: list[dict[str, Any]] | None | Unset
        if isinstance(self.new_emails, Unset):
            new_emails = UNSET
        elif isinstance(self.new_emails, list):
            new_emails = []
            for new_emails_type_0_item_data in self.new_emails:
                new_emails_type_0_item = new_emails_type_0_item_data.to_dict()
                new_emails.append(new_emails_type_0_item)

        else:
            new_emails = self.new_emails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactChangeKind": contact_change_kind,
            }
        )
        if linkedin_company_id is not UNSET:
            field_dict["linkedinCompanyId"] = linkedin_company_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_linkedin_url is not UNSET:
            field_dict["companyLinkedinUrl"] = company_linkedin_url
        if linkedin_company_slug is not UNSET:
            field_dict["linkedinCompanySlug"] = linkedin_company_slug
        if company_domains is not UNSET:
            field_dict["companyDomains"] = company_domains
        if crunchbase_slug is not UNSET:
            field_dict["crunchbaseSlug"] = crunchbase_slug
        if title is not UNSET:
            field_dict["title"] = title
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if location is not UNSET:
            field_dict["location"] = location
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if seniority is not UNSET:
            field_dict["seniority"] = seniority
        if new_emails is not UNSET:
            field_dict["newEmails"] = new_emails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revealed_email import RevealedEmail  # noqa: PLC0415

        d = dict(src_dict)
        contact_change_kind = ContactUpdateChangeContactChangeKind(d.pop("contactChangeKind"))

        def _parse_linkedin_company_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_id = _parse_linkedin_company_id(d.pop("linkedinCompanyId", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_company_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_linkedin_url = _parse_company_linkedin_url(d.pop("companyLinkedinUrl", UNSET))

        def _parse_linkedin_company_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_company_slug = _parse_linkedin_company_slug(d.pop("linkedinCompanySlug", UNSET))

        def _parse_company_domains(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_domains_type_0 = cast(list[str], data)

                return company_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        company_domains = _parse_company_domains(d.pop("companyDomains", UNSET))

        def _parse_crunchbase_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crunchbase_slug = _parse_crunchbase_slug(d.pop("crunchbaseSlug", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        is_current = d.pop("isCurrent", UNSET)

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_employment_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_type = _parse_employment_type(d.pop("employmentType", UNSET))

        def _parse_seniority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        def _parse_new_emails(data: object) -> list[RevealedEmail] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                new_emails_type_0 = []
                _new_emails_type_0 = data
                for new_emails_type_0_item_data in _new_emails_type_0:
                    new_emails_type_0_item = RevealedEmail.from_dict(new_emails_type_0_item_data)

                    new_emails_type_0.append(new_emails_type_0_item)

                return new_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RevealedEmail] | None | Unset, data)

        new_emails = _parse_new_emails(d.pop("newEmails", UNSET))

        contact_update_change = cls(
            contact_change_kind=contact_change_kind,
            linkedin_company_id=linkedin_company_id,
            company_name=company_name,
            company_linkedin_url=company_linkedin_url,
            linkedin_company_slug=linkedin_company_slug,
            company_domains=company_domains,
            crunchbase_slug=crunchbase_slug,
            title=title,
            is_current=is_current,
            start_date=start_date,
            end_date=end_date,
            location=location,
            employment_type=employment_type,
            seniority=seniority,
            new_emails=new_emails,
        )

        contact_update_change.additional_properties = d
        return contact_update_change

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
