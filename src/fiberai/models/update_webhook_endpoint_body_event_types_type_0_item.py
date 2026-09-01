from enum import StrEnum


class UpdateWebhookEndpointBodyEventTypesType0Item(StrEnum):
    AUDIENCE_BUILD_COMPLETED = "audience.build_completed"
    AUDIENCE_COMPANY_EXPORT_COMPLETED = "audience.company_export_completed"
    AUDIENCE_ENRICHMENT_COMPLETED = "audience.enrichment_completed"
    AUDIENCE_PROSPECT_EXPORT_COMPLETED = "audience.prospect_export_completed"
    BATCH_CONTACT_ENRICH_COMPLETED = "batch_contact_enrich.completed"
    BATCH_CONTACT_ENRICH_V1_COMPLETED = "batch_contact_enrich_v1.completed"
    BATCH_LIVE_ENRICH_COMPLETED = "batch_live_enrich.completed"
    COMBINED_SEARCH_COMPLETED = "combined_search.completed"
    DEPTH_CHART_COMPLETED = "depth_chart.completed"
    DOMAIN_LOOKUP_COMPLETED = "domain_lookup.completed"
    GITHUB_LOOKUP_COMPLETED = "github_lookup.completed"
    GITHUB_TO_LINKEDIN_COMPLETED = "github_to_linkedin.completed"
    GOOGLE_MAPS_SEARCH_COMPLETED = "google_maps_search.completed"
    JOB_CHANGED = "job.changed"
    JOB_CHANGES_PROFILES_ADDED = "job_changes.profiles_added"
    LOCAL_BUSINESS_SEARCH_COMPLETED = "local_business_search.completed"
    MOSAIC_COMPLETED = "mosaic.completed"
    REVEAL_COMPLETED = "reveal.completed"
    SALES_NAV_LITE_SCRAPE_COMPLETED = "sales_nav_lite_scrape.completed"
    SALES_NAV_SCRAPE_COMPLETED = "sales_nav_scrape.completed"
    SAVED_SEARCH_RUN_COMPLETED = "saved_search.run_completed"
    SAVED_SEARCH_RUN_UPCOMING = "saved_search.run_upcoming"
    SOCIAL_MEDIA_LOOKUP_COMPLETED = "social_media_lookup.completed"
    TRACKER_LIST_RUN_COMPLETED = "tracker.list_run_completed"
    TRACKER_LIST_RUN_UPCOMING = "tracker.list_run_upcoming"
    TRACKER_SIGNAL_DETECTED = "tracker.signal_detected"

    def __str__(self) -> str:
        return str(self.value)
