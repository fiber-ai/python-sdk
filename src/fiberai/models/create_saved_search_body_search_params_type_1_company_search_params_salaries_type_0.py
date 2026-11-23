from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_max_level_total_compensation_usd_type_0 import (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0,
    )
    from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_median_total_compensation_usd_type_0 import (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0,
    )
    from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_min_level_total_compensation_usd_type_0 import (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0,
    )


T = TypeVar("T", bound="CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0")


@_attrs_define
class CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0:
    """
    Attributes:
        job_family_slugs (list[str] | None | Unset):
        median_total_compensation_usd
            (CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0 | None |
            Unset):
        max_level_total_compensation_usd
            (CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0 | None
            | Unset):
        min_level_total_compensation_usd
            (CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0 | None
            | Unset):
    """

    job_family_slugs: list[str] | None | Unset = UNSET
    median_total_compensation_usd: (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0
        | None
        | Unset
    ) = UNSET
    max_level_total_compensation_usd: (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0
        | None
        | Unset
    ) = UNSET
    min_level_total_compensation_usd: (
        CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_max_level_total_compensation_usd_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_median_total_compensation_usd_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_min_level_total_compensation_usd_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0,  # noqa: PLC0415
        )

        job_family_slugs: list[str] | None | Unset
        if isinstance(self.job_family_slugs, Unset):
            job_family_slugs = UNSET
        elif isinstance(self.job_family_slugs, list):
            job_family_slugs = self.job_family_slugs

        else:
            job_family_slugs = self.job_family_slugs

        median_total_compensation_usd: dict[str, Any] | None | Unset
        if isinstance(self.median_total_compensation_usd, Unset):
            median_total_compensation_usd = UNSET
        elif isinstance(
            self.median_total_compensation_usd,
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0,
        ):
            median_total_compensation_usd = self.median_total_compensation_usd.to_dict()
        else:
            median_total_compensation_usd = self.median_total_compensation_usd

        max_level_total_compensation_usd: dict[str, Any] | None | Unset
        if isinstance(self.max_level_total_compensation_usd, Unset):
            max_level_total_compensation_usd = UNSET
        elif isinstance(
            self.max_level_total_compensation_usd,
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0,
        ):
            max_level_total_compensation_usd = self.max_level_total_compensation_usd.to_dict()
        else:
            max_level_total_compensation_usd = self.max_level_total_compensation_usd

        min_level_total_compensation_usd: dict[str, Any] | None | Unset
        if isinstance(self.min_level_total_compensation_usd, Unset):
            min_level_total_compensation_usd = UNSET
        elif isinstance(
            self.min_level_total_compensation_usd,
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0,
        ):
            min_level_total_compensation_usd = self.min_level_total_compensation_usd.to_dict()
        else:
            min_level_total_compensation_usd = self.min_level_total_compensation_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_family_slugs is not UNSET:
            field_dict["jobFamilySlugs"] = job_family_slugs
        if median_total_compensation_usd is not UNSET:
            field_dict["medianTotalCompensationUsd"] = median_total_compensation_usd
        if max_level_total_compensation_usd is not UNSET:
            field_dict["maxLevelTotalCompensationUsd"] = max_level_total_compensation_usd
        if min_level_total_compensation_usd is not UNSET:
            field_dict["minLevelTotalCompensationUsd"] = min_level_total_compensation_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_max_level_total_compensation_usd_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_median_total_compensation_usd_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0,  # noqa: PLC0415
        )
        from ..models.create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0_min_level_total_compensation_usd_type_0 import (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_job_family_slugs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                job_family_slugs_type_0 = cast(list[str], data)

                return job_family_slugs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        job_family_slugs = _parse_job_family_slugs(d.pop("jobFamilySlugs", UNSET))

        def _parse_median_total_compensation_usd(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                median_total_compensation_usd_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0.from_dict(
                    data
                )

                return median_total_compensation_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MedianTotalCompensationUsdType0
                | None
                | Unset,
                data,
            )

        median_total_compensation_usd = _parse_median_total_compensation_usd(d.pop("medianTotalCompensationUsd", UNSET))

        def _parse_max_level_total_compensation_usd(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                max_level_total_compensation_usd_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0.from_dict(
                    data
                )

                return max_level_total_compensation_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MaxLevelTotalCompensationUsdType0
                | None
                | Unset,
                data,
            )

        max_level_total_compensation_usd = _parse_max_level_total_compensation_usd(
            d.pop("maxLevelTotalCompensationUsd", UNSET)
        )

        def _parse_min_level_total_compensation_usd(
            data: object,
        ) -> (
            CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                min_level_total_compensation_usd_type_0 = CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0.from_dict(
                    data
                )

                return min_level_total_compensation_usd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateSavedSearchBodySearchParamsType1CompanySearchParamsSalariesType0MinLevelTotalCompensationUsdType0
                | None
                | Unset,
                data,
            )

        min_level_total_compensation_usd = _parse_min_level_total_compensation_usd(
            d.pop("minLevelTotalCompensationUsd", UNSET)
        )

        create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0 = cls(
            job_family_slugs=job_family_slugs,
            median_total_compensation_usd=median_total_compensation_usd,
            max_level_total_compensation_usd=max_level_total_compensation_usd,
            min_level_total_compensation_usd=min_level_total_compensation_usd,
        )

        create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0.additional_properties = d
        return create_saved_search_body_search_params_type_1_company_search_params_salaries_type_0

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
