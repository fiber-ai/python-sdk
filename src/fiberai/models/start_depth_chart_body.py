from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_depth_chart_body_company_type_0 import StartDepthChartBodyCompanyType0
    from ..models.start_depth_chart_body_company_type_1 import StartDepthChartBodyCompanyType1
    from ..models.start_depth_chart_body_company_type_2 import StartDepthChartBodyCompanyType2
    from ..models.start_depth_chart_body_company_type_3 import StartDepthChartBodyCompanyType3


T = TypeVar("T", bound="StartDepthChartBody")


@_attrs_define
class StartDepthChartBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        company (StartDepthChartBodyCompanyType0 | StartDepthChartBodyCompanyType1 | StartDepthChartBodyCompanyType2 |
            StartDepthChartBodyCompanyType3): Company identifier. Set identifier to 'linkedinUrl', 'linkedinSlug',
            'linkedinOrgId', or 'domain' and provide the corresponding value.
        functions (list[str] | None | Unset): Optional list of function/department labels to classify employees into
            (e.g. ['Engineering', 'Sales', 'Legal Practice']). When omitted, functions are auto-detected based on the
            company's employee titles. An 'Other' category is automatically appended if not already included, to catch
            employees that don't fit the provided labels.
    """

    api_key: str
    company: (
        StartDepthChartBodyCompanyType0
        | StartDepthChartBodyCompanyType1
        | StartDepthChartBodyCompanyType2
        | StartDepthChartBodyCompanyType3
    )
    functions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.start_depth_chart_body_company_type_0 import StartDepthChartBodyCompanyType0  # noqa: PLC0415
        from ..models.start_depth_chart_body_company_type_1 import StartDepthChartBodyCompanyType1  # noqa: PLC0415
        from ..models.start_depth_chart_body_company_type_2 import StartDepthChartBodyCompanyType2  # noqa: PLC0415

        api_key = self.api_key

        company: dict[str, Any]
        if isinstance(self.company, StartDepthChartBodyCompanyType0):
            company = self.company.to_dict()
        elif isinstance(self.company, StartDepthChartBodyCompanyType1):
            company = self.company.to_dict()
        elif isinstance(self.company, StartDepthChartBodyCompanyType2):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        functions: list[str] | None | Unset
        if isinstance(self.functions, Unset):
            functions = UNSET
        elif isinstance(self.functions, list):
            functions = self.functions

        else:
            functions = self.functions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "company": company,
            }
        )
        if functions is not UNSET:
            field_dict["functions"] = functions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_depth_chart_body_company_type_0 import StartDepthChartBodyCompanyType0  # noqa: PLC0415
        from ..models.start_depth_chart_body_company_type_1 import StartDepthChartBodyCompanyType1  # noqa: PLC0415
        from ..models.start_depth_chart_body_company_type_2 import StartDepthChartBodyCompanyType2  # noqa: PLC0415
        from ..models.start_depth_chart_body_company_type_3 import StartDepthChartBodyCompanyType3  # noqa: PLC0415

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        def _parse_company(
            data: object,
        ) -> (
            StartDepthChartBodyCompanyType0
            | StartDepthChartBodyCompanyType1
            | StartDepthChartBodyCompanyType2
            | StartDepthChartBodyCompanyType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_0 = StartDepthChartBodyCompanyType0.from_dict(data)

                return company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_1 = StartDepthChartBodyCompanyType1.from_dict(data)

                return company_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                company_type_2 = StartDepthChartBodyCompanyType2.from_dict(data)

                return company_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            company_type_3 = StartDepthChartBodyCompanyType3.from_dict(data)

            return company_type_3

        company = _parse_company(d.pop("company"))

        def _parse_functions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functions_type_0 = cast(list[str], data)

                return functions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        functions = _parse_functions(d.pop("functions", UNSET))

        start_depth_chart_body = cls(
            api_key=api_key,
            company=company,
            functions=functions,
        )

        start_depth_chart_body.additional_properties = d
        return start_depth_chart_body

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
