from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_talent_flow_rivals_response_200_output_company import GetTalentFlowRivalsResponse200OutputCompany
    from ..models.get_talent_flow_rivals_response_200_output_rivals_item import (
        GetTalentFlowRivalsResponse200OutputRivalsItem,
    )
    from ..models.get_talent_flow_rivals_response_200_output_window import GetTalentFlowRivalsResponse200OutputWindow


T = TypeVar("T", bound="GetTalentFlowRivalsResponse200Output")


@_attrs_define
class GetTalentFlowRivalsResponse200Output:
    """
    Attributes:
        company (GetTalentFlowRivalsResponse200OutputCompany): Company that was analyzed.
        window (GetTalentFlowRivalsResponse200OutputWindow): Time window for the analysis.
        num_companies_per_side (int): Requested number of donor and acceptor companies per side.
        joiners_count (int): Number of people who joined the analyzed company within the window.
        leavers_count (int): Number of people who left the analyzed company within the window.
        rivals (list[GetTalentFlowRivalsResponse200OutputRivalsItem]): Companies trading the most talent with the
            analyzed company, sorted by total two-way moves (gained plus lost) descending. Includes up to
            `numCompaniesPerSide` top donors (companies it hires from most) and up to `numCompaniesPerSide` top acceptors
            (companies its alumni join most); overlapping companies are combined into one entry.
        generated_at (str): ISO 8601 timestamp when the report was generated.
        markdown_summary (str): Human-readable markdown summary of the report, including a rival table.
    """

    company: GetTalentFlowRivalsResponse200OutputCompany
    window: GetTalentFlowRivalsResponse200OutputWindow
    num_companies_per_side: int
    joiners_count: int
    leavers_count: int
    rivals: list[GetTalentFlowRivalsResponse200OutputRivalsItem]
    generated_at: str
    markdown_summary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        window = self.window.to_dict()

        num_companies_per_side = self.num_companies_per_side

        joiners_count = self.joiners_count

        leavers_count = self.leavers_count

        rivals = []
        for rivals_item_data in self.rivals:
            rivals_item = rivals_item_data.to_dict()
            rivals.append(rivals_item)

        generated_at = self.generated_at

        markdown_summary = self.markdown_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "window": window,
                "numCompaniesPerSide": num_companies_per_side,
                "joinersCount": joiners_count,
                "leaversCount": leavers_count,
                "rivals": rivals,
                "generatedAt": generated_at,
                "markdownSummary": markdown_summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_talent_flow_rivals_response_200_output_company import (
            GetTalentFlowRivalsResponse200OutputCompany,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_response_200_output_rivals_item import (
            GetTalentFlowRivalsResponse200OutputRivalsItem,  # noqa: PLC0415
        )
        from ..models.get_talent_flow_rivals_response_200_output_window import (
            GetTalentFlowRivalsResponse200OutputWindow,  # noqa: PLC0415
        )

        d = dict(src_dict)
        company = GetTalentFlowRivalsResponse200OutputCompany.from_dict(d.pop("company"))

        window = GetTalentFlowRivalsResponse200OutputWindow.from_dict(d.pop("window"))

        num_companies_per_side = d.pop("numCompaniesPerSide")

        joiners_count = d.pop("joinersCount")

        leavers_count = d.pop("leaversCount")

        rivals = []
        _rivals = d.pop("rivals")
        for rivals_item_data in _rivals:
            rivals_item = GetTalentFlowRivalsResponse200OutputRivalsItem.from_dict(rivals_item_data)

            rivals.append(rivals_item)

        generated_at = d.pop("generatedAt")

        markdown_summary = d.pop("markdownSummary")

        get_talent_flow_rivals_response_200_output = cls(
            company=company,
            window=window,
            num_companies_per_side=num_companies_per_side,
            joiners_count=joiners_count,
            leavers_count=leavers_count,
            rivals=rivals,
            generated_at=generated_at,
            markdown_summary=markdown_summary,
        )

        get_talent_flow_rivals_response_200_output.additional_properties = d
        return get_talent_flow_rivals_response_200_output

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
