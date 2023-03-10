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


class CategoryForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "categoryName",
        }
        
        class properties:
            categoryName = schemas.StrSchema
            siteId = schemas.StrSchema
            inode = schemas.StrSchema
            parent = schemas.StrSchema
            description = schemas.StrSchema
            keywords = schemas.StrSchema
            key = schemas.StrSchema
            active = schemas.BoolSchema
            sortOrder = schemas.Int32Schema
            categoryVelocityVarName = schemas.StrSchema
            __annotations__ = {
                "categoryName": categoryName,
                "siteId": siteId,
                "inode": inode,
                "parent": parent,
                "description": description,
                "keywords": keywords,
                "key": key,
                "active": active,
                "sortOrder": sortOrder,
                "categoryVelocityVarName": categoryVelocityVarName,
            }
    
    categoryName: MetaOapg.properties.categoryName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categoryName"]) -> MetaOapg.properties.categoryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siteId"]) -> MetaOapg.properties.siteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inode"]) -> MetaOapg.properties.inode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keywords"]) -> MetaOapg.properties.keywords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sortOrder"]) -> MetaOapg.properties.sortOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categoryVelocityVarName"]) -> MetaOapg.properties.categoryVelocityVarName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["categoryName", "siteId", "inode", "parent", "description", "keywords", "key", "active", "sortOrder", "categoryVelocityVarName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categoryName"]) -> MetaOapg.properties.categoryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siteId"]) -> typing.Union[MetaOapg.properties.siteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inode"]) -> typing.Union[MetaOapg.properties.inode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union[MetaOapg.properties.parent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keywords"]) -> typing.Union[MetaOapg.properties.keywords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sortOrder"]) -> typing.Union[MetaOapg.properties.sortOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categoryVelocityVarName"]) -> typing.Union[MetaOapg.properties.categoryVelocityVarName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["categoryName", "siteId", "inode", "parent", "description", "keywords", "key", "active", "sortOrder", "categoryVelocityVarName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        categoryName: typing.Union[MetaOapg.properties.categoryName, str, ],
        siteId: typing.Union[MetaOapg.properties.siteId, str, schemas.Unset] = schemas.unset,
        inode: typing.Union[MetaOapg.properties.inode, str, schemas.Unset] = schemas.unset,
        parent: typing.Union[MetaOapg.properties.parent, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        keywords: typing.Union[MetaOapg.properties.keywords, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        sortOrder: typing.Union[MetaOapg.properties.sortOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        categoryVelocityVarName: typing.Union[MetaOapg.properties.categoryVelocityVarName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CategoryForm':
        return super().__new__(
            cls,
            *_args,
            categoryName=categoryName,
            siteId=siteId,
            inode=inode,
            parent=parent,
            description=description,
            keywords=keywords,
            key=key,
            active=active,
            sortOrder=sortOrder,
            categoryVelocityVarName=categoryVelocityVarName,
            _configuration=_configuration,
            **kwargs,
        )
