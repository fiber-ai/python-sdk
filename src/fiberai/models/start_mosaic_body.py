from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.start_mosaic_body_options_type_0 import StartMosaicBodyOptionsType0


T = TypeVar("T", bound="StartMosaicBody")


@_attrs_define
class StartMosaicBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        source_url (str): HTTPS URL of the input file. Supported formats: CSV, TXT (one LinkedIn profile URL per line),
            XLSX, or a public Google Sheet. You may also pass a public Google Drive file link, Dropbox share link, or
            OneDrive / SharePoint share link. The link must be publicly accessible (e.g. Google Sheets / Drive: "Anyone with
            the link can view"; Dropbox / OneDrive: link allows direct download) or the fetch will fail. Google Sheets
            export the first tab only. For XLSX workbooks we auto-detect the most likely worksheet and header row; if
            detection is unavailable we use the sheet with the most rows and treat row 1 as the header. Maximum file size is
            50 MiB. The file is securely fetched and stored before processing.
        custom_instructions (None | str | Unset): Optional additional instructions for the AI on top of our system
            prompt — not a replacement for it. Use this to steer enrichment when your file needs extra context. Examples: "I
            really want personal emails but I don't care about phones"; "These are all doctors — make sure you get office
            phones, not home phones".
        options (None | StartMosaicBodyOptionsType0 | Unset): Feature toggles that control billing and enrichment
            (contact info, company details, live fetch, redline, max rows).
    """

    api_key: str
    source_url: str
    custom_instructions: None | str | Unset = UNSET
    options: None | StartMosaicBodyOptionsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.start_mosaic_body_options_type_0 import StartMosaicBodyOptionsType0

        api_key = self.api_key

        source_url = self.source_url

        custom_instructions: None | str | Unset
        if isinstance(self.custom_instructions, Unset):
            custom_instructions = UNSET
        else:
            custom_instructions = self.custom_instructions

        options: dict[str, Any] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, StartMosaicBodyOptionsType0):
            options = self.options.to_dict()
        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "sourceUrl": source_url,
            }
        )
        if custom_instructions is not UNSET:
            field_dict["customInstructions"] = custom_instructions
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_mosaic_body_options_type_0 import StartMosaicBodyOptionsType0

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        source_url = d.pop("sourceUrl")

        def _parse_custom_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_instructions = _parse_custom_instructions(d.pop("customInstructions", UNSET))

        def _parse_options(data: object) -> None | StartMosaicBodyOptionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = StartMosaicBodyOptionsType0.from_dict(data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StartMosaicBodyOptionsType0 | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        start_mosaic_body = cls(
            api_key=api_key,
            source_url=source_url,
            custom_instructions=custom_instructions,
            options=options,
        )

        start_mosaic_body.additional_properties = d
        return start_mosaic_body

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
