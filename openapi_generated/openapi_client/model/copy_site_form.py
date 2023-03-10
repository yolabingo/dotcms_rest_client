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


class CopySiteForm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            copyFromSiteId = schemas.StrSchema
            copyAll = schemas.BoolSchema
            copyTemplatesContainers = schemas.BoolSchema
            copyContentOnPages = schemas.BoolSchema
            copyFolders = schemas.BoolSchema
            copyContentOnSite = schemas.BoolSchema
            copyLinks = schemas.BoolSchema
            copySiteVariables = schemas.BoolSchema
        
            @staticmethod
            def site() -> typing.Type['SiteForm']:
                return SiteForm
            __annotations__ = {
                "copyFromSiteId": copyFromSiteId,
                "copyAll": copyAll,
                "copyTemplatesContainers": copyTemplatesContainers,
                "copyContentOnPages": copyContentOnPages,
                "copyFolders": copyFolders,
                "copyContentOnSite": copyContentOnSite,
                "copyLinks": copyLinks,
                "copySiteVariables": copySiteVariables,
                "site": site,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyFromSiteId"]) -> MetaOapg.properties.copyFromSiteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyAll"]) -> MetaOapg.properties.copyAll: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyTemplatesContainers"]) -> MetaOapg.properties.copyTemplatesContainers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyContentOnPages"]) -> MetaOapg.properties.copyContentOnPages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyFolders"]) -> MetaOapg.properties.copyFolders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyContentOnSite"]) -> MetaOapg.properties.copyContentOnSite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyLinks"]) -> MetaOapg.properties.copyLinks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copySiteVariables"]) -> MetaOapg.properties.copySiteVariables: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["site"]) -> 'SiteForm': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["copyFromSiteId", "copyAll", "copyTemplatesContainers", "copyContentOnPages", "copyFolders", "copyContentOnSite", "copyLinks", "copySiteVariables", "site", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyFromSiteId"]) -> typing.Union[MetaOapg.properties.copyFromSiteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyAll"]) -> typing.Union[MetaOapg.properties.copyAll, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyTemplatesContainers"]) -> typing.Union[MetaOapg.properties.copyTemplatesContainers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyContentOnPages"]) -> typing.Union[MetaOapg.properties.copyContentOnPages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyFolders"]) -> typing.Union[MetaOapg.properties.copyFolders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyContentOnSite"]) -> typing.Union[MetaOapg.properties.copyContentOnSite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyLinks"]) -> typing.Union[MetaOapg.properties.copyLinks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copySiteVariables"]) -> typing.Union[MetaOapg.properties.copySiteVariables, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["site"]) -> typing.Union['SiteForm', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["copyFromSiteId", "copyAll", "copyTemplatesContainers", "copyContentOnPages", "copyFolders", "copyContentOnSite", "copyLinks", "copySiteVariables", "site", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        copyFromSiteId: typing.Union[MetaOapg.properties.copyFromSiteId, str, schemas.Unset] = schemas.unset,
        copyAll: typing.Union[MetaOapg.properties.copyAll, bool, schemas.Unset] = schemas.unset,
        copyTemplatesContainers: typing.Union[MetaOapg.properties.copyTemplatesContainers, bool, schemas.Unset] = schemas.unset,
        copyContentOnPages: typing.Union[MetaOapg.properties.copyContentOnPages, bool, schemas.Unset] = schemas.unset,
        copyFolders: typing.Union[MetaOapg.properties.copyFolders, bool, schemas.Unset] = schemas.unset,
        copyContentOnSite: typing.Union[MetaOapg.properties.copyContentOnSite, bool, schemas.Unset] = schemas.unset,
        copyLinks: typing.Union[MetaOapg.properties.copyLinks, bool, schemas.Unset] = schemas.unset,
        copySiteVariables: typing.Union[MetaOapg.properties.copySiteVariables, bool, schemas.Unset] = schemas.unset,
        site: typing.Union['SiteForm', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CopySiteForm':
        return super().__new__(
            cls,
            *_args,
            copyFromSiteId=copyFromSiteId,
            copyAll=copyAll,
            copyTemplatesContainers=copyTemplatesContainers,
            copyContentOnPages=copyContentOnPages,
            copyFolders=copyFolders,
            copyContentOnSite=copyContentOnSite,
            copyLinks=copyLinks,
            copySiteVariables=copySiteVariables,
            site=site,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.site_form import SiteForm
