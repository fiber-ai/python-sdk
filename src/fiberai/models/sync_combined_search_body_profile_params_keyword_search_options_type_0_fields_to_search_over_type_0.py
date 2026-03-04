from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="SyncCombinedSearchBodyProfileParamsKeywordSearchOptionsType0FieldsToSearchOverType0")



@_attrs_define
class SyncCombinedSearchBodyProfileParamsKeywordSearchOptionsType0FieldsToSearchOverType0:
    """ 
        Attributes:
            summary (Union[Unset, bool]):  Default: True.
            headline (Union[Unset, bool]):  Default: True.
            past_job_titles (Union[Unset, bool]):  Default: True.
            past_job_summaries (Union[Unset, bool]):  Default: True.
            past_company_names (Union[Unset, bool]):  Default: True.
            current_job_titles (Union[Unset, bool]):  Default: True.
            current_job_summaries (Union[Unset, bool]):  Default: True.
            current_company_names (Union[Unset, bool]):  Default: True.
            interests (Union[Unset, bool]):  Default: True.
            skills (Union[Unset, bool]):  Default: True.
            industry (Union[Unset, bool]):  Default: True.
            education (Union[Unset, bool]):  Default: True.
            publications (Union[Unset, bool]):  Default: True.
            certifications (Union[Unset, bool]):  Default: True.
            articles (Union[Unset, bool]):  Default: True.
            courses (Union[Unset, bool]):  Default: True.
            projects (Union[Unset, bool]):  Default: True.
            patents (Union[Unset, bool]):  Default: True.
            volunteering (Union[Unset, bool]):  Default: False.
            languages (Union[Unset, bool]):  Default: False.
     """

    summary: Union[Unset, bool] = True
    headline: Union[Unset, bool] = True
    past_job_titles: Union[Unset, bool] = True
    past_job_summaries: Union[Unset, bool] = True
    past_company_names: Union[Unset, bool] = True
    current_job_titles: Union[Unset, bool] = True
    current_job_summaries: Union[Unset, bool] = True
    current_company_names: Union[Unset, bool] = True
    interests: Union[Unset, bool] = True
    skills: Union[Unset, bool] = True
    industry: Union[Unset, bool] = True
    education: Union[Unset, bool] = True
    publications: Union[Unset, bool] = True
    certifications: Union[Unset, bool] = True
    articles: Union[Unset, bool] = True
    courses: Union[Unset, bool] = True
    projects: Union[Unset, bool] = True
    patents: Union[Unset, bool] = True
    volunteering: Union[Unset, bool] = False
    languages: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        headline = self.headline

        past_job_titles = self.past_job_titles

        past_job_summaries = self.past_job_summaries

        past_company_names = self.past_company_names

        current_job_titles = self.current_job_titles

        current_job_summaries = self.current_job_summaries

        current_company_names = self.current_company_names

        interests = self.interests

        skills = self.skills

        industry = self.industry

        education = self.education

        publications = self.publications

        certifications = self.certifications

        articles = self.articles

        courses = self.courses

        projects = self.projects

        patents = self.patents

        volunteering = self.volunteering

        languages = self.languages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if summary is not UNSET:
            field_dict["summary"] = summary
        if headline is not UNSET:
            field_dict["headline"] = headline
        if past_job_titles is not UNSET:
            field_dict["pastJobTitles"] = past_job_titles
        if past_job_summaries is not UNSET:
            field_dict["pastJobSummaries"] = past_job_summaries
        if past_company_names is not UNSET:
            field_dict["pastCompanyNames"] = past_company_names
        if current_job_titles is not UNSET:
            field_dict["currentJobTitles"] = current_job_titles
        if current_job_summaries is not UNSET:
            field_dict["currentJobSummaries"] = current_job_summaries
        if current_company_names is not UNSET:
            field_dict["currentCompanyNames"] = current_company_names
        if interests is not UNSET:
            field_dict["interests"] = interests
        if skills is not UNSET:
            field_dict["skills"] = skills
        if industry is not UNSET:
            field_dict["industry"] = industry
        if education is not UNSET:
            field_dict["education"] = education
        if publications is not UNSET:
            field_dict["publications"] = publications
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if articles is not UNSET:
            field_dict["articles"] = articles
        if courses is not UNSET:
            field_dict["courses"] = courses
        if projects is not UNSET:
            field_dict["projects"] = projects
        if patents is not UNSET:
            field_dict["patents"] = patents
        if volunteering is not UNSET:
            field_dict["volunteering"] = volunteering
        if languages is not UNSET:
            field_dict["languages"] = languages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary", UNSET)

        headline = d.pop("headline", UNSET)

        past_job_titles = d.pop("pastJobTitles", UNSET)

        past_job_summaries = d.pop("pastJobSummaries", UNSET)

        past_company_names = d.pop("pastCompanyNames", UNSET)

        current_job_titles = d.pop("currentJobTitles", UNSET)

        current_job_summaries = d.pop("currentJobSummaries", UNSET)

        current_company_names = d.pop("currentCompanyNames", UNSET)

        interests = d.pop("interests", UNSET)

        skills = d.pop("skills", UNSET)

        industry = d.pop("industry", UNSET)

        education = d.pop("education", UNSET)

        publications = d.pop("publications", UNSET)

        certifications = d.pop("certifications", UNSET)

        articles = d.pop("articles", UNSET)

        courses = d.pop("courses", UNSET)

        projects = d.pop("projects", UNSET)

        patents = d.pop("patents", UNSET)

        volunteering = d.pop("volunteering", UNSET)

        languages = d.pop("languages", UNSET)

        sync_combined_search_body_profile_params_keyword_search_options_type_0_fields_to_search_over_type_0 = cls(
            summary=summary,
            headline=headline,
            past_job_titles=past_job_titles,
            past_job_summaries=past_job_summaries,
            past_company_names=past_company_names,
            current_job_titles=current_job_titles,
            current_job_summaries=current_job_summaries,
            current_company_names=current_company_names,
            interests=interests,
            skills=skills,
            industry=industry,
            education=education,
            publications=publications,
            certifications=certifications,
            articles=articles,
            courses=courses,
            projects=projects,
            patents=patents,
            volunteering=volunteering,
            languages=languages,
        )


        sync_combined_search_body_profile_params_keyword_search_options_type_0_fields_to_search_over_type_0.additional_properties = d
        return sync_combined_search_body_profile_params_keyword_search_options_type_0_fields_to_search_over_type_0

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
