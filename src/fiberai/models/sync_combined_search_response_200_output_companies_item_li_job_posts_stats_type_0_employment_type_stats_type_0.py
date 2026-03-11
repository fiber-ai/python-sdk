from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_contract import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract,
    )
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_full_time import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime,
    )
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_internship import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship,
    )
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_other import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other,
    )
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_part_time import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime,
    )
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_temporary import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary,
    )
    from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_volunteer import (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer,
    )


T = TypeVar("T", bound="SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0")


@_attrs_define
class SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0:
    """
    Attributes:
        full_time (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime
            | Unset):
        temporary (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary
            | Unset):
        internship
            (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship |
            Unset):
        contract (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract |
            Unset):
        part_time (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime
            | Unset):
        volunteer (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer
            | Unset):
        other (SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other |
            Unset):
    """

    full_time: (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime | Unset
    ) = UNSET
    temporary: (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary | Unset
    ) = UNSET
    internship: (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship | Unset
    ) = UNSET
    contract: (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract | Unset
    ) = UNSET
    part_time: (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime | Unset
    ) = UNSET
    volunteer: (
        SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer | Unset
    ) = UNSET
    other: SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        full_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_time, Unset):
            full_time = self.full_time.to_dict()

        temporary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.temporary, Unset):
            temporary = self.temporary.to_dict()

        internship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internship, Unset):
            internship = self.internship.to_dict()

        contract: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contract, Unset):
            contract = self.contract.to_dict()

        part_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_time, Unset):
            part_time = self.part_time.to_dict()

        volunteer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volunteer, Unset):
            volunteer = self.volunteer.to_dict()

        other: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if full_time is not UNSET:
            field_dict["Full-time"] = full_time
        if temporary is not UNSET:
            field_dict["Temporary"] = temporary
        if internship is not UNSET:
            field_dict["Internship"] = internship
        if contract is not UNSET:
            field_dict["Contract"] = contract
        if part_time is not UNSET:
            field_dict["Part-time"] = part_time
        if volunteer is not UNSET:
            field_dict["Volunteer"] = volunteer
        if other is not UNSET:
            field_dict["Other"] = other

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_contract import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract,
        )
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_full_time import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime,
        )
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_internship import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship,
        )
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_other import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other,
        )
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_part_time import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime,
        )
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_temporary import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary,
        )
        from ..models.sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_volunteer import (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer,
        )

        d = dict(src_dict)
        _full_time = d.pop("Full-time", UNSET)
        full_time: (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime | Unset
        )
        if isinstance(_full_time, Unset):
            full_time = UNSET
        else:
            full_time = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime.from_dict(
                _full_time
            )

        _temporary = d.pop("Temporary", UNSET)
        temporary: (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary
            | Unset
        )
        if isinstance(_temporary, Unset):
            temporary = UNSET
        else:
            temporary = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary.from_dict(
                _temporary
            )

        _internship = d.pop("Internship", UNSET)
        internship: (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship
            | Unset
        )
        if isinstance(_internship, Unset):
            internship = UNSET
        else:
            internship = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship.from_dict(
                _internship
            )

        _contract = d.pop("Contract", UNSET)
        contract: (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract | Unset
        )
        if isinstance(_contract, Unset):
            contract = UNSET
        else:
            contract = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract.from_dict(
                _contract
            )

        _part_time = d.pop("Part-time", UNSET)
        part_time: (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime | Unset
        )
        if isinstance(_part_time, Unset):
            part_time = UNSET
        else:
            part_time = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime.from_dict(
                _part_time
            )

        _volunteer = d.pop("Volunteer", UNSET)
        volunteer: (
            SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer
            | Unset
        )
        if isinstance(_volunteer, Unset):
            volunteer = UNSET
        else:
            volunteer = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer.from_dict(
                _volunteer
            )

        _other = d.pop("Other", UNSET)
        other: SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other | Unset
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = SyncCombinedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other.from_dict(
                _other
            )

        sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0 = cls(
            full_time=full_time,
            temporary=temporary,
            internship=internship,
            contract=contract,
            part_time=part_time,
            volunteer=volunteer,
            other=other,
        )

        return sync_combined_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0
