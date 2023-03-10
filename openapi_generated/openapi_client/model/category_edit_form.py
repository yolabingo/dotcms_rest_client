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


class CategoryEditForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            filter = schemas.StrSchema
            page = schemas.Int32Schema
            perPage = schemas.Int32Schema
            direction = schemas.StrSchema
            orderBy = schemas.StrSchema
            siteId = schemas.StrSchema
            parentInode = schemas.StrSchema
            
            
            class categoryData(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.Int32Schema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, decimal.Decimal, int, ],
                ) -> 'categoryData':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "filter": filter,
                "page": page,
                "perPage": perPage,
                "direction": direction,
                "orderBy": orderBy,
                "siteId": siteId,
                "parentInode": parentInode,
                "categoryData": categoryData,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["perPage"]) -> MetaOapg.properties.perPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderBy"]) -> MetaOapg.properties.orderBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siteId"]) -> MetaOapg.properties.siteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentInode"]) -> MetaOapg.properties.parentInode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categoryData"]) -> MetaOapg.properties.categoryData: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["filter", "page", "perPage", "direction", "orderBy", "siteId", "parentInode", "categoryData", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["perPage"]) -> typing.Union[MetaOapg.properties.perPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderBy"]) -> typing.Union[MetaOapg.properties.orderBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siteId"]) -> typing.Union[MetaOapg.properties.siteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentInode"]) -> typing.Union[MetaOapg.properties.parentInode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categoryData"]) -> typing.Union[MetaOapg.properties.categoryData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["filter", "page", "perPage", "direction", "orderBy", "siteId", "parentInode", "categoryData", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        filter: typing.Union[MetaOapg.properties.filter, str, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        perPage: typing.Union[MetaOapg.properties.perPage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        direction: typing.Union[MetaOapg.properties.direction, str, schemas.Unset] = schemas.unset,
        orderBy: typing.Union[MetaOapg.properties.orderBy, str, schemas.Unset] = schemas.unset,
        siteId: typing.Union[MetaOapg.properties.siteId, str, schemas.Unset] = schemas.unset,
        parentInode: typing.Union[MetaOapg.properties.parentInode, str, schemas.Unset] = schemas.unset,
        categoryData: typing.Union[MetaOapg.properties.categoryData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CategoryEditForm':
        return super().__new__(
            cls,
            *_args,
            filter=filter,
            page=page,
            perPage=perPage,
            direction=direction,
            orderBy=orderBy,
            siteId=siteId,
            parentInode=parentInode,
            categoryData=categoryData,
            _configuration=_configuration,
            **kwargs,
        )
