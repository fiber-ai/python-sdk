from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_other import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_full_time import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_contract import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_part_time import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_temporary import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_volunteer import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer
  from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_internship import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship





T = TypeVar("T", bound="GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0")



@_attrs_define
class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0:
    """ 
        Attributes:
            full_time (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Employ
                mentTypeStatsType0FullTime]):
            temporary (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Employ
                mentTypeStatsType0Temporary]):
            internship (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Emplo
                ymentTypeStatsType0Internship]):
            contract (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Employm
                entTypeStatsType0Contract]):
            part_time (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Employ
                mentTypeStatsType0PartTime]):
            volunteer (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Employ
                mentTypeStatsType0Volunteer]):
            other (Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0Employment
                TypeStatsType0Other]):
     """

    full_time: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime'] = UNSET
    temporary: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary'] = UNSET
    internship: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship'] = UNSET
    contract: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract'] = UNSET
    part_time: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime'] = UNSET
    volunteer: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer'] = UNSET
    other: Union[Unset, 'GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other'] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_other import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_full_time import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_contract import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_part_time import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_temporary import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_volunteer import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_internship import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship
        full_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_time, Unset):
            full_time = self.full_time.to_dict()

        temporary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temporary, Unset):
            temporary = self.temporary.to_dict()

        internship: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.internship, Unset):
            internship = self.internship.to_dict()

        contract: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contract, Unset):
            contract = self.contract.to_dict()

        part_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.part_time, Unset):
            part_time = self.part_time.to_dict()

        volunteer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.volunteer, Unset):
            volunteer = self.volunteer.to_dict()

        other: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
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
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_other import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_full_time import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_contract import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_part_time import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_temporary import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_volunteer import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer
        from ..models.get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0_internship import GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship
        d = dict(src_dict)
        _full_time = d.pop("Full-time", UNSET)
        full_time: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime]
        if isinstance(_full_time,  Unset):
            full_time = UNSET
        else:
            full_time = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0FullTime.from_dict(_full_time)




        _temporary = d.pop("Temporary", UNSET)
        temporary: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary]
        if isinstance(_temporary,  Unset):
            temporary = UNSET
        else:
            temporary = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Temporary.from_dict(_temporary)




        _internship = d.pop("Internship", UNSET)
        internship: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship]
        if isinstance(_internship,  Unset):
            internship = UNSET
        else:
            internship = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Internship.from_dict(_internship)




        _contract = d.pop("Contract", UNSET)
        contract: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract]
        if isinstance(_contract,  Unset):
            contract = UNSET
        else:
            contract = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Contract.from_dict(_contract)




        _part_time = d.pop("Part-time", UNSET)
        part_time: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime]
        if isinstance(_part_time,  Unset):
            part_time = UNSET
        else:
            part_time = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0PartTime.from_dict(_part_time)




        _volunteer = d.pop("Volunteer", UNSET)
        volunteer: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer]
        if isinstance(_volunteer,  Unset):
            volunteer = UNSET
        else:
            volunteer = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Volunteer.from_dict(_volunteer)




        _other = d.pop("Other", UNSET)
        other: Union[Unset, GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other]
        if isinstance(_other,  Unset):
            other = UNSET
        else:
            other = GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemLiJobPostsStatsType0EmploymentTypeStatsType0Other.from_dict(_other)




        get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0 = cls(
            full_time=full_time,
            temporary=temporary,
            internship=internship,
            contract=contract,
            part_time=part_time,
            volunteer=volunteer,
            other=other,
        )

        return get_current_companies_in_saved_search_response_200_output_companies_item_li_job_posts_stats_type_0_employment_type_stats_type_0

