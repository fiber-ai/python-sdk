from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.basic_work_email_reveal_body_company_type_1_mode import BasicWorkEmailRevealBodyCompanyType1Mode

if TYPE_CHECKING:
    from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_0 import (
        BasicWorkEmailRevealBodyCompanyType1IdentifierType0,
    )
    from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_1 import (
        BasicWorkEmailRevealBodyCompanyType1IdentifierType1,
    )
    from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_2 import (
        BasicWorkEmailRevealBodyCompanyType1IdentifierType2,
    )
    from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_3 import (
        BasicWorkEmailRevealBodyCompanyType1IdentifierType3,
    )


T = TypeVar("T", bound="BasicWorkEmailRevealBodyCompanyType1")


@_attrs_define
class BasicWorkEmailRevealBodyCompanyType1:
    """
    Attributes:
        mode (BasicWorkEmailRevealBodyCompanyType1Mode):
        identifier (BasicWorkEmailRevealBodyCompanyType1IdentifierType0 |
            BasicWorkEmailRevealBodyCompanyType1IdentifierType1 | BasicWorkEmailRevealBodyCompanyType1IdentifierType2 |
            BasicWorkEmailRevealBodyCompanyType1IdentifierType3): Company identifier. Resolved to a website domain before
            lookup.
    """

    mode: BasicWorkEmailRevealBodyCompanyType1Mode
    identifier: (
        BasicWorkEmailRevealBodyCompanyType1IdentifierType0
        | BasicWorkEmailRevealBodyCompanyType1IdentifierType1
        | BasicWorkEmailRevealBodyCompanyType1IdentifierType2
        | BasicWorkEmailRevealBodyCompanyType1IdentifierType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_0 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType0,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_1 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType1,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_2 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType2,  # noqa: PLC0415
        )

        mode = self.mode.value

        identifier: dict[str, Any]
        if isinstance(self.identifier, BasicWorkEmailRevealBodyCompanyType1IdentifierType0):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, BasicWorkEmailRevealBodyCompanyType1IdentifierType1):
            identifier = self.identifier.to_dict()
        elif isinstance(self.identifier, BasicWorkEmailRevealBodyCompanyType1IdentifierType2):
            identifier = self.identifier.to_dict()
        else:
            identifier = self.identifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "identifier": identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_0 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType0,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_1 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType1,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_2 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType2,  # noqa: PLC0415
        )
        from ..models.basic_work_email_reveal_body_company_type_1_identifier_type_3 import (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType3,  # noqa: PLC0415
        )

        d = dict(src_dict)
        mode = BasicWorkEmailRevealBodyCompanyType1Mode(d.pop("mode"))

        def _parse_identifier(
            data: object,
        ) -> (
            BasicWorkEmailRevealBodyCompanyType1IdentifierType0
            | BasicWorkEmailRevealBodyCompanyType1IdentifierType1
            | BasicWorkEmailRevealBodyCompanyType1IdentifierType2
            | BasicWorkEmailRevealBodyCompanyType1IdentifierType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_0 = BasicWorkEmailRevealBodyCompanyType1IdentifierType0.from_dict(data)

                return identifier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_1 = BasicWorkEmailRevealBodyCompanyType1IdentifierType1.from_dict(data)

                return identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                identifier_type_2 = BasicWorkEmailRevealBodyCompanyType1IdentifierType2.from_dict(data)

                return identifier_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            identifier_type_3 = BasicWorkEmailRevealBodyCompanyType1IdentifierType3.from_dict(data)

            return identifier_type_3

        identifier = _parse_identifier(d.pop("identifier"))

        basic_work_email_reveal_body_company_type_1 = cls(
            mode=mode,
            identifier=identifier,
        )

        basic_work_email_reveal_body_company_type_1.additional_properties = d
        return basic_work_email_reveal_body_company_type_1

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
