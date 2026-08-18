from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_api_key_limit_body_operation import UpdateApiKeyLimitBodyOperation
from ..models.update_api_key_limit_body_target import UpdateApiKeyLimitBodyTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApiKeyLimitBody")


@_attrs_define
class UpdateApiKeyLimitBody:
    """
    Attributes:
        api_key (str): Your Fiber API key
        operation (UpdateApiKeyLimitBodyOperation): set: pin an absolute credit ceiling. increase/decrease: adjust the
            current ceiling by a number of credits. multiply/divide: scale the current ceiling by a factor. remove: make the
            key unlimited. increase, decrease, multiply, and divide have no effect on an already-unlimited key; use set to
            establish a ceiling first.
        target (UpdateApiKeyLimitBodyTarget | Unset): Which key to act on. SELF acts on the key that authenticates this
            request. OTHER acts on a different key in your organization, supplied in targetApiKey. Default:
            UpdateApiKeyLimitBodyTarget.SELF.
        target_api_key (None | str | Unset): The key to act on when target is OTHER. Must belong to your organization.
            You can pass prefix, id, or the raw key. Omit when target is SELF.
        credits_ (float | None | Unset): The credit amount. Required for set (zero or greater), increase, and decrease
            (greater than zero); ignored otherwise.
        factor (float | None | Unset): The factor to scale the current ceiling by. Required for multiply and divide;
            ignored otherwise.
    """

    api_key: str
    operation: UpdateApiKeyLimitBodyOperation
    target: UpdateApiKeyLimitBodyTarget | Unset = UpdateApiKeyLimitBodyTarget.SELF
    target_api_key: None | str | Unset = UNSET
    credits_: float | None | Unset = UNSET
    factor: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        operation = self.operation.value

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        target_api_key: None | str | Unset
        if isinstance(self.target_api_key, Unset):
            target_api_key = UNSET
        else:
            target_api_key = self.target_api_key

        credits_: float | None | Unset
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = self.credits_

        factor: float | None | Unset
        if isinstance(self.factor, Unset):
            factor = UNSET
        else:
            factor = self.factor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "operation": operation,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if target_api_key is not UNSET:
            field_dict["targetApiKey"] = target_api_key
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if factor is not UNSET:
            field_dict["factor"] = factor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        operation = UpdateApiKeyLimitBodyOperation(d.pop("operation"))

        _target = d.pop("target", UNSET)
        target: UpdateApiKeyLimitBodyTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = UpdateApiKeyLimitBodyTarget(_target)

        def _parse_target_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_api_key = _parse_target_api_key(d.pop("targetApiKey", UNSET))

        def _parse_credits_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        def _parse_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        factor = _parse_factor(d.pop("factor", UNSET))

        update_api_key_limit_body = cls(
            api_key=api_key,
            operation=operation,
            target=target,
            target_api_key=target_api_key,
            credits_=credits_,
            factor=factor,
        )

        update_api_key_limit_body.additional_properties = d
        return update_api_key_limit_body

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
