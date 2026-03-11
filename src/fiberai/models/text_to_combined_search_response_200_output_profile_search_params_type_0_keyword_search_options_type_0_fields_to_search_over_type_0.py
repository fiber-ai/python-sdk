from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0FieldsToSearchOverType0",
)


@_attrs_define
class TextToCombinedSearchResponse200OutputProfileSearchParamsType0KeywordSearchOptionsType0FieldsToSearchOverType0:
    """
    Attributes:
        summary (bool):  Default: True.
        headline (bool):  Default: True.
        past_job_titles (bool):  Default: True.
        past_job_summaries (bool):  Default: True.
        past_company_names (bool):  Default: True.
        current_job_titles (bool):  Default: True.
        current_job_summaries (bool):  Default: True.
        current_company_names (bool):  Default: True.
        interests (bool):  Default: True.
        skills (bool):  Default: True.
        industry (bool):  Default: True.
        education (bool):  Default: True.
        publications (bool):  Default: True.
        certifications (bool):  Default: True.
        articles (bool):  Default: True.
        courses (bool):  Default: True.
        projects (bool):  Default: True.
        patents (bool):  Default: True.
        volunteering (bool):  Default: False.
        languages (bool):  Default: False.
    """

    summary: bool = True
    headline: bool = True
    past_job_titles: bool = True
    past_job_summaries: bool = True
    past_company_names: bool = True
    current_job_titles: bool = True
    current_job_summaries: bool = True
    current_company_names: bool = True
    interests: bool = True
    skills: bool = True
    industry: bool = True
    education: bool = True
    publications: bool = True
    certifications: bool = True
    articles: bool = True
    courses: bool = True
    projects: bool = True
    patents: bool = True
    volunteering: bool = False
    languages: bool = False
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
        field_dict.update(
            {
                "summary": summary,
                "headline": headline,
                "pastJobTitles": past_job_titles,
                "pastJobSummaries": past_job_summaries,
                "pastCompanyNames": past_company_names,
                "currentJobTitles": current_job_titles,
                "currentJobSummaries": current_job_summaries,
                "currentCompanyNames": current_company_names,
                "interests": interests,
                "skills": skills,
                "industry": industry,
                "education": education,
                "publications": publications,
                "certifications": certifications,
                "articles": articles,
                "courses": courses,
                "projects": projects,
                "patents": patents,
                "volunteering": volunteering,
                "languages": languages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary")

        headline = d.pop("headline")

        past_job_titles = d.pop("pastJobTitles")

        past_job_summaries = d.pop("pastJobSummaries")

        past_company_names = d.pop("pastCompanyNames")

        current_job_titles = d.pop("currentJobTitles")

        current_job_summaries = d.pop("currentJobSummaries")

        current_company_names = d.pop("currentCompanyNames")

        interests = d.pop("interests")

        skills = d.pop("skills")

        industry = d.pop("industry")

        education = d.pop("education")

        publications = d.pop("publications")

        certifications = d.pop("certifications")

        articles = d.pop("articles")

        courses = d.pop("courses")

        projects = d.pop("projects")

        patents = d.pop("patents")

        volunteering = d.pop("volunteering")

        languages = d.pop("languages")

        text_to_combined_search_response_200_output_profile_search_params_type_0_keyword_search_options_type_0_fields_to_search_over_type_0 = cls(
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

        text_to_combined_search_response_200_output_profile_search_params_type_0_keyword_search_options_type_0_fields_to_search_over_type_0.additional_properties = d
        return text_to_combined_search_response_200_output_profile_search_params_type_0_keyword_search_options_type_0_fields_to_search_over_type_0

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
