from typing import Optional

from drf_client import (
    APIResponse,
    APIResource,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
    PaginationAPIResourceMixin,
)
from drf_client.types import Toid, TParams


class Report(
    APIResource,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
    PaginationAPIResourceMixin,
):
    OBJECT_NAME = "api.report"
    EXPANDABLE_FIELDS = {
        "retrieve": ["profile", "analysis"],
        "list": ["profile", "analysis"],
    }
    ORDERING_FIELDS = [
        "time__start_analysis",
        "analysis__sample__filename",
        "weight",
    ]

    @classmethod
    def timeline(
        cls,
        object_id: Toid,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.instance_url(object_id) + "/timeline"
        response = cls._request("GET", url=url, params=params)
        return response

    @classmethod
    def matched_rules(
        cls,
        object_id: Toid,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.instance_url(object_id) + "/matched_rules"
        response = cls._request("GET", url=url, params=params)
        return response

    @classmethod
    def revoke(
        cls,
        object_id: Toid,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.instance_url(object_id) + "/revoke"
        response = cls._request("POST", url=url, params=params)
        return response
