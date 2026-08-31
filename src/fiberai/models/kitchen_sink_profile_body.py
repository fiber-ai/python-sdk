from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kitchen_sink_profile_body_thoroughness_type_1 import KitchenSinkProfileBodyThoroughnessType1
from ..models.kitchen_sink_profile_body_thoroughness_type_2_type_1 import KitchenSinkProfileBodyThoroughnessType2Type1
from ..models.kitchen_sink_profile_body_thoroughness_type_3_type_1 import KitchenSinkProfileBodyThoroughnessType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kitchen_sink_profile_body_company_domain_type_0 import KitchenSinkProfileBodyCompanyDomainType0
    from ..models.kitchen_sink_profile_body_company_identifier_type_0 import (
        KitchenSinkProfileBodyCompanyIdentifierType0,
    )
    from ..models.kitchen_sink_profile_body_company_identifier_type_1 import (
        KitchenSinkProfileBodyCompanyIdentifierType1,
    )
    from ..models.kitchen_sink_profile_body_company_identifier_type_2 import (
        KitchenSinkProfileBodyCompanyIdentifierType2,
    )
    from ..models.kitchen_sink_profile_body_company_name_type_0 import KitchenSinkProfileBodyCompanyNameType0
    from ..models.kitchen_sink_profile_body_job_title_type_0 import KitchenSinkProfileBodyJobTitleType0
    from ..models.kitchen_sink_profile_body_linkedin_headline_type_0 import KitchenSinkProfileBodyLinkedinHeadlineType0
    from ..models.kitchen_sink_profile_body_person_name_type_0 import KitchenSinkProfileBodyPersonNameType0
    from ..models.kitchen_sink_profile_body_profile_identifier_type_0 import (
        KitchenSinkProfileBodyProfileIdentifierType0,
    )
    from ..models.kitchen_sink_profile_body_profile_identifier_type_1 import (
        KitchenSinkProfileBodyProfileIdentifierType1,
    )
    from ..models.kitchen_sink_profile_body_profile_identifier_type_2 import (
        KitchenSinkProfileBodyProfileIdentifierType2,
    )
    from ..models.kitchen_sink_profile_body_profile_location_type_0 import KitchenSinkProfileBodyProfileLocationType0
    from ..models.kitchen_sink_profile_body_school_domain_type_0 import KitchenSinkProfileBodySchoolDomainType0
    from ..models.kitchen_sink_profile_body_school_identifier_type_0 import KitchenSinkProfileBodySchoolIdentifierType0
    from ..models.kitchen_sink_profile_body_school_identifier_type_1 import KitchenSinkProfileBodySchoolIdentifierType1
    from ..models.kitchen_sink_profile_body_school_identifier_type_2 import KitchenSinkProfileBodySchoolIdentifierType2
    from ..models.kitchen_sink_profile_body_school_name_type_0 import KitchenSinkProfileBodySchoolNameType0


T = TypeVar("T", bound="KitchenSinkProfileBody")


@_attrs_define
class KitchenSinkProfileBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        profile_identifier (KitchenSinkProfileBodyProfileIdentifierType0 | KitchenSinkProfileBodyProfileIdentifierType1
            | KitchenSinkProfileBodyProfileIdentifierType2 | None | Unset): LinkedIn profile identifier (slug or URL).
            Provides the best match accuracy.
        email_address (None | str | Unset): Email address to look up. Second-best accuracy after profileIdentifier.
        person_name (KitchenSinkProfileBodyPersonNameType0 | None | Unset): Person's name for matching. Best used with
            companyDomain or companyIdentifier.
        job_title (KitchenSinkProfileBodyJobTitleType0 | None | Unset):
        company_identifier (KitchenSinkProfileBodyCompanyIdentifierType0 | KitchenSinkProfileBodyCompanyIdentifierType1
            | KitchenSinkProfileBodyCompanyIdentifierType2 | None | Unset): LinkedIn identifier for the person's current
            company. Used with personName for matching.
        linkedin_headline (KitchenSinkProfileBodyLinkedinHeadlineType0 | None | Unset):
        company_name (KitchenSinkProfileBodyCompanyNameType0 | None | Unset):
        company_domain (KitchenSinkProfileBodyCompanyDomainType0 | None | Unset): Domain of the person's current company
            (e.g. 'fiber.ai'). Used with personName for matching.
        profile_location (KitchenSinkProfileBodyProfileLocationType0 | None | Unset): Location of the person. Accepts
            country code, state name, and/or a free-text locality string.
        num_profiles (int | Unset): Maximum number of profile results to return per lookup. Defaults to 1. Default: 1.
        live_fetch (bool | None | Unset): When true, triggers a real-time LinkedIn profile fetch. Costs additional
            credits. Useful for profiles not yet in the database or to get the freshest data. Default: False.
        force_company_match (bool | None | Unset): When true, requires that the matched profile works at the specified
            company. Without this, the API may return profiles that match by name but work elsewhere. Default: False.
        school_name (KitchenSinkProfileBodySchoolNameType0 | None | Unset):
        school_identifier (KitchenSinkProfileBodySchoolIdentifierType0 | KitchenSinkProfileBodySchoolIdentifierType1 |
            KitchenSinkProfileBodySchoolIdentifierType2 | None | Unset): The identifier of the school the person is
            currently attending or has attended. If provided, we will lookup the person by school identifier.
        school_domain (KitchenSinkProfileBodySchoolDomainType0 | None | Unset):
        fuzzy_search (bool | None | Unset): When true, enables fuzzy name matching. Useful when exact name spelling is
            uncertain. Default: False.
        thoroughness (KitchenSinkProfileBodyThoroughnessType1 | KitchenSinkProfileBodyThoroughnessType2Type1 |
            KitchenSinkProfileBodyThoroughnessType3Type1 | None | Unset): Controls how thoroughly to search. Higher values
            recover more matches at the cost of additional latency; lower values return faster. Omit to use the recommended
            default. Default: KitchenSinkProfileBodyThoroughnessType1.HIGH.
        get_detailed_education (bool | None | Unset): When true, returns detailed_education[] with school_details for
            each education entry. Default: False.
        get_detailed_work_experience (bool | None | Unset): When true, returns detailed_work_experiences[] with
            company_details (domains, preferred_name, linkedin_primary_slug, li_org_id) for each work experience. Use this
            to get company domains for a person. Default: False.
    """

    api_key: str
    profile_identifier: (
        KitchenSinkProfileBodyProfileIdentifierType0
        | KitchenSinkProfileBodyProfileIdentifierType1
        | KitchenSinkProfileBodyProfileIdentifierType2
        | None
        | Unset
    ) = UNSET
    email_address: None | str | Unset = UNSET
    person_name: KitchenSinkProfileBodyPersonNameType0 | None | Unset = UNSET
    job_title: KitchenSinkProfileBodyJobTitleType0 | None | Unset = UNSET
    company_identifier: (
        KitchenSinkProfileBodyCompanyIdentifierType0
        | KitchenSinkProfileBodyCompanyIdentifierType1
        | KitchenSinkProfileBodyCompanyIdentifierType2
        | None
        | Unset
    ) = UNSET
    linkedin_headline: KitchenSinkProfileBodyLinkedinHeadlineType0 | None | Unset = UNSET
    company_name: KitchenSinkProfileBodyCompanyNameType0 | None | Unset = UNSET
    company_domain: KitchenSinkProfileBodyCompanyDomainType0 | None | Unset = UNSET
    profile_location: KitchenSinkProfileBodyProfileLocationType0 | None | Unset = UNSET
    num_profiles: int | Unset = 1
    live_fetch: bool | None | Unset = False
    force_company_match: bool | None | Unset = False
    school_name: KitchenSinkProfileBodySchoolNameType0 | None | Unset = UNSET
    school_identifier: (
        KitchenSinkProfileBodySchoolIdentifierType0
        | KitchenSinkProfileBodySchoolIdentifierType1
        | KitchenSinkProfileBodySchoolIdentifierType2
        | None
        | Unset
    ) = UNSET
    school_domain: KitchenSinkProfileBodySchoolDomainType0 | None | Unset = UNSET
    fuzzy_search: bool | None | Unset = False
    thoroughness: (
        KitchenSinkProfileBodyThoroughnessType1
        | KitchenSinkProfileBodyThoroughnessType2Type1
        | KitchenSinkProfileBodyThoroughnessType3Type1
        | None
        | Unset
    ) = KitchenSinkProfileBodyThoroughnessType1.HIGH
    get_detailed_education: bool | None | Unset = False
    get_detailed_work_experience: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.kitchen_sink_profile_body_company_domain_type_0 import (
            KitchenSinkProfileBodyCompanyDomainType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_identifier_type_0 import (
            KitchenSinkProfileBodyCompanyIdentifierType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_identifier_type_1 import (
            KitchenSinkProfileBodyCompanyIdentifierType1,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_identifier_type_2 import (
            KitchenSinkProfileBodyCompanyIdentifierType2,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_name_type_0 import (
            KitchenSinkProfileBodyCompanyNameType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_job_title_type_0 import (
            KitchenSinkProfileBodyJobTitleType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_linkedin_headline_type_0 import (
            KitchenSinkProfileBodyLinkedinHeadlineType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_person_name_type_0 import (
            KitchenSinkProfileBodyPersonNameType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_identifier_type_0 import (
            KitchenSinkProfileBodyProfileIdentifierType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_identifier_type_1 import (
            KitchenSinkProfileBodyProfileIdentifierType1,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_identifier_type_2 import (
            KitchenSinkProfileBodyProfileIdentifierType2,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_location_type_0 import (
            KitchenSinkProfileBodyProfileLocationType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_domain_type_0 import (
            KitchenSinkProfileBodySchoolDomainType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_identifier_type_0 import (
            KitchenSinkProfileBodySchoolIdentifierType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_identifier_type_1 import (
            KitchenSinkProfileBodySchoolIdentifierType1,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_identifier_type_2 import (
            KitchenSinkProfileBodySchoolIdentifierType2,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_name_type_0 import (
            KitchenSinkProfileBodySchoolNameType0,  # noqa: PLC0415
        )

        api_key = self.api_key

        profile_identifier: dict[str, Any] | None | Unset
        if isinstance(self.profile_identifier, Unset):
            profile_identifier = UNSET
        elif isinstance(self.profile_identifier, KitchenSinkProfileBodyProfileIdentifierType0):
            profile_identifier = self.profile_identifier.to_dict()
        elif isinstance(self.profile_identifier, KitchenSinkProfileBodyProfileIdentifierType1):
            profile_identifier = self.profile_identifier.to_dict()
        elif isinstance(self.profile_identifier, KitchenSinkProfileBodyProfileIdentifierType2):
            profile_identifier = self.profile_identifier.to_dict()
        else:
            profile_identifier = self.profile_identifier

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        person_name: dict[str, Any] | None | Unset
        if isinstance(self.person_name, Unset):
            person_name = UNSET
        elif isinstance(self.person_name, KitchenSinkProfileBodyPersonNameType0):
            person_name = self.person_name.to_dict()
        else:
            person_name = self.person_name

        job_title: dict[str, Any] | None | Unset
        if isinstance(self.job_title, Unset):
            job_title = UNSET
        elif isinstance(self.job_title, KitchenSinkProfileBodyJobTitleType0):
            job_title = self.job_title.to_dict()
        else:
            job_title = self.job_title

        company_identifier: dict[str, Any] | None | Unset
        if isinstance(self.company_identifier, Unset):
            company_identifier = UNSET
        elif isinstance(self.company_identifier, KitchenSinkProfileBodyCompanyIdentifierType0):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkProfileBodyCompanyIdentifierType1):
            company_identifier = self.company_identifier.to_dict()
        elif isinstance(self.company_identifier, KitchenSinkProfileBodyCompanyIdentifierType2):
            company_identifier = self.company_identifier.to_dict()
        else:
            company_identifier = self.company_identifier

        linkedin_headline: dict[str, Any] | None | Unset
        if isinstance(self.linkedin_headline, Unset):
            linkedin_headline = UNSET
        elif isinstance(self.linkedin_headline, KitchenSinkProfileBodyLinkedinHeadlineType0):
            linkedin_headline = self.linkedin_headline.to_dict()
        else:
            linkedin_headline = self.linkedin_headline

        company_name: dict[str, Any] | None | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        elif isinstance(self.company_name, KitchenSinkProfileBodyCompanyNameType0):
            company_name = self.company_name.to_dict()
        else:
            company_name = self.company_name

        company_domain: dict[str, Any] | None | Unset
        if isinstance(self.company_domain, Unset):
            company_domain = UNSET
        elif isinstance(self.company_domain, KitchenSinkProfileBodyCompanyDomainType0):
            company_domain = self.company_domain.to_dict()
        else:
            company_domain = self.company_domain

        profile_location: dict[str, Any] | None | Unset
        if isinstance(self.profile_location, Unset):
            profile_location = UNSET
        elif isinstance(self.profile_location, KitchenSinkProfileBodyProfileLocationType0):
            profile_location = self.profile_location.to_dict()
        else:
            profile_location = self.profile_location

        num_profiles = self.num_profiles

        live_fetch: bool | None | Unset
        if isinstance(self.live_fetch, Unset):
            live_fetch = UNSET
        else:
            live_fetch = self.live_fetch

        force_company_match: bool | None | Unset
        if isinstance(self.force_company_match, Unset):
            force_company_match = UNSET
        else:
            force_company_match = self.force_company_match

        school_name: dict[str, Any] | None | Unset
        if isinstance(self.school_name, Unset):
            school_name = UNSET
        elif isinstance(self.school_name, KitchenSinkProfileBodySchoolNameType0):
            school_name = self.school_name.to_dict()
        else:
            school_name = self.school_name

        school_identifier: dict[str, Any] | None | Unset
        if isinstance(self.school_identifier, Unset):
            school_identifier = UNSET
        elif isinstance(self.school_identifier, KitchenSinkProfileBodySchoolIdentifierType0):
            school_identifier = self.school_identifier.to_dict()
        elif isinstance(self.school_identifier, KitchenSinkProfileBodySchoolIdentifierType1):
            school_identifier = self.school_identifier.to_dict()
        elif isinstance(self.school_identifier, KitchenSinkProfileBodySchoolIdentifierType2):
            school_identifier = self.school_identifier.to_dict()
        else:
            school_identifier = self.school_identifier

        school_domain: dict[str, Any] | None | Unset
        if isinstance(self.school_domain, Unset):
            school_domain = UNSET
        elif isinstance(self.school_domain, KitchenSinkProfileBodySchoolDomainType0):
            school_domain = self.school_domain.to_dict()
        else:
            school_domain = self.school_domain

        fuzzy_search: bool | None | Unset
        if isinstance(self.fuzzy_search, Unset):
            fuzzy_search = UNSET
        else:
            fuzzy_search = self.fuzzy_search

        thoroughness: None | str | Unset
        if isinstance(self.thoroughness, Unset):
            thoroughness = UNSET
        elif isinstance(self.thoroughness, KitchenSinkProfileBodyThoroughnessType1):
            thoroughness = self.thoroughness.value
        elif isinstance(self.thoroughness, KitchenSinkProfileBodyThoroughnessType2Type1):
            thoroughness = self.thoroughness.value
        elif isinstance(self.thoroughness, KitchenSinkProfileBodyThoroughnessType3Type1):
            thoroughness = self.thoroughness.value
        else:
            thoroughness = self.thoroughness

        get_detailed_education: bool | None | Unset
        if isinstance(self.get_detailed_education, Unset):
            get_detailed_education = UNSET
        else:
            get_detailed_education = self.get_detailed_education

        get_detailed_work_experience: bool | None | Unset
        if isinstance(self.get_detailed_work_experience, Unset):
            get_detailed_work_experience = UNSET
        else:
            get_detailed_work_experience = self.get_detailed_work_experience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
            }
        )
        if profile_identifier is not UNSET:
            field_dict["profileIdentifier"] = profile_identifier
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if person_name is not UNSET:
            field_dict["personName"] = person_name
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if company_identifier is not UNSET:
            field_dict["companyIdentifier"] = company_identifier
        if linkedin_headline is not UNSET:
            field_dict["linkedinHeadline"] = linkedin_headline
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_domain is not UNSET:
            field_dict["companyDomain"] = company_domain
        if profile_location is not UNSET:
            field_dict["profileLocation"] = profile_location
        if num_profiles is not UNSET:
            field_dict["numProfiles"] = num_profiles
        if live_fetch is not UNSET:
            field_dict["liveFetch"] = live_fetch
        if force_company_match is not UNSET:
            field_dict["forceCompanyMatch"] = force_company_match
        if school_name is not UNSET:
            field_dict["schoolName"] = school_name
        if school_identifier is not UNSET:
            field_dict["schoolIdentifier"] = school_identifier
        if school_domain is not UNSET:
            field_dict["schoolDomain"] = school_domain
        if fuzzy_search is not UNSET:
            field_dict["fuzzySearch"] = fuzzy_search
        if thoroughness is not UNSET:
            field_dict["thoroughness"] = thoroughness
        if get_detailed_education is not UNSET:
            field_dict["getDetailedEducation"] = get_detailed_education
        if get_detailed_work_experience is not UNSET:
            field_dict["getDetailedWorkExperience"] = get_detailed_work_experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kitchen_sink_profile_body_company_domain_type_0 import (
            KitchenSinkProfileBodyCompanyDomainType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_identifier_type_0 import (
            KitchenSinkProfileBodyCompanyIdentifierType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_identifier_type_1 import (
            KitchenSinkProfileBodyCompanyIdentifierType1,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_identifier_type_2 import (
            KitchenSinkProfileBodyCompanyIdentifierType2,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_company_name_type_0 import (
            KitchenSinkProfileBodyCompanyNameType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_job_title_type_0 import (
            KitchenSinkProfileBodyJobTitleType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_linkedin_headline_type_0 import (
            KitchenSinkProfileBodyLinkedinHeadlineType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_person_name_type_0 import (
            KitchenSinkProfileBodyPersonNameType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_identifier_type_0 import (
            KitchenSinkProfileBodyProfileIdentifierType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_identifier_type_1 import (
            KitchenSinkProfileBodyProfileIdentifierType1,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_identifier_type_2 import (
            KitchenSinkProfileBodyProfileIdentifierType2,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_profile_location_type_0 import (
            KitchenSinkProfileBodyProfileLocationType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_domain_type_0 import (
            KitchenSinkProfileBodySchoolDomainType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_identifier_type_0 import (
            KitchenSinkProfileBodySchoolIdentifierType0,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_identifier_type_1 import (
            KitchenSinkProfileBodySchoolIdentifierType1,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_identifier_type_2 import (
            KitchenSinkProfileBodySchoolIdentifierType2,  # noqa: PLC0415
        )
        from ..models.kitchen_sink_profile_body_school_name_type_0 import (
            KitchenSinkProfileBodySchoolNameType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_profile_identifier(
            data: object,
        ) -> (
            KitchenSinkProfileBodyProfileIdentifierType0
            | KitchenSinkProfileBodyProfileIdentifierType1
            | KitchenSinkProfileBodyProfileIdentifierType2
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_identifier_type_0 = KitchenSinkProfileBodyProfileIdentifierType0.from_dict(data)

                return profile_identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_identifier_type_1 = KitchenSinkProfileBodyProfileIdentifierType1.from_dict(data)

                return profile_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_identifier_type_2 = KitchenSinkProfileBodyProfileIdentifierType2.from_dict(data)

                return profile_identifier_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkProfileBodyProfileIdentifierType0
                | KitchenSinkProfileBodyProfileIdentifierType1
                | KitchenSinkProfileBodyProfileIdentifierType2
                | None
                | Unset,
                data,
            )

        profile_identifier = _parse_profile_identifier(d.pop("profileIdentifier", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_person_name(data: object) -> KitchenSinkProfileBodyPersonNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_name_type_0 = KitchenSinkProfileBodyPersonNameType0.from_dict(data)

                return person_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodyPersonNameType0 | None | Unset, data)

        person_name = _parse_person_name(d.pop("personName", UNSET))

        def _parse_job_title(data: object) -> KitchenSinkProfileBodyJobTitleType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_title_type_0 = KitchenSinkProfileBodyJobTitleType0.from_dict(data)

                return job_title_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodyJobTitleType0 | None | Unset, data)

        job_title = _parse_job_title(d.pop("jobTitle", UNSET))

        def _parse_company_identifier(
            data: object,
        ) -> (
            KitchenSinkProfileBodyCompanyIdentifierType0
            | KitchenSinkProfileBodyCompanyIdentifierType1
            | KitchenSinkProfileBodyCompanyIdentifierType2
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_0 = KitchenSinkProfileBodyCompanyIdentifierType0.from_dict(data)

                return company_identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_1 = KitchenSinkProfileBodyCompanyIdentifierType1.from_dict(data)

                return company_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_identifier_type_2 = KitchenSinkProfileBodyCompanyIdentifierType2.from_dict(data)

                return company_identifier_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkProfileBodyCompanyIdentifierType0
                | KitchenSinkProfileBodyCompanyIdentifierType1
                | KitchenSinkProfileBodyCompanyIdentifierType2
                | None
                | Unset,
                data,
            )

        company_identifier = _parse_company_identifier(d.pop("companyIdentifier", UNSET))

        def _parse_linkedin_headline(data: object) -> KitchenSinkProfileBodyLinkedinHeadlineType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                linkedin_headline_type_0 = KitchenSinkProfileBodyLinkedinHeadlineType0.from_dict(data)

                return linkedin_headline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodyLinkedinHeadlineType0 | None | Unset, data)

        linkedin_headline = _parse_linkedin_headline(d.pop("linkedinHeadline", UNSET))

        def _parse_company_name(data: object) -> KitchenSinkProfileBodyCompanyNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_name_type_0 = KitchenSinkProfileBodyCompanyNameType0.from_dict(data)

                return company_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodyCompanyNameType0 | None | Unset, data)

        company_name = _parse_company_name(d.pop("companyName", UNSET))

        def _parse_company_domain(data: object) -> KitchenSinkProfileBodyCompanyDomainType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_domain_type_0 = KitchenSinkProfileBodyCompanyDomainType0.from_dict(data)

                return company_domain_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodyCompanyDomainType0 | None | Unset, data)

        company_domain = _parse_company_domain(d.pop("companyDomain", UNSET))

        def _parse_profile_location(data: object) -> KitchenSinkProfileBodyProfileLocationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_location_type_0 = KitchenSinkProfileBodyProfileLocationType0.from_dict(data)

                return profile_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodyProfileLocationType0 | None | Unset, data)

        profile_location = _parse_profile_location(d.pop("profileLocation", UNSET))

        num_profiles = d.pop("numProfiles", UNSET)

        def _parse_live_fetch(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        live_fetch = _parse_live_fetch(d.pop("liveFetch", UNSET))

        def _parse_force_company_match(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_company_match = _parse_force_company_match(d.pop("forceCompanyMatch", UNSET))

        def _parse_school_name(data: object) -> KitchenSinkProfileBodySchoolNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_name_type_0 = KitchenSinkProfileBodySchoolNameType0.from_dict(data)

                return school_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodySchoolNameType0 | None | Unset, data)

        school_name = _parse_school_name(d.pop("schoolName", UNSET))

        def _parse_school_identifier(
            data: object,
        ) -> (
            KitchenSinkProfileBodySchoolIdentifierType0
            | KitchenSinkProfileBodySchoolIdentifierType1
            | KitchenSinkProfileBodySchoolIdentifierType2
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_identifier_type_0 = KitchenSinkProfileBodySchoolIdentifierType0.from_dict(data)

                return school_identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_identifier_type_1 = KitchenSinkProfileBodySchoolIdentifierType1.from_dict(data)

                return school_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_identifier_type_2 = KitchenSinkProfileBodySchoolIdentifierType2.from_dict(data)

                return school_identifier_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkProfileBodySchoolIdentifierType0
                | KitchenSinkProfileBodySchoolIdentifierType1
                | KitchenSinkProfileBodySchoolIdentifierType2
                | None
                | Unset,
                data,
            )

        school_identifier = _parse_school_identifier(d.pop("schoolIdentifier", UNSET))

        def _parse_school_domain(data: object) -> KitchenSinkProfileBodySchoolDomainType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                school_domain_type_0 = KitchenSinkProfileBodySchoolDomainType0.from_dict(data)

                return school_domain_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KitchenSinkProfileBodySchoolDomainType0 | None | Unset, data)

        school_domain = _parse_school_domain(d.pop("schoolDomain", UNSET))

        def _parse_fuzzy_search(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fuzzy_search = _parse_fuzzy_search(d.pop("fuzzySearch", UNSET))

        def _parse_thoroughness(
            data: object,
        ) -> (
            KitchenSinkProfileBodyThoroughnessType1
            | KitchenSinkProfileBodyThoroughnessType2Type1
            | KitchenSinkProfileBodyThoroughnessType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thoroughness_type_1 = KitchenSinkProfileBodyThoroughnessType1(data)

                return thoroughness_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thoroughness_type_2_type_1 = KitchenSinkProfileBodyThoroughnessType2Type1(data)

                return thoroughness_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thoroughness_type_3_type_1 = KitchenSinkProfileBodyThoroughnessType3Type1(data)

                return thoroughness_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KitchenSinkProfileBodyThoroughnessType1
                | KitchenSinkProfileBodyThoroughnessType2Type1
                | KitchenSinkProfileBodyThoroughnessType3Type1
                | None
                | Unset,
                data,
            )

        thoroughness = _parse_thoroughness(d.pop("thoroughness", UNSET))

        def _parse_get_detailed_education(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_education = _parse_get_detailed_education(d.pop("getDetailedEducation", UNSET))

        def _parse_get_detailed_work_experience(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        get_detailed_work_experience = _parse_get_detailed_work_experience(d.pop("getDetailedWorkExperience", UNSET))

        kitchen_sink_profile_body = cls(
            api_key=api_key,
            profile_identifier=profile_identifier,
            email_address=email_address,
            person_name=person_name,
            job_title=job_title,
            company_identifier=company_identifier,
            linkedin_headline=linkedin_headline,
            company_name=company_name,
            company_domain=company_domain,
            profile_location=profile_location,
            num_profiles=num_profiles,
            live_fetch=live_fetch,
            force_company_match=force_company_match,
            school_name=school_name,
            school_identifier=school_identifier,
            school_domain=school_domain,
            fuzzy_search=fuzzy_search,
            thoroughness=thoroughness,
            get_detailed_education=get_detailed_education,
            get_detailed_work_experience=get_detailed_work_experience,
        )

        kitchen_sink_profile_body.additional_properties = d
        return kitchen_sink_profile_body

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
