from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_combined_search_response_200_output_data_profiles_item_tags_type_0_item import (
    TextToCombinedSearchResponse200OutputDataProfilesItemTagsType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_articles_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_certifications_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_courses_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_current_job_type_0 import (
        TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_custom_data_type_0 import (
        TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_detailed_education_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_detailed_work_experiences_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_education_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_experiences_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_inferred_location_type_0 import (
        TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_languages_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_organizations_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_patents_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_projects_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_publications_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_tenures_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item,
    )
    from ..models.text_to_combined_search_response_200_output_data_profiles_item_volunteering_type_0_item import (
        TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item,
    )


T = TypeVar("T", bound="TextToCombinedSearchResponse200OutputDataProfilesItem")


@_attrs_define
class TextToCombinedSearchResponse200OutputDataProfilesItem:
    """
    Attributes:
        primary_slug (str):
        articles (list[TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item] | None | Unset):
        certifications (list[TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item] | None |
            Unset):
        connection_count (float | None | Unset):
        courses (list[TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item] | None | Unset):
        dob (None | str | Unset):
        education (list[TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item] | None | Unset):
        experiences (list[TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item] | None | Unset):
        first_name (None | str | Unset):
        follower_count (float | None | Unset):
        headline (None | str | Unset):
        industry_name (None | str | Unset):
        inferred_location (None | TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0 | Unset):
        interests (list[str] | None | Unset):
        last_name (None | str | Unset):
        locality (None | str | Unset):
        name (None | str | Unset):
        patents (list[TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item] | None | Unset):
        profile_pic (None | str | Unset):
        projects (list[TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item] | None | Unset):
        publications (list[TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item] | None | Unset):
        skills (list[str] | None | Unset):
        slugs (list[str] | None | Unset):
        summary (None | str | Unset):
        url (None | str | Unset):
        user_id (None | str | Unset):
        volunteering (list[TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item] | None | Unset):
        tenures (list[TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item] | None | Unset):
        career_began_at (None | str | Unset):
        tags (list[TextToCombinedSearchResponse200OutputDataProfilesItemTagsType0Item] | None | Unset):
        entity_urn (None | str | Unset):
        open_to_work (bool | None | Unset):
        premium (bool | None | Unset):
        influencer (bool | None | Unset):
        organizations (list[TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item] | None |
            Unset):
        entity_urns (list[str] | None | Unset):
        is_hiring (bool | None | Unset):
        current_job (None | TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0 | Unset):
        custom_data (None | TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0 | Unset):
        relevance_score (float | None | Unset):
        last_sort_key (None | str | Unset):
        languages (list[TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item] | None | Unset):
        detailed_education (list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item] | None
            | Unset):
        detailed_work_experiences
            (list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item] | None | Unset):
    """

    primary_slug: str
    articles: list[TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item] | None | Unset = UNSET
    certifications: (
        list[TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item] | None | Unset
    ) = UNSET
    connection_count: float | None | Unset = UNSET
    courses: list[TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item] | None | Unset = UNSET
    dob: None | str | Unset = UNSET
    education: list[TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item] | None | Unset = UNSET
    experiences: list[TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item] | None | Unset = UNSET
    first_name: None | str | Unset = UNSET
    follower_count: float | None | Unset = UNSET
    headline: None | str | Unset = UNSET
    industry_name: None | str | Unset = UNSET
    inferred_location: None | TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0 | Unset = UNSET
    interests: list[str] | None | Unset = UNSET
    last_name: None | str | Unset = UNSET
    locality: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    patents: list[TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item] | None | Unset = UNSET
    profile_pic: None | str | Unset = UNSET
    projects: list[TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item] | None | Unset = UNSET
    publications: list[TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item] | None | Unset = (
        UNSET
    )
    skills: list[str] | None | Unset = UNSET
    slugs: list[str] | None | Unset = UNSET
    summary: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    volunteering: list[TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item] | None | Unset = (
        UNSET
    )
    tenures: list[TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item] | None | Unset = UNSET
    career_began_at: None | str | Unset = UNSET
    tags: list[TextToCombinedSearchResponse200OutputDataProfilesItemTagsType0Item] | None | Unset = UNSET
    entity_urn: None | str | Unset = UNSET
    open_to_work: bool | None | Unset = UNSET
    premium: bool | None | Unset = UNSET
    influencer: bool | None | Unset = UNSET
    organizations: list[TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item] | None | Unset = (
        UNSET
    )
    entity_urns: list[str] | None | Unset = UNSET
    is_hiring: bool | None | Unset = UNSET
    current_job: None | TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0 | Unset = UNSET
    custom_data: None | TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0 | Unset = UNSET
    relevance_score: float | None | Unset = UNSET
    last_sort_key: None | str | Unset = UNSET
    languages: list[TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item] | None | Unset = UNSET
    detailed_education: (
        list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item] | None | Unset
    ) = UNSET
    detailed_work_experiences: (
        list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item] | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_current_job_type_0 import (
            TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_custom_data_type_0 import (
            TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_inferred_location_type_0 import (
            TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0,
        )

        primary_slug = self.primary_slug

        articles: list[dict[str, Any]] | None | Unset
        if isinstance(self.articles, Unset):
            articles = UNSET
        elif isinstance(self.articles, list):
            articles = []
            for articles_type_0_item_data in self.articles:
                articles_type_0_item = articles_type_0_item_data.to_dict()
                articles.append(articles_type_0_item)

        else:
            articles = self.articles

        certifications: list[dict[str, Any]] | None | Unset
        if isinstance(self.certifications, Unset):
            certifications = UNSET
        elif isinstance(self.certifications, list):
            certifications = []
            for certifications_type_0_item_data in self.certifications:
                certifications_type_0_item = certifications_type_0_item_data.to_dict()
                certifications.append(certifications_type_0_item)

        else:
            certifications = self.certifications

        connection_count: float | None | Unset
        if isinstance(self.connection_count, Unset):
            connection_count = UNSET
        else:
            connection_count = self.connection_count

        courses: list[dict[str, Any]] | None | Unset
        if isinstance(self.courses, Unset):
            courses = UNSET
        elif isinstance(self.courses, list):
            courses = []
            for courses_type_0_item_data in self.courses:
                courses_type_0_item = courses_type_0_item_data.to_dict()
                courses.append(courses_type_0_item)

        else:
            courses = self.courses

        dob: None | str | Unset
        if isinstance(self.dob, Unset):
            dob = UNSET
        else:
            dob = self.dob

        education: list[dict[str, Any]] | None | Unset
        if isinstance(self.education, Unset):
            education = UNSET
        elif isinstance(self.education, list):
            education = []
            for education_type_0_item_data in self.education:
                education_type_0_item = education_type_0_item_data.to_dict()
                education.append(education_type_0_item)

        else:
            education = self.education

        experiences: list[dict[str, Any]] | None | Unset
        if isinstance(self.experiences, Unset):
            experiences = UNSET
        elif isinstance(self.experiences, list):
            experiences = []
            for experiences_type_0_item_data in self.experiences:
                experiences_type_0_item = experiences_type_0_item_data.to_dict()
                experiences.append(experiences_type_0_item)

        else:
            experiences = self.experiences

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        follower_count: float | None | Unset
        if isinstance(self.follower_count, Unset):
            follower_count = UNSET
        else:
            follower_count = self.follower_count

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        industry_name: None | str | Unset
        if isinstance(self.industry_name, Unset):
            industry_name = UNSET
        else:
            industry_name = self.industry_name

        inferred_location: dict[str, Any] | None | Unset
        if isinstance(self.inferred_location, Unset):
            inferred_location = UNSET
        elif isinstance(
            self.inferred_location, TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0
        ):
            inferred_location = self.inferred_location.to_dict()
        else:
            inferred_location = self.inferred_location

        interests: list[str] | None | Unset
        if isinstance(self.interests, Unset):
            interests = UNSET
        elif isinstance(self.interests, list):
            interests = self.interests

        else:
            interests = self.interests

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        locality: None | str | Unset
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        patents: list[dict[str, Any]] | None | Unset
        if isinstance(self.patents, Unset):
            patents = UNSET
        elif isinstance(self.patents, list):
            patents = []
            for patents_type_0_item_data in self.patents:
                patents_type_0_item = patents_type_0_item_data.to_dict()
                patents.append(patents_type_0_item)

        else:
            patents = self.patents

        profile_pic: None | str | Unset
        if isinstance(self.profile_pic, Unset):
            profile_pic = UNSET
        else:
            profile_pic = self.profile_pic

        projects: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        publications: list[dict[str, Any]] | None | Unset
        if isinstance(self.publications, Unset):
            publications = UNSET
        elif isinstance(self.publications, list):
            publications = []
            for publications_type_0_item_data in self.publications:
                publications_type_0_item = publications_type_0_item_data.to_dict()
                publications.append(publications_type_0_item)

        else:
            publications = self.publications

        skills: list[str] | None | Unset
        if isinstance(self.skills, Unset):
            skills = UNSET
        elif isinstance(self.skills, list):
            skills = self.skills

        else:
            skills = self.skills

        slugs: list[str] | None | Unset
        if isinstance(self.slugs, Unset):
            slugs = UNSET
        elif isinstance(self.slugs, list):
            slugs = self.slugs

        else:
            slugs = self.slugs

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        volunteering: list[dict[str, Any]] | None | Unset
        if isinstance(self.volunteering, Unset):
            volunteering = UNSET
        elif isinstance(self.volunteering, list):
            volunteering = []
            for volunteering_type_0_item_data in self.volunteering:
                volunteering_type_0_item = volunteering_type_0_item_data.to_dict()
                volunteering.append(volunteering_type_0_item)

        else:
            volunteering = self.volunteering

        tenures: list[dict[str, Any]] | None | Unset
        if isinstance(self.tenures, Unset):
            tenures = UNSET
        elif isinstance(self.tenures, list):
            tenures = []
            for tenures_type_0_item_data in self.tenures:
                tenures_type_0_item = tenures_type_0_item_data.to_dict()
                tenures.append(tenures_type_0_item)

        else:
            tenures = self.tenures

        career_began_at: None | str | Unset
        if isinstance(self.career_began_at, Unset):
            career_began_at = UNSET
        else:
            career_began_at = self.career_began_at

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.value
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        entity_urn: None | str | Unset
        if isinstance(self.entity_urn, Unset):
            entity_urn = UNSET
        else:
            entity_urn = self.entity_urn

        open_to_work: bool | None | Unset
        if isinstance(self.open_to_work, Unset):
            open_to_work = UNSET
        else:
            open_to_work = self.open_to_work

        premium: bool | None | Unset
        if isinstance(self.premium, Unset):
            premium = UNSET
        else:
            premium = self.premium

        influencer: bool | None | Unset
        if isinstance(self.influencer, Unset):
            influencer = UNSET
        else:
            influencer = self.influencer

        organizations: list[dict[str, Any]] | None | Unset
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item = organizations_type_0_item_data.to_dict()
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

        entity_urns: list[str] | None | Unset
        if isinstance(self.entity_urns, Unset):
            entity_urns = UNSET
        elif isinstance(self.entity_urns, list):
            entity_urns = self.entity_urns

        else:
            entity_urns = self.entity_urns

        is_hiring: bool | None | Unset
        if isinstance(self.is_hiring, Unset):
            is_hiring = UNSET
        else:
            is_hiring = self.is_hiring

        current_job: dict[str, Any] | None | Unset
        if isinstance(self.current_job, Unset):
            current_job = UNSET
        elif isinstance(self.current_job, TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0):
            current_job = self.current_job.to_dict()
        else:
            current_job = self.current_job

        custom_data: dict[str, Any] | None | Unset
        if isinstance(self.custom_data, Unset):
            custom_data = UNSET
        elif isinstance(self.custom_data, TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0):
            custom_data = self.custom_data.to_dict()
        else:
            custom_data = self.custom_data

        relevance_score: float | None | Unset
        if isinstance(self.relevance_score, Unset):
            relevance_score = UNSET
        else:
            relevance_score = self.relevance_score

        last_sort_key: None | str | Unset
        if isinstance(self.last_sort_key, Unset):
            last_sort_key = UNSET
        else:
            last_sort_key = self.last_sort_key

        languages: list[dict[str, Any]] | None | Unset
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, list):
            languages = []
            for languages_type_0_item_data in self.languages:
                languages_type_0_item = languages_type_0_item_data.to_dict()
                languages.append(languages_type_0_item)

        else:
            languages = self.languages

        detailed_education: list[dict[str, Any]] | None | Unset
        if isinstance(self.detailed_education, Unset):
            detailed_education = UNSET
        elif isinstance(self.detailed_education, list):
            detailed_education = []
            for detailed_education_type_0_item_data in self.detailed_education:
                detailed_education_type_0_item = detailed_education_type_0_item_data.to_dict()
                detailed_education.append(detailed_education_type_0_item)

        else:
            detailed_education = self.detailed_education

        detailed_work_experiences: list[dict[str, Any]] | None | Unset
        if isinstance(self.detailed_work_experiences, Unset):
            detailed_work_experiences = UNSET
        elif isinstance(self.detailed_work_experiences, list):
            detailed_work_experiences = []
            for detailed_work_experiences_type_0_item_data in self.detailed_work_experiences:
                detailed_work_experiences_type_0_item = detailed_work_experiences_type_0_item_data.to_dict()
                detailed_work_experiences.append(detailed_work_experiences_type_0_item)

        else:
            detailed_work_experiences = self.detailed_work_experiences

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "primary_slug": primary_slug,
            }
        )
        if articles is not UNSET:
            field_dict["articles"] = articles
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if connection_count is not UNSET:
            field_dict["connection_count"] = connection_count
        if courses is not UNSET:
            field_dict["courses"] = courses
        if dob is not UNSET:
            field_dict["dob"] = dob
        if education is not UNSET:
            field_dict["education"] = education
        if experiences is not UNSET:
            field_dict["experiences"] = experiences
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if headline is not UNSET:
            field_dict["headline"] = headline
        if industry_name is not UNSET:
            field_dict["industry_name"] = industry_name
        if inferred_location is not UNSET:
            field_dict["inferred_location"] = inferred_location
        if interests is not UNSET:
            field_dict["interests"] = interests
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if locality is not UNSET:
            field_dict["locality"] = locality
        if name is not UNSET:
            field_dict["name"] = name
        if patents is not UNSET:
            field_dict["patents"] = patents
        if profile_pic is not UNSET:
            field_dict["profile_pic"] = profile_pic
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publications is not UNSET:
            field_dict["publications"] = publications
        if skills is not UNSET:
            field_dict["skills"] = skills
        if slugs is not UNSET:
            field_dict["slugs"] = slugs
        if summary is not UNSET:
            field_dict["summary"] = summary
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if volunteering is not UNSET:
            field_dict["volunteering"] = volunteering
        if tenures is not UNSET:
            field_dict["tenures"] = tenures
        if career_began_at is not UNSET:
            field_dict["career_began_at"] = career_began_at
        if tags is not UNSET:
            field_dict["tags"] = tags
        if entity_urn is not UNSET:
            field_dict["entity_urn"] = entity_urn
        if open_to_work is not UNSET:
            field_dict["open_to_work"] = open_to_work
        if premium is not UNSET:
            field_dict["premium"] = premium
        if influencer is not UNSET:
            field_dict["influencer"] = influencer
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if entity_urns is not UNSET:
            field_dict["entity_urns"] = entity_urns
        if is_hiring is not UNSET:
            field_dict["is_hiring"] = is_hiring
        if current_job is not UNSET:
            field_dict["current_job"] = current_job
        if custom_data is not UNSET:
            field_dict["custom_data"] = custom_data
        if relevance_score is not UNSET:
            field_dict["relevance_score"] = relevance_score
        if last_sort_key is not UNSET:
            field_dict["last_sort_key"] = last_sort_key
        if languages is not UNSET:
            field_dict["languages"] = languages
        if detailed_education is not UNSET:
            field_dict["detailed_education"] = detailed_education
        if detailed_work_experiences is not UNSET:
            field_dict["detailed_work_experiences"] = detailed_work_experiences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_articles_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_certifications_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_courses_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_current_job_type_0 import (
            TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_custom_data_type_0 import (
            TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_detailed_education_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_detailed_work_experiences_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_education_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_experiences_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_inferred_location_type_0 import (
            TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_languages_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_organizations_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_patents_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_projects_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_publications_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_tenures_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item,
        )
        from ..models.text_to_combined_search_response_200_output_data_profiles_item_volunteering_type_0_item import (
            TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item,
        )

        d = dict(src_dict)
        primary_slug = d.pop("primary_slug")

        def _parse_articles(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                articles_type_0 = []
                _articles_type_0 = data
                for articles_type_0_item_data in _articles_type_0:
                    articles_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item.from_dict(
                            articles_type_0_item_data
                        )
                    )

                    articles_type_0.append(articles_type_0_item)

                return articles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemArticlesType0Item] | None | Unset, data
            )

        articles = _parse_articles(d.pop("articles", UNSET))

        def _parse_certifications(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                certifications_type_0 = []
                _certifications_type_0 = data
                for certifications_type_0_item_data in _certifications_type_0:
                    certifications_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item.from_dict(
                            certifications_type_0_item_data
                        )
                    )

                    certifications_type_0.append(certifications_type_0_item)

                return certifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemCertificationsType0Item] | None | Unset, data
            )

        certifications = _parse_certifications(d.pop("certifications", UNSET))

        def _parse_connection_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        connection_count = _parse_connection_count(d.pop("connection_count", UNSET))

        def _parse_courses(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                courses_type_0 = []
                _courses_type_0 = data
                for courses_type_0_item_data in _courses_type_0:
                    courses_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item.from_dict(
                            courses_type_0_item_data
                        )
                    )

                    courses_type_0.append(courses_type_0_item)

                return courses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemCoursesType0Item] | None | Unset, data
            )

        courses = _parse_courses(d.pop("courses", UNSET))

        def _parse_dob(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dob = _parse_dob(d.pop("dob", UNSET))

        def _parse_education(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                education_type_0 = []
                _education_type_0 = data
                for education_type_0_item_data in _education_type_0:
                    education_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item.from_dict(
                            education_type_0_item_data
                        )
                    )

                    education_type_0.append(education_type_0_item)

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemEducationType0Item] | None | Unset, data
            )

        education = _parse_education(d.pop("education", UNSET))

        def _parse_experiences(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experiences_type_0 = []
                _experiences_type_0 = data
                for experiences_type_0_item_data in _experiences_type_0:
                    experiences_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item.from_dict(
                            experiences_type_0_item_data
                        )
                    )

                    experiences_type_0.append(experiences_type_0_item)

                return experiences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemExperiencesType0Item] | None | Unset, data
            )

        experiences = _parse_experiences(d.pop("experiences", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_follower_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        follower_count = _parse_follower_count(d.pop("follower_count", UNSET))

        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))

        def _parse_industry_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry_name = _parse_industry_name(d.pop("industry_name", UNSET))

        def _parse_inferred_location(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inferred_location_type_0 = (
                    TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0.from_dict(data)
                )

                return inferred_location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCombinedSearchResponse200OutputDataProfilesItemInferredLocationType0 | Unset, data)

        inferred_location = _parse_inferred_location(d.pop("inferred_location", UNSET))

        def _parse_interests(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interests_type_0 = cast(list[str], data)

                return interests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        interests = _parse_interests(d.pop("interests", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_locality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality = _parse_locality(d.pop("locality", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_patents(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                patents_type_0 = []
                _patents_type_0 = data
                for patents_type_0_item_data in _patents_type_0:
                    patents_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item.from_dict(
                            patents_type_0_item_data
                        )
                    )

                    patents_type_0.append(patents_type_0_item)

                return patents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemPatentsType0Item] | None | Unset, data
            )

        patents = _parse_patents(d.pop("patents", UNSET))

        def _parse_profile_pic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_pic = _parse_profile_pic(d.pop("profile_pic", UNSET))

        def _parse_projects(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in _projects_type_0:
                    projects_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item.from_dict(
                            projects_type_0_item_data
                        )
                    )

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemProjectsType0Item] | None | Unset, data
            )

        projects = _parse_projects(d.pop("projects", UNSET))

        def _parse_publications(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                publications_type_0 = []
                _publications_type_0 = data
                for publications_type_0_item_data in _publications_type_0:
                    publications_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item.from_dict(
                            publications_type_0_item_data
                        )
                    )

                    publications_type_0.append(publications_type_0_item)

                return publications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemPublicationsType0Item] | None | Unset, data
            )

        publications = _parse_publications(d.pop("publications", UNSET))

        def _parse_skills(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = cast(list[str], data)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        skills = _parse_skills(d.pop("skills", UNSET))

        def _parse_slugs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slugs_type_0 = cast(list[str], data)

                return slugs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        slugs = _parse_slugs(d.pop("slugs", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_volunteering(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volunteering_type_0 = []
                _volunteering_type_0 = data
                for volunteering_type_0_item_data in _volunteering_type_0:
                    volunteering_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item.from_dict(
                            volunteering_type_0_item_data
                        )
                    )

                    volunteering_type_0.append(volunteering_type_0_item)

                return volunteering_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemVolunteeringType0Item] | None | Unset, data
            )

        volunteering = _parse_volunteering(d.pop("volunteering", UNSET))

        def _parse_tenures(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tenures_type_0 = []
                _tenures_type_0 = data
                for tenures_type_0_item_data in _tenures_type_0:
                    tenures_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item.from_dict(
                            tenures_type_0_item_data
                        )
                    )

                    tenures_type_0.append(tenures_type_0_item)

                return tenures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemTenuresType0Item] | None | Unset, data
            )

        tenures = _parse_tenures(d.pop("tenures", UNSET))

        def _parse_career_began_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        career_began_at = _parse_career_began_at(d.pop("career_began_at", UNSET))

        def _parse_tags(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemTagsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = TextToCombinedSearchResponse200OutputDataProfilesItemTagsType0Item(
                        tags_type_0_item_data
                    )

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TextToCombinedSearchResponse200OutputDataProfilesItemTagsType0Item] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_entity_urn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_urn = _parse_entity_urn(d.pop("entity_urn", UNSET))

        def _parse_open_to_work(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        open_to_work = _parse_open_to_work(d.pop("open_to_work", UNSET))

        def _parse_premium(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        premium = _parse_premium(d.pop("premium", UNSET))

        def _parse_influencer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        influencer = _parse_influencer(d.pop("influencer", UNSET))

        def _parse_organizations(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:
                    organizations_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item.from_dict(
                            organizations_type_0_item_data
                        )
                    )

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemOrganizationsType0Item] | None | Unset, data
            )

        organizations = _parse_organizations(d.pop("organizations", UNSET))

        def _parse_entity_urns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entity_urns_type_0 = cast(list[str], data)

                return entity_urns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        entity_urns = _parse_entity_urns(d.pop("entity_urns", UNSET))

        def _parse_is_hiring(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_hiring = _parse_is_hiring(d.pop("is_hiring", UNSET))

        def _parse_current_job(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_job_type_0 = TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0.from_dict(
                    data
                )

                return current_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCombinedSearchResponse200OutputDataProfilesItemCurrentJobType0 | Unset, data)

        current_job = _parse_current_job(d.pop("current_job", UNSET))

        def _parse_custom_data(
            data: object,
        ) -> None | TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_data_type_0 = TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0.from_dict(
                    data
                )

                return custom_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TextToCombinedSearchResponse200OutputDataProfilesItemCustomDataType0 | Unset, data)

        custom_data = _parse_custom_data(d.pop("custom_data", UNSET))

        def _parse_relevance_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        relevance_score = _parse_relevance_score(d.pop("relevance_score", UNSET))

        def _parse_last_sort_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sort_key = _parse_last_sort_key(d.pop("last_sort_key", UNSET))

        def _parse_languages(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                languages_type_0 = []
                _languages_type_0 = data
                for languages_type_0_item_data in _languages_type_0:
                    languages_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item.from_dict(
                            languages_type_0_item_data
                        )
                    )

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemLanguagesType0Item] | None | Unset, data
            )

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_detailed_education(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detailed_education_type_0 = []
                _detailed_education_type_0 = data
                for detailed_education_type_0_item_data in _detailed_education_type_0:
                    detailed_education_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item.from_dict(
                            detailed_education_type_0_item_data
                        )
                    )

                    detailed_education_type_0.append(detailed_education_type_0_item)

                return detailed_education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedEducationType0Item] | None | Unset,
                data,
            )

        detailed_education = _parse_detailed_education(d.pop("detailed_education", UNSET))

        def _parse_detailed_work_experiences(
            data: object,
        ) -> list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detailed_work_experiences_type_0 = []
                _detailed_work_experiences_type_0 = data
                for detailed_work_experiences_type_0_item_data in _detailed_work_experiences_type_0:
                    detailed_work_experiences_type_0_item = (
                        TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item.from_dict(
                            detailed_work_experiences_type_0_item_data
                        )
                    )

                    detailed_work_experiences_type_0.append(detailed_work_experiences_type_0_item)

                return detailed_work_experiences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[TextToCombinedSearchResponse200OutputDataProfilesItemDetailedWorkExperiencesType0Item]
                | None
                | Unset,
                data,
            )

        detailed_work_experiences = _parse_detailed_work_experiences(d.pop("detailed_work_experiences", UNSET))

        text_to_combined_search_response_200_output_data_profiles_item = cls(
            primary_slug=primary_slug,
            articles=articles,
            certifications=certifications,
            connection_count=connection_count,
            courses=courses,
            dob=dob,
            education=education,
            experiences=experiences,
            first_name=first_name,
            follower_count=follower_count,
            headline=headline,
            industry_name=industry_name,
            inferred_location=inferred_location,
            interests=interests,
            last_name=last_name,
            locality=locality,
            name=name,
            patents=patents,
            profile_pic=profile_pic,
            projects=projects,
            publications=publications,
            skills=skills,
            slugs=slugs,
            summary=summary,
            url=url,
            user_id=user_id,
            volunteering=volunteering,
            tenures=tenures,
            career_began_at=career_began_at,
            tags=tags,
            entity_urn=entity_urn,
            open_to_work=open_to_work,
            premium=premium,
            influencer=influencer,
            organizations=organizations,
            entity_urns=entity_urns,
            is_hiring=is_hiring,
            current_job=current_job,
            custom_data=custom_data,
            relevance_score=relevance_score,
            last_sort_key=last_sort_key,
            languages=languages,
            detailed_education=detailed_education,
            detailed_work_experiences=detailed_work_experiences,
        )

        text_to_combined_search_response_200_output_data_profiles_item.additional_properties = d
        return text_to_combined_search_response_200_output_data_profiles_item

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
