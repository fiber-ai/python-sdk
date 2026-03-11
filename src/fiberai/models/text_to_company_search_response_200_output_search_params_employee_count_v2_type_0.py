from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_0 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_1 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_2 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_3 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_4 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_5 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_6 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_7 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_lower_bound_exclusive_type_8 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_0 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_1 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_2 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_3 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_4 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_5 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_6 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_7 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7,
)
from ..models.text_to_company_search_response_200_output_search_params_employee_count_v2_type_0_upper_bound_inclusive_type_8 import (
    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0")


@_attrs_define
class TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0:
    """
    Attributes:
        lower_bound_exclusive (None |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8 | Unset):
        upper_bound_inclusive (None |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7 |
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8 | Unset):
    """

    lower_bound_exclusive: (
        None
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8
        | Unset
    ) = UNSET
    upper_bound_inclusive: (
        None
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7
        | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower_bound_exclusive: int | None | Unset
        if isinstance(self.lower_bound_exclusive, Unset):
            lower_bound_exclusive = UNSET
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        elif isinstance(
            self.lower_bound_exclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8,
        ):
            lower_bound_exclusive = self.lower_bound_exclusive.value
        else:
            lower_bound_exclusive = self.lower_bound_exclusive

        upper_bound_inclusive: int | None | Unset
        if isinstance(self.upper_bound_inclusive, Unset):
            upper_bound_inclusive = UNSET
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        elif isinstance(
            self.upper_bound_inclusive,
            TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8,
        ):
            upper_bound_inclusive = self.upper_bound_inclusive.value
        else:
            upper_bound_inclusive = self.upper_bound_inclusive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower_bound_exclusive is not UNSET:
            field_dict["lowerBoundExclusive"] = lower_bound_exclusive
        if upper_bound_inclusive is not UNSET:
            field_dict["upperBoundInclusive"] = upper_bound_inclusive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_lower_bound_exclusive(
            data: object,
        ) -> (
            None
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_0 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0(data)
                )

                return lower_bound_exclusive_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_1 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1(data)
                )

                return lower_bound_exclusive_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_2 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2(data)
                )

                return lower_bound_exclusive_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_3 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3(data)
                )

                return lower_bound_exclusive_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_4 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4(data)
                )

                return lower_bound_exclusive_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_5 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5(data)
                )

                return lower_bound_exclusive_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_6 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6(data)
                )

                return lower_bound_exclusive_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_7 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7(data)
                )

                return lower_bound_exclusive_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                lower_bound_exclusive_type_8 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8(data)
                )

                return lower_bound_exclusive_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType0
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType1
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType2
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType3
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType4
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType5
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType6
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType7
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0LowerBoundExclusiveType8
                | Unset,
                data,
            )

        lower_bound_exclusive = _parse_lower_bound_exclusive(d.pop("lowerBoundExclusive", UNSET))

        def _parse_upper_bound_inclusive(
            data: object,
        ) -> (
            None
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7
            | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_0 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0(data)
                )

                return upper_bound_inclusive_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_1 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1(data)
                )

                return upper_bound_inclusive_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_2 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2(data)
                )

                return upper_bound_inclusive_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_3 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3(data)
                )

                return upper_bound_inclusive_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_4 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4(data)
                )

                return upper_bound_inclusive_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_5 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5(data)
                )

                return upper_bound_inclusive_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_6 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6(data)
                )

                return upper_bound_inclusive_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_7 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7(data)
                )

                return upper_bound_inclusive_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                upper_bound_inclusive_type_8 = (
                    TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8(data)
                )

                return upper_bound_inclusive_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType0
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType1
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType2
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType3
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType4
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType5
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType6
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType7
                | TextToCompanySearchResponse200OutputSearchParamsEmployeeCountV2Type0UpperBoundInclusiveType8
                | Unset,
                data,
            )

        upper_bound_inclusive = _parse_upper_bound_inclusive(d.pop("upperBoundInclusive", UNSET))

        text_to_company_search_response_200_output_search_params_employee_count_v2_type_0 = cls(
            lower_bound_exclusive=lower_bound_exclusive,
            upper_bound_inclusive=upper_bound_inclusive,
        )

        text_to_company_search_response_200_output_search_params_employee_count_v2_type_0.additional_properties = d
        return text_to_company_search_response_200_output_search_params_employee_count_v2_type_0

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
