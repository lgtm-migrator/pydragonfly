import json
import dataclasses
from typing import Optional, List
from typing_extensions import Literal

from drf_client import (
    APIResponse,
    APIResource,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
    PaginationAPIResourceMixin,
)
from drf_client.types import Toid, TParams


@dataclasses.dataclass
class CreateAnalysisRequestBody:
    profiles: List[int]
    private: Optional[bool] = False
    allow_actions: Optional[bool] = False
    root: Optional[bool] = False
    os: Optional[Literal["WINDOWS", "LINUX"]] = None
    arguments: List[str] = dataclasses.field(default_factory=list)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


class Analysis(
    APIResource,
    RetrievableAPIResourceMixin,
    ListableAPIResourceMixin,
    PaginationAPIResourceMixin,
):
    OBJECT_NAME = "api.analysis"
    EXPANDABLE_FIELDS = {
        "retrieve": ["sample", "reports"],
        "list": [],
    }
    ORDERING_FIELDS = [
        "created_at",
        "sample__filename",
        "weight",
    ]
    CreateRequestBody = CreateAnalysisRequestBody

    @classmethod
    def create(
        cls,
        data: CreateAnalysisRequestBody,
        sample_name: str,
        sample: bytes,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = "api/create_analysis"
        post_data = {"data": json.dumps(data.to_dict())}
        post_files = {"sample": (sample_name, sample)}
        response = cls._request(
            "POST",
            url=url,
            data=post_data,
            files=post_files,
            params=params,
        )
        return response

    @classmethod
    def aggregate_evaluations(
        cls,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.class_url() + "/aggregate/evaluations"
        response = cls._request("GET", url=url, params=params)
        return response

    @classmethod
    def aggregate_status(
        cls,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.class_url() + "/aggregate/status"
        response = cls._request("GET", url=url, params=params)
        return response

    @classmethod
    def aggregate_malware_families(
        cls,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.class_url() + "/aggregate/malware_families"
        response = cls._request("GET", url=url, params=params)
        return response

    @classmethod
    def aggregate_malware_type(
        cls,
        **params: Optional[TParams],
    ) -> APIResponse:
        url = cls.class_url() + "/aggregate/malware_type"
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
