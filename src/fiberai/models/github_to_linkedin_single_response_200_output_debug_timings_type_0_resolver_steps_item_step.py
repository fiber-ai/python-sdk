from enum import Enum


class GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemStep(str, Enum):
    AGENT = "agent"
    CACHE_BOOTSTRAP = "cache_bootstrap"
    EMAIL_WATERFALL = "email_waterfall"
    GITHUB_FETCH = "github_fetch"
    KITCHEN_SINK = "kitchen_sink"
    TAVILY_WEB_SEARCH = "tavily_web_search"
    ZEN_CACHE_HIT = "zen_cache_hit"

    def __str__(self) -> str:
        return str(self.value)
