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


class FireBulkActionsForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            query = schemas.StrSchema
            
            
            class contentletIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contentletIds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            workflowActionId = schemas.StrSchema
        
            @staticmethod
            def additionalParams() -> typing.Type['AdditionalParamsBean']:
                return AdditionalParamsBean
        
            @staticmethod
            def popupParamsBean() -> typing.Type['AdditionalParamsBean']:
                return AdditionalParamsBean
            __annotations__ = {
                "query": query,
                "contentletIds": contentletIds,
                "workflowActionId": workflowActionId,
                "additionalParams": additionalParams,
                "popupParamsBean": popupParamsBean,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentletIds"]) -> MetaOapg.properties.contentletIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowActionId"]) -> MetaOapg.properties.workflowActionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalParams"]) -> 'AdditionalParamsBean': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["popupParamsBean"]) -> 'AdditionalParamsBean': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["query", "contentletIds", "workflowActionId", "additionalParams", "popupParamsBean", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentletIds"]) -> typing.Union[MetaOapg.properties.contentletIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowActionId"]) -> typing.Union[MetaOapg.properties.workflowActionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalParams"]) -> typing.Union['AdditionalParamsBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["popupParamsBean"]) -> typing.Union['AdditionalParamsBean', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["query", "contentletIds", "workflowActionId", "additionalParams", "popupParamsBean", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        contentletIds: typing.Union[MetaOapg.properties.contentletIds, list, tuple, schemas.Unset] = schemas.unset,
        workflowActionId: typing.Union[MetaOapg.properties.workflowActionId, str, schemas.Unset] = schemas.unset,
        additionalParams: typing.Union['AdditionalParamsBean', schemas.Unset] = schemas.unset,
        popupParamsBean: typing.Union['AdditionalParamsBean', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FireBulkActionsForm':
        return super().__new__(
            cls,
            *_args,
            query=query,
            contentletIds=contentletIds,
            workflowActionId=workflowActionId,
            additionalParams=additionalParams,
            popupParamsBean=popupParamsBean,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.additional_params_bean import AdditionalParamsBean
