from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_accelerator_name import (
    CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemAcceleratorName,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_0 import (
        CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0,
    )
    from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1 import (
        CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1,
    )
    from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_years_type_0 import (
        CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0,
    )


T = TypeVar("T", bound="CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0Item")


@_attrs_define
class CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0Item:
    """
    Attributes:
        accelerator_name (CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemAcceleratorName):
        batch_selection (CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0 |
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1 | None | Unset):
        years (CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0 | None | Unset):
    """

    accelerator_name: CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemAcceleratorName
    batch_selection: (
        CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0
        | CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1
        | None
        | Unset
    ) = UNSET
    years: CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_0 import (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0,
        )
        from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1 import (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1,
        )
        from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_years_type_0 import (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0,
        )

        accelerator_name = self.accelerator_name.value

        batch_selection: dict[str, Any] | None | Unset
        if isinstance(self.batch_selection, Unset):
            batch_selection = UNSET
        elif isinstance(
            self.batch_selection, CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0
        ):
            batch_selection = self.batch_selection.to_dict()
        elif isinstance(
            self.batch_selection, CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1
        ):
            batch_selection = self.batch_selection.to_dict()
        else:
            batch_selection = self.batch_selection

        years: dict[str, Any] | None | Unset
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(self.years, CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0):
            years = self.years.to_dict()
        else:
            years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acceleratorName": accelerator_name,
            }
        )
        if batch_selection is not UNSET:
            field_dict["batchSelection"] = batch_selection
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_0 import (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0,
        )
        from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_batch_selection_type_1 import (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1,
        )
        from ..models.company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item_years_type_0 import (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0,
        )

        d = dict(src_dict)
        accelerator_name = CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemAcceleratorName(
            d.pop("acceleratorName")
        )

        def _parse_batch_selection(
            data: object,
        ) -> (
            CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0
            | CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1
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
                batch_selection_type_0 = (
                    CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0.from_dict(data)
                )

                return batch_selection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                batch_selection_type_1 = (
                    CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1.from_dict(data)
                )

                return batch_selection_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType0
                | CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemBatchSelectionType1
                | None
                | Unset,
                data,
            )

        batch_selection = _parse_batch_selection(d.pop("batchSelection", UNSET))

        def _parse_years(
            data: object,
        ) -> CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                years_type_0 = CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0.from_dict(data)

                return years_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyCountBodySearchParamsAcceleratorsV2Type0NoneOfType0ItemYearsType0 | None | Unset, data)

        years = _parse_years(d.pop("years", UNSET))

        company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item = cls(
            accelerator_name=accelerator_name,
            batch_selection=batch_selection,
            years=years,
        )

        company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item.additional_properties = d
        return company_count_body_search_params_accelerators_v2_type_0_none_of_type_0_item

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
