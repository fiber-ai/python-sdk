from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_kitchen_sink_person import GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkPerson
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_saved_search_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchCompany
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_company_posts import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiCompanyPosts
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_saved_search_prospect import GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchProspect
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PhoneReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_job_posting_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_github_lookup_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0GithubLookupAgent
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePersonalEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_email_from_github_username import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetEmailFromGithubUsername
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_google_maps_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0GoogleMapsScrape
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_combined_enrichment import GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedEnrichment
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_text_to_person_search_params import GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToPersonSearchParams
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveWorkEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumWorkEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_job_posting_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingCountFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PersonalEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumAllEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_person_for_contact_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPersonForContactReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_person_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonCountFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_company_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrape
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_standardize_company_slug import GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizeCompanySlug
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_posts import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfilePosts
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveAllEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0AllEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_company_logo_lookup import GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkCompanyLogoLookup
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_standardize_person_slug import GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizePersonSlug
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_validate_email import GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidateEmail
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_company_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyCountFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPersonalEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_investor_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestorFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_validate_phone import GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidatePhone
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_reactions import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileReactions
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_local_business_research_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0LocalBusinessResearchAgent
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_person_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavPersonScrape
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_person_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_company_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichCompany
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePhoneReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_person import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPerson
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_domain_lookup_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0DomainLookupAgent
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_kitchen_sink_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkCompany
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0WorkEmailReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup import GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_geolocation import GetOrgCreditsResponse200OutputCreditsPerOperationType0Geolocation
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_text_to_company_search_params import GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToCompanySearchParams
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_from_github_username import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileFromGithubUsername
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_email_to_linkedin_url import GetOrgCreditsResponse200OutputCreditsPerOperationType0EmailToLinkedinUrl
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_investment_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestmentFromDb
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_post_reactions import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostReactions
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_comments import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileComments
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPhoneReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveCombinedReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumCombinedReveal
  from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_post_comments import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostComments





T = TypeVar("T", bound="GetOrgCreditsResponse200OutputCreditsPerOperationType0")



@_attrs_define
class GetOrgCreditsResponse200OutputCreditsPerOperationType0:
    """ 
        Attributes:
            get_company_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyFromDb):
            get_person_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonFromDb):
            get_company_count_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyCountFromDb):
            get_job_posting_count_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingCountFromDb):
            get_person_count_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonCountFromDb):
            get_investor_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestorFromDb):
            get_investment_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestmentFromDb):
            get_job_posting_from_db (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingFromDb):
            text_to_company_search_params (GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToCompanySearchParams):
            text_to_person_search_params (GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToPersonSearchParams):
            live_enrich_company (GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichCompany):
            live_enrich_person (GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPerson):
            live_enrich_person_for_contact_reveal
                (GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPersonForContactReveal):
            standardize_company_slug (GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizeCompanySlug):
            standardize_person_slug (GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizePersonSlug):
            work_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0WorkEmailReveal):
            personal_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0PersonalEmailReveal):
            all_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0AllEmailReveal):
            phone_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0PhoneReveal):
            combined_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedReveal):
            validate_email (GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidateEmail):
            validate_phone (GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidatePhone):
            email_to_linkedin_url (GetOrgCreditsResponse200OutputCreditsPerOperationType0EmailToLinkedinUrl):
            kitchen_sink_person (GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkPerson):
            kitchen_sink_company (GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkCompany):
            sales_nav_company_scrape (GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrape):
            sales_nav_person_scrape (GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavPersonScrape):
            google_maps_scrape (GetOrgCreditsResponse200OutputCreditsPerOperationType0GoogleMapsScrape):
            geolocation (GetOrgCreditsResponse200OutputCreditsPerOperationType0Geolocation):
            combined_enrichment (GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedEnrichment):
            domain_lookup_agent (GetOrgCreditsResponse200OutputCreditsPerOperationType0DomainLookupAgent):
            local_business_research_agent
                (GetOrgCreditsResponse200OutputCreditsPerOperationType0LocalBusinessResearchAgent):
            github_lookup_agent (GetOrgCreditsResponse200OutputCreditsPerOperationType0GithubLookupAgent):
            get_li_profile_from_github_username
                (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileFromGithubUsername):
            get_email_from_github_username
                (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetEmailFromGithubUsername):
            bulk_company_logo_lookup (GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkCompanyLogoLookup):
            bulk_profile_pic_lookup (GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup):
            get_li_profile_posts (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfilePosts):
            get_li_company_posts (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiCompanyPosts):
            get_li_post_comments (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostComments):
            get_li_post_reactions (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostReactions):
            get_li_profile_comments (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileComments):
            get_li_profile_reactions (GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileReactions):
            saved_search_company (GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchCompany):
            saved_search_prospect (GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchProspect):
            premium_work_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumWorkEmailReveal):
            premium_personal_email_reveal
                (GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPersonalEmailReveal):
            premium_all_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumAllEmailReveal):
            premium_phone_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPhoneReveal):
            premium_combined_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumCombinedReveal):
            exhaustive_work_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveWorkEmailReveal):
            exhaustive_personal_email_reveal
                (GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePersonalEmailReveal):
            exhaustive_all_email_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveAllEmailReveal):
            exhaustive_phone_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePhoneReveal):
            exhaustive_combined_reveal (GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveCombinedReveal):
     """

    get_company_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyFromDb'
    get_person_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonFromDb'
    get_company_count_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyCountFromDb'
    get_job_posting_count_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingCountFromDb'
    get_person_count_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonCountFromDb'
    get_investor_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestorFromDb'
    get_investment_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestmentFromDb'
    get_job_posting_from_db: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingFromDb'
    text_to_company_search_params: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToCompanySearchParams'
    text_to_person_search_params: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToPersonSearchParams'
    live_enrich_company: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichCompany'
    live_enrich_person: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPerson'
    live_enrich_person_for_contact_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPersonForContactReveal'
    standardize_company_slug: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizeCompanySlug'
    standardize_person_slug: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizePersonSlug'
    work_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0WorkEmailReveal'
    personal_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PersonalEmailReveal'
    all_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0AllEmailReveal'
    phone_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PhoneReveal'
    combined_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedReveal'
    validate_email: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidateEmail'
    validate_phone: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidatePhone'
    email_to_linkedin_url: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0EmailToLinkedinUrl'
    kitchen_sink_person: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkPerson'
    kitchen_sink_company: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkCompany'
    sales_nav_company_scrape: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrape'
    sales_nav_person_scrape: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavPersonScrape'
    google_maps_scrape: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GoogleMapsScrape'
    geolocation: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0Geolocation'
    combined_enrichment: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedEnrichment'
    domain_lookup_agent: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0DomainLookupAgent'
    local_business_research_agent: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0LocalBusinessResearchAgent'
    github_lookup_agent: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GithubLookupAgent'
    get_li_profile_from_github_username: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileFromGithubUsername'
    get_email_from_github_username: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetEmailFromGithubUsername'
    bulk_company_logo_lookup: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkCompanyLogoLookup'
    bulk_profile_pic_lookup: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup'
    get_li_profile_posts: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfilePosts'
    get_li_company_posts: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiCompanyPosts'
    get_li_post_comments: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostComments'
    get_li_post_reactions: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostReactions'
    get_li_profile_comments: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileComments'
    get_li_profile_reactions: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileReactions'
    saved_search_company: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchCompany'
    saved_search_prospect: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchProspect'
    premium_work_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumWorkEmailReveal'
    premium_personal_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPersonalEmailReveal'
    premium_all_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumAllEmailReveal'
    premium_phone_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPhoneReveal'
    premium_combined_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumCombinedReveal'
    exhaustive_work_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveWorkEmailReveal'
    exhaustive_personal_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePersonalEmailReveal'
    exhaustive_all_email_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveAllEmailReveal'
    exhaustive_phone_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePhoneReveal'
    exhaustive_combined_reveal: 'GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveCombinedReveal'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_kitchen_sink_person import GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkPerson
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_saved_search_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchCompany
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_company_posts import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiCompanyPosts
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_saved_search_prospect import GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchProspect
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PhoneReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_job_posting_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_github_lookup_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0GithubLookupAgent
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePersonalEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_email_from_github_username import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetEmailFromGithubUsername
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_google_maps_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0GoogleMapsScrape
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_combined_enrichment import GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedEnrichment
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_text_to_person_search_params import GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToPersonSearchParams
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveWorkEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumWorkEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_job_posting_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingCountFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PersonalEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumAllEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_person_for_contact_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPersonForContactReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_person_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonCountFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_company_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrape
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_standardize_company_slug import GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizeCompanySlug
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_posts import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfilePosts
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveAllEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0AllEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_company_logo_lookup import GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkCompanyLogoLookup
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_standardize_person_slug import GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizePersonSlug
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_validate_email import GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidateEmail
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_company_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyCountFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPersonalEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_investor_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestorFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_validate_phone import GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidatePhone
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_reactions import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileReactions
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_local_business_research_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0LocalBusinessResearchAgent
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_person_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavPersonScrape
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_person_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_company_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichCompany
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePhoneReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_person import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPerson
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_domain_lookup_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0DomainLookupAgent
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_kitchen_sink_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkCompany
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0WorkEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup import GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_geolocation import GetOrgCreditsResponse200OutputCreditsPerOperationType0Geolocation
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_text_to_company_search_params import GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToCompanySearchParams
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_from_github_username import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileFromGithubUsername
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_email_to_linkedin_url import GetOrgCreditsResponse200OutputCreditsPerOperationType0EmailToLinkedinUrl
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_investment_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestmentFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_post_reactions import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostReactions
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_comments import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileComments
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPhoneReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveCombinedReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumCombinedReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_post_comments import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostComments
        get_company_from_db = self.get_company_from_db.to_dict()

        get_person_from_db = self.get_person_from_db.to_dict()

        get_company_count_from_db = self.get_company_count_from_db.to_dict()

        get_job_posting_count_from_db = self.get_job_posting_count_from_db.to_dict()

        get_person_count_from_db = self.get_person_count_from_db.to_dict()

        get_investor_from_db = self.get_investor_from_db.to_dict()

        get_investment_from_db = self.get_investment_from_db.to_dict()

        get_job_posting_from_db = self.get_job_posting_from_db.to_dict()

        text_to_company_search_params = self.text_to_company_search_params.to_dict()

        text_to_person_search_params = self.text_to_person_search_params.to_dict()

        live_enrich_company = self.live_enrich_company.to_dict()

        live_enrich_person = self.live_enrich_person.to_dict()

        live_enrich_person_for_contact_reveal = self.live_enrich_person_for_contact_reveal.to_dict()

        standardize_company_slug = self.standardize_company_slug.to_dict()

        standardize_person_slug = self.standardize_person_slug.to_dict()

        work_email_reveal = self.work_email_reveal.to_dict()

        personal_email_reveal = self.personal_email_reveal.to_dict()

        all_email_reveal = self.all_email_reveal.to_dict()

        phone_reveal = self.phone_reveal.to_dict()

        combined_reveal = self.combined_reveal.to_dict()

        validate_email = self.validate_email.to_dict()

        validate_phone = self.validate_phone.to_dict()

        email_to_linkedin_url = self.email_to_linkedin_url.to_dict()

        kitchen_sink_person = self.kitchen_sink_person.to_dict()

        kitchen_sink_company = self.kitchen_sink_company.to_dict()

        sales_nav_company_scrape = self.sales_nav_company_scrape.to_dict()

        sales_nav_person_scrape = self.sales_nav_person_scrape.to_dict()

        google_maps_scrape = self.google_maps_scrape.to_dict()

        geolocation = self.geolocation.to_dict()

        combined_enrichment = self.combined_enrichment.to_dict()

        domain_lookup_agent = self.domain_lookup_agent.to_dict()

        local_business_research_agent = self.local_business_research_agent.to_dict()

        github_lookup_agent = self.github_lookup_agent.to_dict()

        get_li_profile_from_github_username = self.get_li_profile_from_github_username.to_dict()

        get_email_from_github_username = self.get_email_from_github_username.to_dict()

        bulk_company_logo_lookup = self.bulk_company_logo_lookup.to_dict()

        bulk_profile_pic_lookup = self.bulk_profile_pic_lookup.to_dict()

        get_li_profile_posts = self.get_li_profile_posts.to_dict()

        get_li_company_posts = self.get_li_company_posts.to_dict()

        get_li_post_comments = self.get_li_post_comments.to_dict()

        get_li_post_reactions = self.get_li_post_reactions.to_dict()

        get_li_profile_comments = self.get_li_profile_comments.to_dict()

        get_li_profile_reactions = self.get_li_profile_reactions.to_dict()

        saved_search_company = self.saved_search_company.to_dict()

        saved_search_prospect = self.saved_search_prospect.to_dict()

        premium_work_email_reveal = self.premium_work_email_reveal.to_dict()

        premium_personal_email_reveal = self.premium_personal_email_reveal.to_dict()

        premium_all_email_reveal = self.premium_all_email_reveal.to_dict()

        premium_phone_reveal = self.premium_phone_reveal.to_dict()

        premium_combined_reveal = self.premium_combined_reveal.to_dict()

        exhaustive_work_email_reveal = self.exhaustive_work_email_reveal.to_dict()

        exhaustive_personal_email_reveal = self.exhaustive_personal_email_reveal.to_dict()

        exhaustive_all_email_reveal = self.exhaustive_all_email_reveal.to_dict()

        exhaustive_phone_reveal = self.exhaustive_phone_reveal.to_dict()

        exhaustive_combined_reveal = self.exhaustive_combined_reveal.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "getCompanyFromDb": get_company_from_db,
            "getPersonFromDb": get_person_from_db,
            "getCompanyCountFromDb": get_company_count_from_db,
            "getJobPostingCountFromDb": get_job_posting_count_from_db,
            "getPersonCountFromDb": get_person_count_from_db,
            "getInvestorFromDb": get_investor_from_db,
            "getInvestmentFromDb": get_investment_from_db,
            "getJobPostingFromDb": get_job_posting_from_db,
            "textToCompanySearchParams": text_to_company_search_params,
            "textToPersonSearchParams": text_to_person_search_params,
            "liveEnrichCompany": live_enrich_company,
            "liveEnrichPerson": live_enrich_person,
            "liveEnrichPersonForContactReveal": live_enrich_person_for_contact_reveal,
            "standardizeCompanySlug": standardize_company_slug,
            "standardizePersonSlug": standardize_person_slug,
            "workEmailReveal": work_email_reveal,
            "personalEmailReveal": personal_email_reveal,
            "allEmailReveal": all_email_reveal,
            "phoneReveal": phone_reveal,
            "combinedReveal": combined_reveal,
            "validateEmail": validate_email,
            "validatePhone": validate_phone,
            "emailToLinkedinUrl": email_to_linkedin_url,
            "kitchenSinkPerson": kitchen_sink_person,
            "kitchenSinkCompany": kitchen_sink_company,
            "salesNavCompanyScrape": sales_nav_company_scrape,
            "salesNavPersonScrape": sales_nav_person_scrape,
            "googleMapsScrape": google_maps_scrape,
            "geolocation": geolocation,
            "combinedEnrichment": combined_enrichment,
            "domainLookupAgent": domain_lookup_agent,
            "localBusinessResearchAgent": local_business_research_agent,
            "githubLookupAgent": github_lookup_agent,
            "getLiProfileFromGithubUsername": get_li_profile_from_github_username,
            "getEmailFromGithubUsername": get_email_from_github_username,
            "bulkCompanyLogoLookup": bulk_company_logo_lookup,
            "bulkProfilePicLookup": bulk_profile_pic_lookup,
            "getLiProfilePosts": get_li_profile_posts,
            "getLiCompanyPosts": get_li_company_posts,
            "getLiPostComments": get_li_post_comments,
            "getLiPostReactions": get_li_post_reactions,
            "getLiProfileComments": get_li_profile_comments,
            "getLiProfileReactions": get_li_profile_reactions,
            "savedSearchCompany": saved_search_company,
            "savedSearchProspect": saved_search_prospect,
            "premiumWorkEmailReveal": premium_work_email_reveal,
            "premiumPersonalEmailReveal": premium_personal_email_reveal,
            "premiumAllEmailReveal": premium_all_email_reveal,
            "premiumPhoneReveal": premium_phone_reveal,
            "premiumCombinedReveal": premium_combined_reveal,
            "exhaustiveWorkEmailReveal": exhaustive_work_email_reveal,
            "exhaustivePersonalEmailReveal": exhaustive_personal_email_reveal,
            "exhaustiveAllEmailReveal": exhaustive_all_email_reveal,
            "exhaustivePhoneReveal": exhaustive_phone_reveal,
            "exhaustiveCombinedReveal": exhaustive_combined_reveal,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_kitchen_sink_person import GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkPerson
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_saved_search_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchCompany
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_company_posts import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiCompanyPosts
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_saved_search_prospect import GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchProspect
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PhoneReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_job_posting_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_github_lookup_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0GithubLookupAgent
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePersonalEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_email_from_github_username import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetEmailFromGithubUsername
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_google_maps_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0GoogleMapsScrape
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_combined_enrichment import GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedEnrichment
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_text_to_person_search_params import GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToPersonSearchParams
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveWorkEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumWorkEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_job_posting_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingCountFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PersonalEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumAllEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_person_for_contact_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPersonForContactReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_person_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonCountFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_company_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrape
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_standardize_company_slug import GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizeCompanySlug
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_posts import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfilePosts
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveAllEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_all_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0AllEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_company_logo_lookup import GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkCompanyLogoLookup
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_standardize_person_slug import GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizePersonSlug
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_validate_email import GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidateEmail
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_company_count_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyCountFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_personal_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPersonalEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_investor_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestorFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_validate_phone import GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidatePhone
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_reactions import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileReactions
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_local_business_research_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0LocalBusinessResearchAgent
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_sales_nav_person_scrape import GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavPersonScrape
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_person_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_company_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichCompany
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePhoneReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_live_enrich_person import GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPerson
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_domain_lookup_agent import GetOrgCreditsResponse200OutputCreditsPerOperationType0DomainLookupAgent
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_kitchen_sink_company import GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkCompany
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_work_email_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0WorkEmailReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_bulk_profile_pic_lookup import GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_geolocation import GetOrgCreditsResponse200OutputCreditsPerOperationType0Geolocation
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_text_to_company_search_params import GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToCompanySearchParams
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_from_github_username import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileFromGithubUsername
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_email_to_linkedin_url import GetOrgCreditsResponse200OutputCreditsPerOperationType0EmailToLinkedinUrl
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_investment_from_db import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestmentFromDb
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_post_reactions import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostReactions
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_profile_comments import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileComments
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_phone_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPhoneReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_exhaustive_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveCombinedReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_premium_combined_reveal import GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumCombinedReveal
        from ..models.get_org_credits_response_200_output_credits_per_operation_type_0_get_li_post_comments import GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostComments
        d = dict(src_dict)
        get_company_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyFromDb.from_dict(d.pop("getCompanyFromDb"))




        get_person_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonFromDb.from_dict(d.pop("getPersonFromDb"))




        get_company_count_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetCompanyCountFromDb.from_dict(d.pop("getCompanyCountFromDb"))




        get_job_posting_count_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingCountFromDb.from_dict(d.pop("getJobPostingCountFromDb"))




        get_person_count_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetPersonCountFromDb.from_dict(d.pop("getPersonCountFromDb"))




        get_investor_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestorFromDb.from_dict(d.pop("getInvestorFromDb"))




        get_investment_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetInvestmentFromDb.from_dict(d.pop("getInvestmentFromDb"))




        get_job_posting_from_db = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetJobPostingFromDb.from_dict(d.pop("getJobPostingFromDb"))




        text_to_company_search_params = GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToCompanySearchParams.from_dict(d.pop("textToCompanySearchParams"))




        text_to_person_search_params = GetOrgCreditsResponse200OutputCreditsPerOperationType0TextToPersonSearchParams.from_dict(d.pop("textToPersonSearchParams"))




        live_enrich_company = GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichCompany.from_dict(d.pop("liveEnrichCompany"))




        live_enrich_person = GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPerson.from_dict(d.pop("liveEnrichPerson"))




        live_enrich_person_for_contact_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0LiveEnrichPersonForContactReveal.from_dict(d.pop("liveEnrichPersonForContactReveal"))




        standardize_company_slug = GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizeCompanySlug.from_dict(d.pop("standardizeCompanySlug"))




        standardize_person_slug = GetOrgCreditsResponse200OutputCreditsPerOperationType0StandardizePersonSlug.from_dict(d.pop("standardizePersonSlug"))




        work_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0WorkEmailReveal.from_dict(d.pop("workEmailReveal"))




        personal_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PersonalEmailReveal.from_dict(d.pop("personalEmailReveal"))




        all_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0AllEmailReveal.from_dict(d.pop("allEmailReveal"))




        phone_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PhoneReveal.from_dict(d.pop("phoneReveal"))




        combined_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedReveal.from_dict(d.pop("combinedReveal"))




        validate_email = GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidateEmail.from_dict(d.pop("validateEmail"))




        validate_phone = GetOrgCreditsResponse200OutputCreditsPerOperationType0ValidatePhone.from_dict(d.pop("validatePhone"))




        email_to_linkedin_url = GetOrgCreditsResponse200OutputCreditsPerOperationType0EmailToLinkedinUrl.from_dict(d.pop("emailToLinkedinUrl"))




        kitchen_sink_person = GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkPerson.from_dict(d.pop("kitchenSinkPerson"))




        kitchen_sink_company = GetOrgCreditsResponse200OutputCreditsPerOperationType0KitchenSinkCompany.from_dict(d.pop("kitchenSinkCompany"))




        sales_nav_company_scrape = GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavCompanyScrape.from_dict(d.pop("salesNavCompanyScrape"))




        sales_nav_person_scrape = GetOrgCreditsResponse200OutputCreditsPerOperationType0SalesNavPersonScrape.from_dict(d.pop("salesNavPersonScrape"))




        google_maps_scrape = GetOrgCreditsResponse200OutputCreditsPerOperationType0GoogleMapsScrape.from_dict(d.pop("googleMapsScrape"))




        geolocation = GetOrgCreditsResponse200OutputCreditsPerOperationType0Geolocation.from_dict(d.pop("geolocation"))




        combined_enrichment = GetOrgCreditsResponse200OutputCreditsPerOperationType0CombinedEnrichment.from_dict(d.pop("combinedEnrichment"))




        domain_lookup_agent = GetOrgCreditsResponse200OutputCreditsPerOperationType0DomainLookupAgent.from_dict(d.pop("domainLookupAgent"))




        local_business_research_agent = GetOrgCreditsResponse200OutputCreditsPerOperationType0LocalBusinessResearchAgent.from_dict(d.pop("localBusinessResearchAgent"))




        github_lookup_agent = GetOrgCreditsResponse200OutputCreditsPerOperationType0GithubLookupAgent.from_dict(d.pop("githubLookupAgent"))




        get_li_profile_from_github_username = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileFromGithubUsername.from_dict(d.pop("getLiProfileFromGithubUsername"))




        get_email_from_github_username = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetEmailFromGithubUsername.from_dict(d.pop("getEmailFromGithubUsername"))




        bulk_company_logo_lookup = GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkCompanyLogoLookup.from_dict(d.pop("bulkCompanyLogoLookup"))




        bulk_profile_pic_lookup = GetOrgCreditsResponse200OutputCreditsPerOperationType0BulkProfilePicLookup.from_dict(d.pop("bulkProfilePicLookup"))




        get_li_profile_posts = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfilePosts.from_dict(d.pop("getLiProfilePosts"))




        get_li_company_posts = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiCompanyPosts.from_dict(d.pop("getLiCompanyPosts"))




        get_li_post_comments = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostComments.from_dict(d.pop("getLiPostComments"))




        get_li_post_reactions = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiPostReactions.from_dict(d.pop("getLiPostReactions"))




        get_li_profile_comments = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileComments.from_dict(d.pop("getLiProfileComments"))




        get_li_profile_reactions = GetOrgCreditsResponse200OutputCreditsPerOperationType0GetLiProfileReactions.from_dict(d.pop("getLiProfileReactions"))




        saved_search_company = GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchCompany.from_dict(d.pop("savedSearchCompany"))




        saved_search_prospect = GetOrgCreditsResponse200OutputCreditsPerOperationType0SavedSearchProspect.from_dict(d.pop("savedSearchProspect"))




        premium_work_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumWorkEmailReveal.from_dict(d.pop("premiumWorkEmailReveal"))




        premium_personal_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPersonalEmailReveal.from_dict(d.pop("premiumPersonalEmailReveal"))




        premium_all_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumAllEmailReveal.from_dict(d.pop("premiumAllEmailReveal"))




        premium_phone_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumPhoneReveal.from_dict(d.pop("premiumPhoneReveal"))




        premium_combined_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0PremiumCombinedReveal.from_dict(d.pop("premiumCombinedReveal"))




        exhaustive_work_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveWorkEmailReveal.from_dict(d.pop("exhaustiveWorkEmailReveal"))




        exhaustive_personal_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePersonalEmailReveal.from_dict(d.pop("exhaustivePersonalEmailReveal"))




        exhaustive_all_email_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveAllEmailReveal.from_dict(d.pop("exhaustiveAllEmailReveal"))




        exhaustive_phone_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustivePhoneReveal.from_dict(d.pop("exhaustivePhoneReveal"))




        exhaustive_combined_reveal = GetOrgCreditsResponse200OutputCreditsPerOperationType0ExhaustiveCombinedReveal.from_dict(d.pop("exhaustiveCombinedReveal"))




        get_org_credits_response_200_output_credits_per_operation_type_0 = cls(
            get_company_from_db=get_company_from_db,
            get_person_from_db=get_person_from_db,
            get_company_count_from_db=get_company_count_from_db,
            get_job_posting_count_from_db=get_job_posting_count_from_db,
            get_person_count_from_db=get_person_count_from_db,
            get_investor_from_db=get_investor_from_db,
            get_investment_from_db=get_investment_from_db,
            get_job_posting_from_db=get_job_posting_from_db,
            text_to_company_search_params=text_to_company_search_params,
            text_to_person_search_params=text_to_person_search_params,
            live_enrich_company=live_enrich_company,
            live_enrich_person=live_enrich_person,
            live_enrich_person_for_contact_reveal=live_enrich_person_for_contact_reveal,
            standardize_company_slug=standardize_company_slug,
            standardize_person_slug=standardize_person_slug,
            work_email_reveal=work_email_reveal,
            personal_email_reveal=personal_email_reveal,
            all_email_reveal=all_email_reveal,
            phone_reveal=phone_reveal,
            combined_reveal=combined_reveal,
            validate_email=validate_email,
            validate_phone=validate_phone,
            email_to_linkedin_url=email_to_linkedin_url,
            kitchen_sink_person=kitchen_sink_person,
            kitchen_sink_company=kitchen_sink_company,
            sales_nav_company_scrape=sales_nav_company_scrape,
            sales_nav_person_scrape=sales_nav_person_scrape,
            google_maps_scrape=google_maps_scrape,
            geolocation=geolocation,
            combined_enrichment=combined_enrichment,
            domain_lookup_agent=domain_lookup_agent,
            local_business_research_agent=local_business_research_agent,
            github_lookup_agent=github_lookup_agent,
            get_li_profile_from_github_username=get_li_profile_from_github_username,
            get_email_from_github_username=get_email_from_github_username,
            bulk_company_logo_lookup=bulk_company_logo_lookup,
            bulk_profile_pic_lookup=bulk_profile_pic_lookup,
            get_li_profile_posts=get_li_profile_posts,
            get_li_company_posts=get_li_company_posts,
            get_li_post_comments=get_li_post_comments,
            get_li_post_reactions=get_li_post_reactions,
            get_li_profile_comments=get_li_profile_comments,
            get_li_profile_reactions=get_li_profile_reactions,
            saved_search_company=saved_search_company,
            saved_search_prospect=saved_search_prospect,
            premium_work_email_reveal=premium_work_email_reveal,
            premium_personal_email_reveal=premium_personal_email_reveal,
            premium_all_email_reveal=premium_all_email_reveal,
            premium_phone_reveal=premium_phone_reveal,
            premium_combined_reveal=premium_combined_reveal,
            exhaustive_work_email_reveal=exhaustive_work_email_reveal,
            exhaustive_personal_email_reveal=exhaustive_personal_email_reveal,
            exhaustive_all_email_reveal=exhaustive_all_email_reveal,
            exhaustive_phone_reveal=exhaustive_phone_reveal,
            exhaustive_combined_reveal=exhaustive_combined_reveal,
        )


        get_org_credits_response_200_output_credits_per_operation_type_0.additional_properties = d
        return get_org_credits_response_200_output_credits_per_operation_type_0

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
