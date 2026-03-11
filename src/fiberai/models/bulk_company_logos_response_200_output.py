from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_company_logos_response_200_output_data_type_0 import BulkCompanyLogosResponse200OutputDataType0
    from ..models.bulk_company_logos_response_200_output_data_type_1 import BulkCompanyLogosResponse200OutputDataType1
    from ..models.bulk_company_logos_response_200_output_data_type_2 import BulkCompanyLogosResponse200OutputDataType2


T = TypeVar("T", bound="BulkCompanyLogosResponse200Output")


@_attrs_define
class BulkCompanyLogosResponse200Output:
    """
    Attributes:
        data (BulkCompanyLogosResponse200OutputDataType0 | BulkCompanyLogosResponse200OutputDataType1 |
            BulkCompanyLogosResponse200OutputDataType2): The list of logo URLs
    """

    data: (
        BulkCompanyLogosResponse200OutputDataType0
        | BulkCompanyLogosResponse200OutputDataType1
        | BulkCompanyLogosResponse200OutputDataType2
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_company_logos_response_200_output_data_type_0 import (
            BulkCompanyLogosResponse200OutputDataType0,
        )
        from ..models.bulk_company_logos_response_200_output_data_type_1 import (
            BulkCompanyLogosResponse200OutputDataType1,
        )

        data: dict[str, Any]
        if isinstance(self.data, BulkCompanyLogosResponse200OutputDataType0):
            data = self.data.to_dict()
        elif isinstance(self.data, BulkCompanyLogosResponse200OutputDataType1):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_company_logos_response_200_output_data_type_0 import (
            BulkCompanyLogosResponse200OutputDataType0,
        )
        from ..models.bulk_company_logos_response_200_output_data_type_1 import (
            BulkCompanyLogosResponse200OutputDataType1,
        )
        from ..models.bulk_company_logos_response_200_output_data_type_2 import (
            BulkCompanyLogosResponse200OutputDataType2,
        )

        d = dict(src_dict)

        def _parse_data(
            data: object,
        ) -> (
            BulkCompanyLogosResponse200OutputDataType0
            | BulkCompanyLogosResponse200OutputDataType1
            | BulkCompanyLogosResponse200OutputDataType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = BulkCompanyLogosResponse200OutputDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = BulkCompanyLogosResponse200OutputDataType1.from_dict(data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_2 = BulkCompanyLogosResponse200OutputDataType2.from_dict(data)

            return data_type_2

        data = _parse_data(d.pop("data"))

        bulk_company_logos_response_200_output = cls(
            data=data,
        )

        bulk_company_logos_response_200_output.additional_properties = d
        return bulk_company_logos_response_200_output

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
