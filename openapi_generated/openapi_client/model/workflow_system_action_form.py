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


class WorkflowSystemActionForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "actionId",
            "systemAction",
        }
        
        class properties:
            actionId = schemas.StrSchema
            
            
            class systemAction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NEW": "NEW",
                        "EDIT": "EDIT",
                        "PUBLISH": "PUBLISH",
                        "UNPUBLISH": "UNPUBLISH",
                        "ARCHIVE": "ARCHIVE",
                        "UNARCHIVE": "UNARCHIVE",
                        "DELETE": "DELETE",
                        "DESTROY": "DESTROY",
                    }
                
                @schemas.classproperty
                def NEW(cls):
                    return cls("NEW")
                
                @schemas.classproperty
                def EDIT(cls):
                    return cls("EDIT")
                
                @schemas.classproperty
                def PUBLISH(cls):
                    return cls("PUBLISH")
                
                @schemas.classproperty
                def UNPUBLISH(cls):
                    return cls("UNPUBLISH")
                
                @schemas.classproperty
                def ARCHIVE(cls):
                    return cls("ARCHIVE")
                
                @schemas.classproperty
                def UNARCHIVE(cls):
                    return cls("UNARCHIVE")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("DELETE")
                
                @schemas.classproperty
                def DESTROY(cls):
                    return cls("DESTROY")
            schemeId = schemas.StrSchema
            contentTypeVariable = schemas.StrSchema
            __annotations__ = {
                "actionId": actionId,
                "systemAction": systemAction,
                "schemeId": schemeId,
                "contentTypeVariable": contentTypeVariable,
            }
    
    actionId: MetaOapg.properties.actionId
    systemAction: MetaOapg.properties.systemAction
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actionId"]) -> MetaOapg.properties.actionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemAction"]) -> MetaOapg.properties.systemAction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemeId"]) -> MetaOapg.properties.schemeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentTypeVariable"]) -> MetaOapg.properties.contentTypeVariable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["actionId", "systemAction", "schemeId", "contentTypeVariable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actionId"]) -> MetaOapg.properties.actionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemAction"]) -> MetaOapg.properties.systemAction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemeId"]) -> typing.Union[MetaOapg.properties.schemeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentTypeVariable"]) -> typing.Union[MetaOapg.properties.contentTypeVariable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["actionId", "systemAction", "schemeId", "contentTypeVariable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        actionId: typing.Union[MetaOapg.properties.actionId, str, ],
        systemAction: typing.Union[MetaOapg.properties.systemAction, str, ],
        schemeId: typing.Union[MetaOapg.properties.schemeId, str, schemas.Unset] = schemas.unset,
        contentTypeVariable: typing.Union[MetaOapg.properties.contentTypeVariable, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowSystemActionForm':
        return super().__new__(
            cls,
            *_args,
            actionId=actionId,
            systemAction=systemAction,
            schemeId=schemeId,
            contentTypeVariable=contentTypeVariable,
            _configuration=_configuration,
            **kwargs,
        )
