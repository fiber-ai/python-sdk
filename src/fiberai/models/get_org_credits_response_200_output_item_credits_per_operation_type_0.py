from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_all_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0AllEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_blue_collar_job_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BlueCollarJobSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_bulk_company_logo_lookup import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkCompanyLogoLookup,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_bulk_profile_pic_lookup import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkProfilePicLookup,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_combined_enrichment import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedEnrichment,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_combined_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_domain_lookup_agent import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0DomainLookupAgent,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_email_to_linkedin_url import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0EmailToLinkedinUrl,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_all_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveAllEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_combined_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveCombinedReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_personal_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePersonalEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_phone_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePhoneReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_work_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveWorkEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_find_company_lookalikes import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindCompanyLookalikes,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_find_person_lookalikes import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindPersonLookalikes,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_flight_booking_page import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightBookingPage,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_flight_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_generate_depth_chart import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GenerateDepthChart,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_geolocation import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0Geolocation,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_count_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyCountFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_latest_li_post import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLatestLiPost,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_layoffs import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLayoffs,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_revenue import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyRevenue,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_department_size import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetDepartmentSize,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_email_from_github_username import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEmailFromGithubUsername,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_entity_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEntityFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_investment_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestmentFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_investor_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestorFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_job_posting_count_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingCountFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_job_posting_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_company_posts import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiCompanyPosts,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_post_comments import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostComments,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_post_reactions import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostReactions,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_comments import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileComments,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_from_github_username import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileFromGithubUsername,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_last_active_date import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLastActiveDate,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_latest_activities import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLatestActivities,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_posts import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfilePosts,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_reactions import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileReactions,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_person_count_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonCountFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_person_from_db import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonFromDb,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_profile_latest_li_post import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetProfileLatestLiPost,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_github_lookup_agent import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GithubLookupAgent,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_google_maps_scrape import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GoogleMapsScrape,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_hotel_property_lookup import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelPropertyLookup,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_hotel_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_job_title_rewrite import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0JobTitleRewrite,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_kitchen_sink_company import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkCompany,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_kitchen_sink_person import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkPerson,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_lite_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_lite_phone_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LitePhoneReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_lite_reverse_email_lookup import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteReverseEmailLookup,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_live_enrich_company import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichCompany,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_live_enrich_person import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPerson,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_live_enrich_person_for_contact_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPersonForContactReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_local_business_research_agent import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LocalBusinessResearchAgent,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_mosaic_row import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MosaicRow,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_multi_source_company_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourceCompanySearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_multi_source_person_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourcePersonSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_personal_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PersonalEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_phone_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PhoneReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_all_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumAllEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_combined_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumCombinedReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_personal_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPersonalEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_phone_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPhoneReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_work_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumWorkEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_real_estate_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0RealEstateSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_reverse_phone_lookup import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ReversePhoneLookup,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_sales_nav_company_scrape import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavCompanyScrape,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_sales_nav_person_scrape import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrape,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_sales_nav_person_scrape_without_live_fetch import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrapeWithoutLiveFetch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_saved_search_company import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchCompany,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_saved_search_prospect import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchProspect,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_scouting_report_company import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportCompany,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_scouting_report_person import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportPerson,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_media_finder_agent import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialMediaFinderAgent,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_details import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostDetails,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_quotes import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostQuotes,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_reactions import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReactions,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_replies import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReplies,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_reposts import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReposts,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_details import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserDetails,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_followers import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowers,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_following import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowing,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_mentions import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserMentions,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_posts import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserPosts,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_standardize_company_slug import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizeCompanySlug,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_standardize_person_slug import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizePersonSlug,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_text_to_company_search_params import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToCompanySearchParams,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_text_to_person_search_params import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToPersonSearchParams,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_text_to_search_params import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToSearchParams,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntity,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity_gold import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityGold,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity_platinum import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityPlatinum,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity_silver import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntitySilver,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_persons_job_changes import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackPersonsJobChanges,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_validate_email import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidateEmail,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_validate_phone import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidatePhone,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_webpage_scrape import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScrape,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_webpage_screenshot import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScreenshot,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_work_email_reveal import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WorkEmailReveal,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_channel_details import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeChannelDetails,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_search import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeSearch,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_comments import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoComments,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_details import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoDetails,
    )
    from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_transcript import (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoTranscript,
    )


T = TypeVar("T", bound="GetOrgCreditsResponse200OutputItemCreditsPerOperationType0")


@_attrs_define
class GetOrgCreditsResponse200OutputItemCreditsPerOperationType0:
    """
    Attributes:
        get_company_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyFromDb):
        get_person_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonFromDb):
        get_company_count_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyCountFromDb):
        get_job_posting_count_from_db
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingCountFromDb):
        get_person_count_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonCountFromDb):
        get_investor_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestorFromDb):
        get_investment_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestmentFromDb):
        get_job_posting_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingFromDb):
        text_to_company_search_params
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToCompanySearchParams):
        text_to_person_search_params
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToPersonSearchParams):
        text_to_search_params (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToSearchParams):
        live_enrich_company (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichCompany):
        live_enrich_person (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPerson):
        live_enrich_person_for_contact_reveal
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPersonForContactReveal):
        standardize_company_slug (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizeCompanySlug):
        standardize_person_slug (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizePersonSlug):
        work_email_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WorkEmailReveal):
        personal_email_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PersonalEmailReveal):
        lite_email_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteEmailReveal):
        lite_phone_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LitePhoneReveal):
        lite_reverse_email_lookup (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteReverseEmailLookup):
        all_email_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0AllEmailReveal):
        phone_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PhoneReveal):
        combined_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedReveal):
        validate_email (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidateEmail):
        validate_phone (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidatePhone):
        email_to_linkedin_url (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0EmailToLinkedinUrl):
        kitchen_sink_person (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkPerson):
        kitchen_sink_company (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkCompany):
        sales_nav_company_scrape (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavCompanyScrape):
        sales_nav_person_scrape (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrape):
        sales_nav_person_scrape_without_live_fetch
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrapeWithoutLiveFetch):
        google_maps_scrape (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GoogleMapsScrape):
        geolocation (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0Geolocation):
        job_title_rewrite (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0JobTitleRewrite):
        combined_enrichment (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedEnrichment):
        domain_lookup_agent (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0DomainLookupAgent):
        local_business_research_agent
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LocalBusinessResearchAgent):
        github_lookup_agent (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GithubLookupAgent):
        get_li_profile_from_github_username
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileFromGithubUsername):
        get_email_from_github_username
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEmailFromGithubUsername):
        social_media_finder_agent (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialMediaFinderAgent):
        bulk_company_logo_lookup (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkCompanyLogoLookup):
        bulk_profile_pic_lookup (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkProfilePicLookup):
        get_li_profile_posts (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfilePosts):
        get_li_company_posts (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiCompanyPosts):
        get_li_post_comments (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostComments):
        get_li_post_reactions (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostReactions):
        get_li_profile_comments (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileComments):
        get_li_profile_reactions (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileReactions):
        get_li_profile_latest_activities
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLatestActivities):
        get_li_profile_last_active_date
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLastActiveDate):
        get_profile_latest_li_post (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetProfileLatestLiPost):
        get_company_latest_li_post (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLatestLiPost):
        saved_search_company (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchCompany):
        saved_search_prospect (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchProspect):
        premium_work_email_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumWorkEmailReveal):
        premium_personal_email_reveal
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPersonalEmailReveal):
        premium_all_email_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumAllEmailReveal):
        premium_phone_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPhoneReveal):
        premium_combined_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumCombinedReveal):
        exhaustive_work_email_reveal
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveWorkEmailReveal):
        exhaustive_personal_email_reveal
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePersonalEmailReveal):
        exhaustive_all_email_reveal
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveAllEmailReveal):
        exhaustive_phone_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePhoneReveal):
        exhaustive_combined_reveal (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveCombinedReveal):
        get_company_revenue (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyRevenue):
        multi_source_company_search
            (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourceCompanySearch):
        multi_source_person_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourcePersonSearch):
        scouting_report_company (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportCompany):
        scouting_report_person (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportPerson):
        track_persons_job_changes (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackPersonsJobChanges):
        youtube_video_transcript (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoTranscript):
        youtube_video_details (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoDetails):
        youtube_video_comments (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoComments):
        youtube_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeSearch):
        youtube_channel_details (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeChannelDetails):
        social_user_details (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserDetails):
        social_user_posts (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserPosts):
        social_user_followers (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowers):
        social_user_following (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowing):
        social_post_details (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostDetails):
        social_post_replies (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReplies):
        social_post_quotes (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostQuotes):
        social_post_reposts (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReposts):
        social_post_reactions (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReactions):
        social_user_mentions (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserMentions):
        social_user_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserSearch):
        social_post_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostSearch):
        webpage_screenshot (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScreenshot):
        webpage_scrape (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScrape):
        generate_depth_chart (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GenerateDepthChart):
        real_estate_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0RealEstateSearch):
        flight_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightSearch):
        mosaic_row (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MosaicRow):
        get_entity_from_db (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEntityFromDb):
        track_entity (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntity):
        track_entity_silver (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntitySilver):
        track_entity_gold (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityGold):
        track_entity_platinum (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityPlatinum):
        blue_collar_job_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BlueCollarJobSearch):
        get_company_layoffs (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLayoffs):
        reverse_phone_lookup (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ReversePhoneLookup):
        find_company_lookalikes (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindCompanyLookalikes):
        find_person_lookalikes (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindPersonLookalikes):
        hotel_search (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelSearch):
        hotel_property_lookup (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelPropertyLookup):
        get_department_size (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetDepartmentSize):
        flight_booking_page (GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightBookingPage):
    """

    get_company_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyFromDb
    get_person_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonFromDb
    get_company_count_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyCountFromDb
    get_job_posting_count_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingCountFromDb
    get_person_count_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonCountFromDb
    get_investor_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestorFromDb
    get_investment_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestmentFromDb
    get_job_posting_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingFromDb
    text_to_company_search_params: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToCompanySearchParams
    text_to_person_search_params: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToPersonSearchParams
    text_to_search_params: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToSearchParams
    live_enrich_company: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichCompany
    live_enrich_person: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPerson
    live_enrich_person_for_contact_reveal: (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPersonForContactReveal
    )
    standardize_company_slug: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizeCompanySlug
    standardize_person_slug: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizePersonSlug
    work_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WorkEmailReveal
    personal_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PersonalEmailReveal
    lite_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteEmailReveal
    lite_phone_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LitePhoneReveal
    lite_reverse_email_lookup: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteReverseEmailLookup
    all_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0AllEmailReveal
    phone_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PhoneReveal
    combined_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedReveal
    validate_email: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidateEmail
    validate_phone: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidatePhone
    email_to_linkedin_url: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0EmailToLinkedinUrl
    kitchen_sink_person: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkPerson
    kitchen_sink_company: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkCompany
    sales_nav_company_scrape: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavCompanyScrape
    sales_nav_person_scrape: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrape
    sales_nav_person_scrape_without_live_fetch: (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrapeWithoutLiveFetch
    )
    google_maps_scrape: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GoogleMapsScrape
    geolocation: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0Geolocation
    job_title_rewrite: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0JobTitleRewrite
    combined_enrichment: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedEnrichment
    domain_lookup_agent: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0DomainLookupAgent
    local_business_research_agent: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LocalBusinessResearchAgent
    github_lookup_agent: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GithubLookupAgent
    get_li_profile_from_github_username: (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileFromGithubUsername
    )
    get_email_from_github_username: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEmailFromGithubUsername
    social_media_finder_agent: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialMediaFinderAgent
    bulk_company_logo_lookup: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkCompanyLogoLookup
    bulk_profile_pic_lookup: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkProfilePicLookup
    get_li_profile_posts: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfilePosts
    get_li_company_posts: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiCompanyPosts
    get_li_post_comments: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostComments
    get_li_post_reactions: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostReactions
    get_li_profile_comments: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileComments
    get_li_profile_reactions: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileReactions
    get_li_profile_latest_activities: (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLatestActivities
    )
    get_li_profile_last_active_date: (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLastActiveDate
    )
    get_profile_latest_li_post: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetProfileLatestLiPost
    get_company_latest_li_post: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLatestLiPost
    saved_search_company: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchCompany
    saved_search_prospect: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchProspect
    premium_work_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumWorkEmailReveal
    premium_personal_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPersonalEmailReveal
    premium_all_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumAllEmailReveal
    premium_phone_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPhoneReveal
    premium_combined_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumCombinedReveal
    exhaustive_work_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveWorkEmailReveal
    exhaustive_personal_email_reveal: (
        GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePersonalEmailReveal
    )
    exhaustive_all_email_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveAllEmailReveal
    exhaustive_phone_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePhoneReveal
    exhaustive_combined_reveal: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveCombinedReveal
    get_company_revenue: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyRevenue
    multi_source_company_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourceCompanySearch
    multi_source_person_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourcePersonSearch
    scouting_report_company: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportCompany
    scouting_report_person: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportPerson
    track_persons_job_changes: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackPersonsJobChanges
    youtube_video_transcript: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoTranscript
    youtube_video_details: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoDetails
    youtube_video_comments: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoComments
    youtube_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeSearch
    youtube_channel_details: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeChannelDetails
    social_user_details: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserDetails
    social_user_posts: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserPosts
    social_user_followers: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowers
    social_user_following: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowing
    social_post_details: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostDetails
    social_post_replies: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReplies
    social_post_quotes: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostQuotes
    social_post_reposts: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReposts
    social_post_reactions: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReactions
    social_user_mentions: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserMentions
    social_user_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserSearch
    social_post_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostSearch
    webpage_screenshot: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScreenshot
    webpage_scrape: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScrape
    generate_depth_chart: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GenerateDepthChart
    real_estate_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0RealEstateSearch
    flight_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightSearch
    mosaic_row: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MosaicRow
    get_entity_from_db: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEntityFromDb
    track_entity: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntity
    track_entity_silver: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntitySilver
    track_entity_gold: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityGold
    track_entity_platinum: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityPlatinum
    blue_collar_job_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BlueCollarJobSearch
    get_company_layoffs: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLayoffs
    reverse_phone_lookup: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ReversePhoneLookup
    find_company_lookalikes: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindCompanyLookalikes
    find_person_lookalikes: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindPersonLookalikes
    hotel_search: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelSearch
    hotel_property_lookup: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelPropertyLookup
    get_department_size: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetDepartmentSize
    flight_booking_page: GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightBookingPage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_validate_phone import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidatePhone,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_webpage_scrape import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScrape,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_webpage_screenshot import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScreenshot,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_work_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WorkEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_channel_details import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeChannelDetails,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_comments import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoComments,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_details import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoDetails,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_transcript import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoTranscript,
        )

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

        text_to_search_params = self.text_to_search_params.to_dict()

        live_enrich_company = self.live_enrich_company.to_dict()

        live_enrich_person = self.live_enrich_person.to_dict()

        live_enrich_person_for_contact_reveal = self.live_enrich_person_for_contact_reveal.to_dict()

        standardize_company_slug = self.standardize_company_slug.to_dict()

        standardize_person_slug = self.standardize_person_slug.to_dict()

        work_email_reveal = self.work_email_reveal.to_dict()

        personal_email_reveal = self.personal_email_reveal.to_dict()

        lite_email_reveal = self.lite_email_reveal.to_dict()

        lite_phone_reveal = self.lite_phone_reveal.to_dict()

        lite_reverse_email_lookup = self.lite_reverse_email_lookup.to_dict()

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

        sales_nav_person_scrape_without_live_fetch = self.sales_nav_person_scrape_without_live_fetch.to_dict()

        google_maps_scrape = self.google_maps_scrape.to_dict()

        geolocation = self.geolocation.to_dict()

        job_title_rewrite = self.job_title_rewrite.to_dict()

        combined_enrichment = self.combined_enrichment.to_dict()

        domain_lookup_agent = self.domain_lookup_agent.to_dict()

        local_business_research_agent = self.local_business_research_agent.to_dict()

        github_lookup_agent = self.github_lookup_agent.to_dict()

        get_li_profile_from_github_username = self.get_li_profile_from_github_username.to_dict()

        get_email_from_github_username = self.get_email_from_github_username.to_dict()

        social_media_finder_agent = self.social_media_finder_agent.to_dict()

        bulk_company_logo_lookup = self.bulk_company_logo_lookup.to_dict()

        bulk_profile_pic_lookup = self.bulk_profile_pic_lookup.to_dict()

        get_li_profile_posts = self.get_li_profile_posts.to_dict()

        get_li_company_posts = self.get_li_company_posts.to_dict()

        get_li_post_comments = self.get_li_post_comments.to_dict()

        get_li_post_reactions = self.get_li_post_reactions.to_dict()

        get_li_profile_comments = self.get_li_profile_comments.to_dict()

        get_li_profile_reactions = self.get_li_profile_reactions.to_dict()

        get_li_profile_latest_activities = self.get_li_profile_latest_activities.to_dict()

        get_li_profile_last_active_date = self.get_li_profile_last_active_date.to_dict()

        get_profile_latest_li_post = self.get_profile_latest_li_post.to_dict()

        get_company_latest_li_post = self.get_company_latest_li_post.to_dict()

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

        get_company_revenue = self.get_company_revenue.to_dict()

        multi_source_company_search = self.multi_source_company_search.to_dict()

        multi_source_person_search = self.multi_source_person_search.to_dict()

        scouting_report_company = self.scouting_report_company.to_dict()

        scouting_report_person = self.scouting_report_person.to_dict()

        track_persons_job_changes = self.track_persons_job_changes.to_dict()

        youtube_video_transcript = self.youtube_video_transcript.to_dict()

        youtube_video_details = self.youtube_video_details.to_dict()

        youtube_video_comments = self.youtube_video_comments.to_dict()

        youtube_search = self.youtube_search.to_dict()

        youtube_channel_details = self.youtube_channel_details.to_dict()

        social_user_details = self.social_user_details.to_dict()

        social_user_posts = self.social_user_posts.to_dict()

        social_user_followers = self.social_user_followers.to_dict()

        social_user_following = self.social_user_following.to_dict()

        social_post_details = self.social_post_details.to_dict()

        social_post_replies = self.social_post_replies.to_dict()

        social_post_quotes = self.social_post_quotes.to_dict()

        social_post_reposts = self.social_post_reposts.to_dict()

        social_post_reactions = self.social_post_reactions.to_dict()

        social_user_mentions = self.social_user_mentions.to_dict()

        social_user_search = self.social_user_search.to_dict()

        social_post_search = self.social_post_search.to_dict()

        webpage_screenshot = self.webpage_screenshot.to_dict()

        webpage_scrape = self.webpage_scrape.to_dict()

        generate_depth_chart = self.generate_depth_chart.to_dict()

        real_estate_search = self.real_estate_search.to_dict()

        flight_search = self.flight_search.to_dict()

        mosaic_row = self.mosaic_row.to_dict()

        get_entity_from_db = self.get_entity_from_db.to_dict()

        track_entity = self.track_entity.to_dict()

        track_entity_silver = self.track_entity_silver.to_dict()

        track_entity_gold = self.track_entity_gold.to_dict()

        track_entity_platinum = self.track_entity_platinum.to_dict()

        blue_collar_job_search = self.blue_collar_job_search.to_dict()

        get_company_layoffs = self.get_company_layoffs.to_dict()

        reverse_phone_lookup = self.reverse_phone_lookup.to_dict()

        find_company_lookalikes = self.find_company_lookalikes.to_dict()

        find_person_lookalikes = self.find_person_lookalikes.to_dict()

        hotel_search = self.hotel_search.to_dict()

        hotel_property_lookup = self.hotel_property_lookup.to_dict()

        get_department_size = self.get_department_size.to_dict()

        flight_booking_page = self.flight_booking_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
                "textToSearchParams": text_to_search_params,
                "liveEnrichCompany": live_enrich_company,
                "liveEnrichPerson": live_enrich_person,
                "liveEnrichPersonForContactReveal": live_enrich_person_for_contact_reveal,
                "standardizeCompanySlug": standardize_company_slug,
                "standardizePersonSlug": standardize_person_slug,
                "workEmailReveal": work_email_reveal,
                "personalEmailReveal": personal_email_reveal,
                "liteEmailReveal": lite_email_reveal,
                "litePhoneReveal": lite_phone_reveal,
                "liteReverseEmailLookup": lite_reverse_email_lookup,
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
                "salesNavPersonScrapeWithoutLiveFetch": sales_nav_person_scrape_without_live_fetch,
                "googleMapsScrape": google_maps_scrape,
                "geolocation": geolocation,
                "jobTitleRewrite": job_title_rewrite,
                "combinedEnrichment": combined_enrichment,
                "domainLookupAgent": domain_lookup_agent,
                "localBusinessResearchAgent": local_business_research_agent,
                "githubLookupAgent": github_lookup_agent,
                "getLiProfileFromGithubUsername": get_li_profile_from_github_username,
                "getEmailFromGithubUsername": get_email_from_github_username,
                "socialMediaFinderAgent": social_media_finder_agent,
                "bulkCompanyLogoLookup": bulk_company_logo_lookup,
                "bulkProfilePicLookup": bulk_profile_pic_lookup,
                "getLiProfilePosts": get_li_profile_posts,
                "getLiCompanyPosts": get_li_company_posts,
                "getLiPostComments": get_li_post_comments,
                "getLiPostReactions": get_li_post_reactions,
                "getLiProfileComments": get_li_profile_comments,
                "getLiProfileReactions": get_li_profile_reactions,
                "getLiProfileLatestActivities": get_li_profile_latest_activities,
                "getLiProfileLastActiveDate": get_li_profile_last_active_date,
                "getProfileLatestLiPost": get_profile_latest_li_post,
                "getCompanyLatestLiPost": get_company_latest_li_post,
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
                "getCompanyRevenue": get_company_revenue,
                "multiSourceCompanySearch": multi_source_company_search,
                "multiSourcePersonSearch": multi_source_person_search,
                "scoutingReportCompany": scouting_report_company,
                "scoutingReportPerson": scouting_report_person,
                "trackPersonsJobChanges": track_persons_job_changes,
                "youtubeVideoTranscript": youtube_video_transcript,
                "youtubeVideoDetails": youtube_video_details,
                "youtubeVideoComments": youtube_video_comments,
                "youtubeSearch": youtube_search,
                "youtubeChannelDetails": youtube_channel_details,
                "socialUserDetails": social_user_details,
                "socialUserPosts": social_user_posts,
                "socialUserFollowers": social_user_followers,
                "socialUserFollowing": social_user_following,
                "socialPostDetails": social_post_details,
                "socialPostReplies": social_post_replies,
                "socialPostQuotes": social_post_quotes,
                "socialPostReposts": social_post_reposts,
                "socialPostReactions": social_post_reactions,
                "socialUserMentions": social_user_mentions,
                "socialUserSearch": social_user_search,
                "socialPostSearch": social_post_search,
                "webpageScreenshot": webpage_screenshot,
                "webpageScrape": webpage_scrape,
                "generateDepthChart": generate_depth_chart,
                "realEstateSearch": real_estate_search,
                "flightSearch": flight_search,
                "mosaicRow": mosaic_row,
                "getEntityFromDb": get_entity_from_db,
                "trackEntity": track_entity,
                "trackEntitySilver": track_entity_silver,
                "trackEntityGold": track_entity_gold,
                "trackEntityPlatinum": track_entity_platinum,
                "blueCollarJobSearch": blue_collar_job_search,
                "getCompanyLayoffs": get_company_layoffs,
                "reversePhoneLookup": reverse_phone_lookup,
                "findCompanyLookalikes": find_company_lookalikes,
                "findPersonLookalikes": find_person_lookalikes,
                "hotelSearch": hotel_search,
                "hotelPropertyLookup": hotel_property_lookup,
                "getDepartmentSize": get_department_size,
                "flightBookingPage": flight_booking_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_all_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0AllEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_blue_collar_job_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BlueCollarJobSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_bulk_company_logo_lookup import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkCompanyLogoLookup,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_bulk_profile_pic_lookup import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkProfilePicLookup,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_combined_enrichment import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedEnrichment,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_combined_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_domain_lookup_agent import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0DomainLookupAgent,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_email_to_linkedin_url import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0EmailToLinkedinUrl,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_all_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveAllEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_combined_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveCombinedReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_personal_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePersonalEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_phone_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePhoneReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_exhaustive_work_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveWorkEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_find_company_lookalikes import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindCompanyLookalikes,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_find_person_lookalikes import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindPersonLookalikes,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_flight_booking_page import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightBookingPage,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_flight_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_generate_depth_chart import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GenerateDepthChart,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_geolocation import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0Geolocation,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_count_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyCountFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_latest_li_post import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLatestLiPost,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_layoffs import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLayoffs,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_company_revenue import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyRevenue,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_department_size import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetDepartmentSize,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_email_from_github_username import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEmailFromGithubUsername,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_entity_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEntityFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_investment_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestmentFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_investor_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestorFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_job_posting_count_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingCountFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_job_posting_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_company_posts import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiCompanyPosts,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_post_comments import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostComments,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_post_reactions import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostReactions,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_comments import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileComments,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_from_github_username import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileFromGithubUsername,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_last_active_date import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLastActiveDate,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_latest_activities import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLatestActivities,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_posts import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfilePosts,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_li_profile_reactions import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileReactions,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_person_count_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonCountFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_person_from_db import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonFromDb,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_get_profile_latest_li_post import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetProfileLatestLiPost,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_github_lookup_agent import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GithubLookupAgent,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_google_maps_scrape import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GoogleMapsScrape,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_hotel_property_lookup import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelPropertyLookup,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_hotel_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_job_title_rewrite import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0JobTitleRewrite,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_kitchen_sink_company import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkCompany,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_kitchen_sink_person import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkPerson,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_lite_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_lite_phone_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LitePhoneReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_lite_reverse_email_lookup import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteReverseEmailLookup,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_live_enrich_company import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichCompany,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_live_enrich_person import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPerson,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_live_enrich_person_for_contact_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPersonForContactReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_local_business_research_agent import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LocalBusinessResearchAgent,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_mosaic_row import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MosaicRow,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_multi_source_company_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourceCompanySearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_multi_source_person_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourcePersonSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_personal_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PersonalEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_phone_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PhoneReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_all_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumAllEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_combined_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumCombinedReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_personal_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPersonalEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_phone_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPhoneReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_premium_work_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumWorkEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_real_estate_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0RealEstateSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_reverse_phone_lookup import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ReversePhoneLookup,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_sales_nav_company_scrape import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavCompanyScrape,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_sales_nav_person_scrape import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrape,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_sales_nav_person_scrape_without_live_fetch import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrapeWithoutLiveFetch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_saved_search_company import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchCompany,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_saved_search_prospect import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchProspect,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_scouting_report_company import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportCompany,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_scouting_report_person import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportPerson,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_media_finder_agent import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialMediaFinderAgent,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_details import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostDetails,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_quotes import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostQuotes,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_reactions import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReactions,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_replies import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReplies,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_reposts import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReposts,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_post_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_details import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserDetails,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_followers import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowers,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_following import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowing,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_mentions import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserMentions,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_posts import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserPosts,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_social_user_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_standardize_company_slug import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizeCompanySlug,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_standardize_person_slug import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizePersonSlug,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_text_to_company_search_params import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToCompanySearchParams,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_text_to_person_search_params import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToPersonSearchParams,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_text_to_search_params import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToSearchParams,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntity,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity_gold import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityGold,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity_platinum import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityPlatinum,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_entity_silver import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntitySilver,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_track_persons_job_changes import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackPersonsJobChanges,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_validate_email import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidateEmail,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_validate_phone import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidatePhone,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_webpage_scrape import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScrape,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_webpage_screenshot import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScreenshot,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_work_email_reveal import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WorkEmailReveal,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_channel_details import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeChannelDetails,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_search import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeSearch,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_comments import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoComments,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_details import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoDetails,
        )
        from ..models.get_org_credits_response_200_output_item_credits_per_operation_type_0_youtube_video_transcript import (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoTranscript,
        )

        d = dict(src_dict)
        get_company_from_db = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyFromDb.from_dict(
            d.pop("getCompanyFromDb")
        )

        get_person_from_db = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonFromDb.from_dict(
            d.pop("getPersonFromDb")
        )

        get_company_count_from_db = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyCountFromDb.from_dict(
                d.pop("getCompanyCountFromDb")
            )
        )

        get_job_posting_count_from_db = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingCountFromDb.from_dict(
                d.pop("getJobPostingCountFromDb")
            )
        )

        get_person_count_from_db = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetPersonCountFromDb.from_dict(
                d.pop("getPersonCountFromDb")
            )
        )

        get_investor_from_db = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestorFromDb.from_dict(
            d.pop("getInvestorFromDb")
        )

        get_investment_from_db = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetInvestmentFromDb.from_dict(
                d.pop("getInvestmentFromDb")
            )
        )

        get_job_posting_from_db = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetJobPostingFromDb.from_dict(
                d.pop("getJobPostingFromDb")
            )
        )

        text_to_company_search_params = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToCompanySearchParams.from_dict(
                d.pop("textToCompanySearchParams")
            )
        )

        text_to_person_search_params = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToPersonSearchParams.from_dict(
                d.pop("textToPersonSearchParams")
            )
        )

        text_to_search_params = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TextToSearchParams.from_dict(
            d.pop("textToSearchParams")
        )

        live_enrich_company = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichCompany.from_dict(
            d.pop("liveEnrichCompany")
        )

        live_enrich_person = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPerson.from_dict(
            d.pop("liveEnrichPerson")
        )

        live_enrich_person_for_contact_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiveEnrichPersonForContactReveal.from_dict(
                d.pop("liveEnrichPersonForContactReveal")
            )
        )

        standardize_company_slug = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizeCompanySlug.from_dict(
                d.pop("standardizeCompanySlug")
            )
        )

        standardize_person_slug = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0StandardizePersonSlug.from_dict(
                d.pop("standardizePersonSlug")
            )
        )

        work_email_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WorkEmailReveal.from_dict(
            d.pop("workEmailReveal")
        )

        personal_email_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PersonalEmailReveal.from_dict(
            d.pop("personalEmailReveal")
        )

        lite_email_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteEmailReveal.from_dict(
            d.pop("liteEmailReveal")
        )

        lite_phone_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LitePhoneReveal.from_dict(
            d.pop("litePhoneReveal")
        )

        lite_reverse_email_lookup = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LiteReverseEmailLookup.from_dict(
                d.pop("liteReverseEmailLookup")
            )
        )

        all_email_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0AllEmailReveal.from_dict(
            d.pop("allEmailReveal")
        )

        phone_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PhoneReveal.from_dict(
            d.pop("phoneReveal")
        )

        combined_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedReveal.from_dict(
            d.pop("combinedReveal")
        )

        validate_email = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidateEmail.from_dict(
            d.pop("validateEmail")
        )

        validate_phone = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ValidatePhone.from_dict(
            d.pop("validatePhone")
        )

        email_to_linkedin_url = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0EmailToLinkedinUrl.from_dict(
            d.pop("emailToLinkedinUrl")
        )

        kitchen_sink_person = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkPerson.from_dict(
            d.pop("kitchenSinkPerson")
        )

        kitchen_sink_company = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0KitchenSinkCompany.from_dict(
            d.pop("kitchenSinkCompany")
        )

        sales_nav_company_scrape = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavCompanyScrape.from_dict(
                d.pop("salesNavCompanyScrape")
            )
        )

        sales_nav_person_scrape = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrape.from_dict(
                d.pop("salesNavPersonScrape")
            )
        )

        sales_nav_person_scrape_without_live_fetch = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SalesNavPersonScrapeWithoutLiveFetch.from_dict(
                d.pop("salesNavPersonScrapeWithoutLiveFetch")
            )
        )

        google_maps_scrape = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GoogleMapsScrape.from_dict(
            d.pop("googleMapsScrape")
        )

        geolocation = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0Geolocation.from_dict(
            d.pop("geolocation")
        )

        job_title_rewrite = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0JobTitleRewrite.from_dict(
            d.pop("jobTitleRewrite")
        )

        combined_enrichment = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0CombinedEnrichment.from_dict(
            d.pop("combinedEnrichment")
        )

        domain_lookup_agent = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0DomainLookupAgent.from_dict(
            d.pop("domainLookupAgent")
        )

        local_business_research_agent = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0LocalBusinessResearchAgent.from_dict(
                d.pop("localBusinessResearchAgent")
            )
        )

        github_lookup_agent = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GithubLookupAgent.from_dict(
            d.pop("githubLookupAgent")
        )

        get_li_profile_from_github_username = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileFromGithubUsername.from_dict(
                d.pop("getLiProfileFromGithubUsername")
            )
        )

        get_email_from_github_username = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEmailFromGithubUsername.from_dict(
                d.pop("getEmailFromGithubUsername")
            )
        )

        social_media_finder_agent = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialMediaFinderAgent.from_dict(
                d.pop("socialMediaFinderAgent")
            )
        )

        bulk_company_logo_lookup = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkCompanyLogoLookup.from_dict(
                d.pop("bulkCompanyLogoLookup")
            )
        )

        bulk_profile_pic_lookup = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BulkProfilePicLookup.from_dict(
                d.pop("bulkProfilePicLookup")
            )
        )

        get_li_profile_posts = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfilePosts.from_dict(
            d.pop("getLiProfilePosts")
        )

        get_li_company_posts = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiCompanyPosts.from_dict(
            d.pop("getLiCompanyPosts")
        )

        get_li_post_comments = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostComments.from_dict(
            d.pop("getLiPostComments")
        )

        get_li_post_reactions = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiPostReactions.from_dict(
            d.pop("getLiPostReactions")
        )

        get_li_profile_comments = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileComments.from_dict(
                d.pop("getLiProfileComments")
            )
        )

        get_li_profile_reactions = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileReactions.from_dict(
                d.pop("getLiProfileReactions")
            )
        )

        get_li_profile_latest_activities = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLatestActivities.from_dict(
                d.pop("getLiProfileLatestActivities")
            )
        )

        get_li_profile_last_active_date = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetLiProfileLastActiveDate.from_dict(
                d.pop("getLiProfileLastActiveDate")
            )
        )

        get_profile_latest_li_post = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetProfileLatestLiPost.from_dict(
                d.pop("getProfileLatestLiPost")
            )
        )

        get_company_latest_li_post = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLatestLiPost.from_dict(
                d.pop("getCompanyLatestLiPost")
            )
        )

        saved_search_company = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchCompany.from_dict(
            d.pop("savedSearchCompany")
        )

        saved_search_prospect = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SavedSearchProspect.from_dict(
            d.pop("savedSearchProspect")
        )

        premium_work_email_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumWorkEmailReveal.from_dict(
                d.pop("premiumWorkEmailReveal")
            )
        )

        premium_personal_email_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPersonalEmailReveal.from_dict(
                d.pop("premiumPersonalEmailReveal")
            )
        )

        premium_all_email_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumAllEmailReveal.from_dict(
                d.pop("premiumAllEmailReveal")
            )
        )

        premium_phone_reveal = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumPhoneReveal.from_dict(
            d.pop("premiumPhoneReveal")
        )

        premium_combined_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0PremiumCombinedReveal.from_dict(
                d.pop("premiumCombinedReveal")
            )
        )

        exhaustive_work_email_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveWorkEmailReveal.from_dict(
                d.pop("exhaustiveWorkEmailReveal")
            )
        )

        exhaustive_personal_email_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePersonalEmailReveal.from_dict(
                d.pop("exhaustivePersonalEmailReveal")
            )
        )

        exhaustive_all_email_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveAllEmailReveal.from_dict(
                d.pop("exhaustiveAllEmailReveal")
            )
        )

        exhaustive_phone_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustivePhoneReveal.from_dict(
                d.pop("exhaustivePhoneReveal")
            )
        )

        exhaustive_combined_reveal = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ExhaustiveCombinedReveal.from_dict(
                d.pop("exhaustiveCombinedReveal")
            )
        )

        get_company_revenue = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyRevenue.from_dict(
            d.pop("getCompanyRevenue")
        )

        multi_source_company_search = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourceCompanySearch.from_dict(
                d.pop("multiSourceCompanySearch")
            )
        )

        multi_source_person_search = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MultiSourcePersonSearch.from_dict(
                d.pop("multiSourcePersonSearch")
            )
        )

        scouting_report_company = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportCompany.from_dict(
                d.pop("scoutingReportCompany")
            )
        )

        scouting_report_person = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ScoutingReportPerson.from_dict(
                d.pop("scoutingReportPerson")
            )
        )

        track_persons_job_changes = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackPersonsJobChanges.from_dict(
                d.pop("trackPersonsJobChanges")
            )
        )

        youtube_video_transcript = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoTranscript.from_dict(
                d.pop("youtubeVideoTranscript")
            )
        )

        youtube_video_details = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoDetails.from_dict(
            d.pop("youtubeVideoDetails")
        )

        youtube_video_comments = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeVideoComments.from_dict(
                d.pop("youtubeVideoComments")
            )
        )

        youtube_search = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeSearch.from_dict(
            d.pop("youtubeSearch")
        )

        youtube_channel_details = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0YoutubeChannelDetails.from_dict(
                d.pop("youtubeChannelDetails")
            )
        )

        social_user_details = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserDetails.from_dict(
            d.pop("socialUserDetails")
        )

        social_user_posts = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserPosts.from_dict(
            d.pop("socialUserPosts")
        )

        social_user_followers = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowers.from_dict(
            d.pop("socialUserFollowers")
        )

        social_user_following = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserFollowing.from_dict(
            d.pop("socialUserFollowing")
        )

        social_post_details = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostDetails.from_dict(
            d.pop("socialPostDetails")
        )

        social_post_replies = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReplies.from_dict(
            d.pop("socialPostReplies")
        )

        social_post_quotes = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostQuotes.from_dict(
            d.pop("socialPostQuotes")
        )

        social_post_reposts = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReposts.from_dict(
            d.pop("socialPostReposts")
        )

        social_post_reactions = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostReactions.from_dict(
            d.pop("socialPostReactions")
        )

        social_user_mentions = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserMentions.from_dict(
            d.pop("socialUserMentions")
        )

        social_user_search = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialUserSearch.from_dict(
            d.pop("socialUserSearch")
        )

        social_post_search = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0SocialPostSearch.from_dict(
            d.pop("socialPostSearch")
        )

        webpage_screenshot = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScreenshot.from_dict(
            d.pop("webpageScreenshot")
        )

        webpage_scrape = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0WebpageScrape.from_dict(
            d.pop("webpageScrape")
        )

        generate_depth_chart = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GenerateDepthChart.from_dict(
            d.pop("generateDepthChart")
        )

        real_estate_search = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0RealEstateSearch.from_dict(
            d.pop("realEstateSearch")
        )

        flight_search = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightSearch.from_dict(
            d.pop("flightSearch")
        )

        mosaic_row = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0MosaicRow.from_dict(d.pop("mosaicRow"))

        get_entity_from_db = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetEntityFromDb.from_dict(
            d.pop("getEntityFromDb")
        )

        track_entity = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntity.from_dict(
            d.pop("trackEntity")
        )

        track_entity_silver = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntitySilver.from_dict(
            d.pop("trackEntitySilver")
        )

        track_entity_gold = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityGold.from_dict(
            d.pop("trackEntityGold")
        )

        track_entity_platinum = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0TrackEntityPlatinum.from_dict(
            d.pop("trackEntityPlatinum")
        )

        blue_collar_job_search = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0BlueCollarJobSearch.from_dict(
                d.pop("blueCollarJobSearch")
            )
        )

        get_company_layoffs = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetCompanyLayoffs.from_dict(
            d.pop("getCompanyLayoffs")
        )

        reverse_phone_lookup = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0ReversePhoneLookup.from_dict(
            d.pop("reversePhoneLookup")
        )

        find_company_lookalikes = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindCompanyLookalikes.from_dict(
                d.pop("findCompanyLookalikes")
            )
        )

        find_person_lookalikes = (
            GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FindPersonLookalikes.from_dict(
                d.pop("findPersonLookalikes")
            )
        )

        hotel_search = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelSearch.from_dict(
            d.pop("hotelSearch")
        )

        hotel_property_lookup = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0HotelPropertyLookup.from_dict(
            d.pop("hotelPropertyLookup")
        )

        get_department_size = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0GetDepartmentSize.from_dict(
            d.pop("getDepartmentSize")
        )

        flight_booking_page = GetOrgCreditsResponse200OutputItemCreditsPerOperationType0FlightBookingPage.from_dict(
            d.pop("flightBookingPage")
        )

        get_org_credits_response_200_output_item_credits_per_operation_type_0 = cls(
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
            text_to_search_params=text_to_search_params,
            live_enrich_company=live_enrich_company,
            live_enrich_person=live_enrich_person,
            live_enrich_person_for_contact_reveal=live_enrich_person_for_contact_reveal,
            standardize_company_slug=standardize_company_slug,
            standardize_person_slug=standardize_person_slug,
            work_email_reveal=work_email_reveal,
            personal_email_reveal=personal_email_reveal,
            lite_email_reveal=lite_email_reveal,
            lite_phone_reveal=lite_phone_reveal,
            lite_reverse_email_lookup=lite_reverse_email_lookup,
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
            sales_nav_person_scrape_without_live_fetch=sales_nav_person_scrape_without_live_fetch,
            google_maps_scrape=google_maps_scrape,
            geolocation=geolocation,
            job_title_rewrite=job_title_rewrite,
            combined_enrichment=combined_enrichment,
            domain_lookup_agent=domain_lookup_agent,
            local_business_research_agent=local_business_research_agent,
            github_lookup_agent=github_lookup_agent,
            get_li_profile_from_github_username=get_li_profile_from_github_username,
            get_email_from_github_username=get_email_from_github_username,
            social_media_finder_agent=social_media_finder_agent,
            bulk_company_logo_lookup=bulk_company_logo_lookup,
            bulk_profile_pic_lookup=bulk_profile_pic_lookup,
            get_li_profile_posts=get_li_profile_posts,
            get_li_company_posts=get_li_company_posts,
            get_li_post_comments=get_li_post_comments,
            get_li_post_reactions=get_li_post_reactions,
            get_li_profile_comments=get_li_profile_comments,
            get_li_profile_reactions=get_li_profile_reactions,
            get_li_profile_latest_activities=get_li_profile_latest_activities,
            get_li_profile_last_active_date=get_li_profile_last_active_date,
            get_profile_latest_li_post=get_profile_latest_li_post,
            get_company_latest_li_post=get_company_latest_li_post,
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
            get_company_revenue=get_company_revenue,
            multi_source_company_search=multi_source_company_search,
            multi_source_person_search=multi_source_person_search,
            scouting_report_company=scouting_report_company,
            scouting_report_person=scouting_report_person,
            track_persons_job_changes=track_persons_job_changes,
            youtube_video_transcript=youtube_video_transcript,
            youtube_video_details=youtube_video_details,
            youtube_video_comments=youtube_video_comments,
            youtube_search=youtube_search,
            youtube_channel_details=youtube_channel_details,
            social_user_details=social_user_details,
            social_user_posts=social_user_posts,
            social_user_followers=social_user_followers,
            social_user_following=social_user_following,
            social_post_details=social_post_details,
            social_post_replies=social_post_replies,
            social_post_quotes=social_post_quotes,
            social_post_reposts=social_post_reposts,
            social_post_reactions=social_post_reactions,
            social_user_mentions=social_user_mentions,
            social_user_search=social_user_search,
            social_post_search=social_post_search,
            webpage_screenshot=webpage_screenshot,
            webpage_scrape=webpage_scrape,
            generate_depth_chart=generate_depth_chart,
            real_estate_search=real_estate_search,
            flight_search=flight_search,
            mosaic_row=mosaic_row,
            get_entity_from_db=get_entity_from_db,
            track_entity=track_entity,
            track_entity_silver=track_entity_silver,
            track_entity_gold=track_entity_gold,
            track_entity_platinum=track_entity_platinum,
            blue_collar_job_search=blue_collar_job_search,
            get_company_layoffs=get_company_layoffs,
            reverse_phone_lookup=reverse_phone_lookup,
            find_company_lookalikes=find_company_lookalikes,
            find_person_lookalikes=find_person_lookalikes,
            hotel_search=hotel_search,
            hotel_property_lookup=hotel_property_lookup,
            get_department_size=get_department_size,
            flight_booking_page=flight_booking_page,
        )

        get_org_credits_response_200_output_item_credits_per_operation_type_0.additional_properties = d
        return get_org_credits_response_200_output_item_credits_per_operation_type_0

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
