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
        source_url (str): HTTPS URL of the input CSV, TXT, XLSX, Google Sheet, Dropbox, or OneDrive share link. The file
            is securely fetched and stored before processing.
        prompt (None | str | Unset): Optional free-text instructions describing what to enrich or heal in the file.
        options (None | StartMosaicBodyOptionsType0 | Unset): Feature toggles that control billing and enrichment
            (contact info, company details, live fetch, redline, max rows).
    """

    api_key: str
    source_url: str
    prompt: None | str | Unset = UNSET
    options: None | StartMosaicBodyOptionsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.start_mosaic_body_options_type_0 import StartMosaicBodyOptionsType0

        api_key = self.api_key

        source_url = self.source_url

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

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
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_mosaic_body_options_type_0 import StartMosaicBodyOptionsType0

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        source_url = d.pop("sourceUrl")

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

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
            prompt=prompt,
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
