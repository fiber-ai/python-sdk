from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.start_local_business_search_body_data_item_type_0 import StartLocalBusinessSearchBodyDataItemType0
    from ..models.start_local_business_search_body_data_item_type_1 import StartLocalBusinessSearchBodyDataItemType1


T = TypeVar("T", bound="StartLocalBusinessSearchBody")


@_attrs_define
class StartLocalBusinessSearchBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        data (list[StartLocalBusinessSearchBodyDataItemType0 | StartLocalBusinessSearchBodyDataItemType1]): Array of
            businesses to search for
    """

    api_key: str
    data: list[StartLocalBusinessSearchBodyDataItemType0 | StartLocalBusinessSearchBodyDataItemType1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.start_local_business_search_body_data_item_type_0 import StartLocalBusinessSearchBodyDataItemType0

        api_key = self.api_key

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, StartLocalBusinessSearchBodyDataItemType0):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.start_local_business_search_body_data_item_type_0 import StartLocalBusinessSearchBodyDataItemType0
        from ..models.start_local_business_search_body_data_item_type_1 import StartLocalBusinessSearchBodyDataItemType1

        d = dict(src_dict)
        api_key = d.pop("apiKey")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(
                data: object,
            ) -> StartLocalBusinessSearchBodyDataItemType0 | StartLocalBusinessSearchBodyDataItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = StartLocalBusinessSearchBodyDataItemType0.from_dict(data)

                    return data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_1 = StartLocalBusinessSearchBodyDataItemType1.from_dict(data)

                return data_item_type_1

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        start_local_business_search_body = cls(
            api_key=api_key,
            data=data,
        )

        start_local_business_search_body.additional_properties = d
        return start_local_business_search_body

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
