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

from dotcms_rest_client import schemas  # noqa: F401


class MulitreeView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            pageId = schemas.StrSchema
            containerId = schemas.StrSchema
            contentId = schemas.StrSchema
            relationType = schemas.StrSchema
            treeOrder = schemas.Int32Schema
            personalization = schemas.StrSchema
            variantId = schemas.StrSchema
            __annotations__ = {
                "pageId": pageId,
                "containerId": containerId,
                "contentId": contentId,
                "relationType": relationType,
                "treeOrder": treeOrder,
                "personalization": personalization,
                "variantId": variantId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageId"]) -> MetaOapg.properties.pageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containerId"]) -> MetaOapg.properties.containerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentId"]) -> MetaOapg.properties.contentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationType"]) -> MetaOapg.properties.relationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["treeOrder"]) -> MetaOapg.properties.treeOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalization"]) -> MetaOapg.properties.personalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variantId"]) -> MetaOapg.properties.variantId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pageId", "containerId", "contentId", "relationType", "treeOrder", "personalization", "variantId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageId"]) -> typing.Union[MetaOapg.properties.pageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containerId"]) -> typing.Union[MetaOapg.properties.containerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentId"]) -> typing.Union[MetaOapg.properties.contentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationType"]) -> typing.Union[MetaOapg.properties.relationType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["treeOrder"]) -> typing.Union[MetaOapg.properties.treeOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalization"]) -> typing.Union[MetaOapg.properties.personalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variantId"]) -> typing.Union[MetaOapg.properties.variantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pageId", "containerId", "contentId", "relationType", "treeOrder", "personalization", "variantId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pageId: typing.Union[MetaOapg.properties.pageId, str, schemas.Unset] = schemas.unset,
        containerId: typing.Union[MetaOapg.properties.containerId, str, schemas.Unset] = schemas.unset,
        contentId: typing.Union[MetaOapg.properties.contentId, str, schemas.Unset] = schemas.unset,
        relationType: typing.Union[MetaOapg.properties.relationType, str, schemas.Unset] = schemas.unset,
        treeOrder: typing.Union[MetaOapg.properties.treeOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        personalization: typing.Union[MetaOapg.properties.personalization, str, schemas.Unset] = schemas.unset,
        variantId: typing.Union[MetaOapg.properties.variantId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MulitreeView':
        return super().__new__(
            cls,
            *_args,
            pageId=pageId,
            containerId=containerId,
            contentId=contentId,
            relationType=relationType,
            treeOrder=treeOrder,
            personalization=personalization,
            variantId=variantId,
            _configuration=_configuration,
            **kwargs,
        )