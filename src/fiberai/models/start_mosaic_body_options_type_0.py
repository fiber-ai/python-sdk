from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_mosaic_body_options_type_0_contact_info_type_0 import (
        StartMosaicBodyOptionsType0ContactInfoType0,
    )


T = TypeVar("T", bound="StartMosaicBodyOptionsType0")


@_attrs_define
class StartMosaicBodyOptionsType0:
    """Feature toggles that control billing and enrichment (contact info, company details, live fetch, redline, max rows).

    Attributes:
        contact_info (None | StartMosaicBodyOptionsType0ContactInfoType0 | Unset): Which kinds of contact info to reveal
            per row — work email, personal email, and/or phone — independently selectable. Omit to skip contact reveal
            entirely. When enabled, adds the matching contact-reveal operation(s) per billable row.
        include_company_details (bool | Unset): When true, enriches each person's current employer with funding,
            offices, headcount, and related company fields. Adds the company lookup operation per billable row. Default:
            False.
        live_fetch (bool | Unset): When true, runs live profile fetch and web-search slug recovery when the enrichment
            plan calls for it. Bundled into the base Mosaic row charge — no separate operation. When false, the engine skips
            gated live-fetch steps only. Default: True.
        run_redline (bool | Unset): When true, compares enriched output against your input columns to flag staleness or
            mismatches. No separate billing operation. Default: False.
        max_rows (int | None | Unset): Cap how many input rows are processed and billed for this run (maximum 20,000).
            Useful for trial runs or cost control.
    """

    contact_info: None | StartMosaicBodyOptionsType0ContactInfoType0 | Unset = UNSET
    include_company_details: bool | Unset = False
    live_fetch: bool | Unset = True
    run_redline: bool | Unset = False
    max_rows: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.start_mosaic_body_options_type_0_contact_info_type_0 import (
            StartMosaicBodyOptionsType0ContactInfoType0,  # noqa: PLC0415
        )

        contact_info: dict[str, Any] | None | Unset
        if isinstance(self.contact_info, Unset):
            contact_info = UNSET
        elif isinstance(self.contact_info, StartMosaicBodyOptionsType0ContactInfoType0):
            contact_info = self.contact_info.to_dict()
        else:
            contact_info = self.contact_info

        include_company_details = self.include_company_details

        live_fetch = self.live_fetch

        run_redline = self.run_redline

        max_rows: int | None | Unset
        if isinstance(self.max_rows, Unset):
            max_rows = UNSET
        else:
            max_rows = self.max_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_info is not UNSET:
            field_dict["contactInfo"] = contact_info
        if include_company_details is not UNSET:
            field_dict["includeCompanyDetails"] = include_company_details
        if live_fetch is not UNSET:
            field_dict["liveFetch"] = live_fetch
        if run_redline is not UNSET:
            field_dict["runRedline"] = run_redline
        if max_rows is not UNSET:
            field_dict["maxRows"] = max_rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_mosaic_body_options_type_0_contact_info_type_0 import (
            StartMosaicBodyOptionsType0ContactInfoType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_contact_info(data: object) -> None | StartMosaicBodyOptionsType0ContactInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contact_info_type_0 = StartMosaicBodyOptionsType0ContactInfoType0.from_dict(data)

                return contact_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StartMosaicBodyOptionsType0ContactInfoType0 | Unset, data)

        contact_info = _parse_contact_info(d.pop("contactInfo", UNSET))

        include_company_details = d.pop("includeCompanyDetails", UNSET)

        live_fetch = d.pop("liveFetch", UNSET)

        run_redline = d.pop("runRedline", UNSET)

        def _parse_max_rows(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_rows = _parse_max_rows(d.pop("maxRows", UNSET))

        start_mosaic_body_options_type_0 = cls(
            contact_info=contact_info,
            include_company_details=include_company_details,
            live_fetch=live_fetch,
            run_redline=run_redline,
            max_rows=max_rows,
        )

        start_mosaic_body_options_type_0.additional_properties = d
        return start_mosaic_body_options_type_0

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
