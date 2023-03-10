# coding: utf-8

"""
    dotCMS REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class WorkflowSchemeForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "schemeName",
        }
        
        class properties:
            schemeName = schemas.StrSchema
            schemeDescription = schemas.StrSchema
            schemeArchived = schemas.BoolSchema
            __annotations__ = {
                "schemeName": schemeName,
                "schemeDescription": schemeDescription,
                "schemeArchived": schemeArchived,
            }
    
    schemeName: MetaOapg.properties.schemeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemeName"]) -> MetaOapg.properties.schemeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemeDescription"]) -> MetaOapg.properties.schemeDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemeArchived"]) -> MetaOapg.properties.schemeArchived: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schemeName", "schemeDescription", "schemeArchived", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemeName"]) -> MetaOapg.properties.schemeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemeDescription"]) -> typing.Union[MetaOapg.properties.schemeDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemeArchived"]) -> typing.Union[MetaOapg.properties.schemeArchived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schemeName", "schemeDescription", "schemeArchived", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        schemeName: typing.Union[MetaOapg.properties.schemeName, str, ],
        schemeDescription: typing.Union[MetaOapg.properties.schemeDescription, str, schemas.Unset] = schemas.unset,
        schemeArchived: typing.Union[MetaOapg.properties.schemeArchived, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowSchemeForm':
        return super().__new__(
            cls,
            *_args,
            schemeName=schemeName,
            schemeDescription=schemeDescription,
            schemeArchived=schemeArchived,
            _configuration=_configuration,
            **kwargs,
        )
