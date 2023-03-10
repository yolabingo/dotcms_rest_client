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


class TextField(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    searchable = schemas.BoolSchema
                    unique = schemas.BoolSchema
                    indexed = schemas.BoolSchema
                    listed = schemas.BoolSchema
                    readOnly = schemas.BoolSchema
                    forceIncludeInApi = schemas.BoolSchema
                    owner = schemas.StrSchema
                    id = schemas.StrSchema
                    modDate = schemas.DateTimeSchema
                    name = schemas.StrSchema
                    relationType = schemas.StrSchema
                    required = schemas.BoolSchema
                    variable = schemas.StrSchema
                    sortOrder = schemas.Int32Schema
                    values = schemas.StrSchema
                    regexCheck = schemas.StrSchema
                    hint = schemas.StrSchema
                    defaultValue = schemas.StrSchema
                    fixed = schemas.BoolSchema
                    contentTypeId = schemas.StrSchema
                    dbColumn = schemas.StrSchema
                    iDate = schemas.DateTimeSchema
                    
                    
                    class dataType(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def NONE(cls):
                            return cls("none")
                        
                        @schemas.classproperty
                        def BOOL(cls):
                            return cls("bool")
                        
                        @schemas.classproperty
                        def DATE(cls):
                            return cls("date")
                        
                        @schemas.classproperty
                        def FLOAT(cls):
                            return cls("float")
                        
                        @schemas.classproperty
                        def INTEGER(cls):
                            return cls("integer")
                        
                        @schemas.classproperty
                        def TEXT(cls):
                            return cls("text")
                        
                        @schemas.classproperty
                        def TEXT_AREA(cls):
                            return cls("text_area")
                        
                        @schemas.classproperty
                        def SYSTEM_FIELD(cls):
                            return cls("system_field")
                    __annotations__ = {
                        "searchable": searchable,
                        "unique": unique,
                        "indexed": indexed,
                        "listed": listed,
                        "readOnly": readOnly,
                        "forceIncludeInApi": forceIncludeInApi,
                        "owner": owner,
                        "id": id,
                        "modDate": modDate,
                        "name": name,
                        "relationType": relationType,
                        "required": required,
                        "variable": variable,
                        "sortOrder": sortOrder,
                        "values": values,
                        "regexCheck": regexCheck,
                        "hint": hint,
                        "defaultValue": defaultValue,
                        "fixed": fixed,
                        "contentTypeId": contentTypeId,
                        "dbColumn": dbColumn,
                        "iDate": iDate,
                        "dataType": dataType,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["searchable"]) -> MetaOapg.properties.searchable: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["unique"]) -> MetaOapg.properties.unique: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["indexed"]) -> MetaOapg.properties.indexed: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["listed"]) -> MetaOapg.properties.listed: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["forceIncludeInApi"]) -> MetaOapg.properties.forceIncludeInApi: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["modDate"]) -> MetaOapg.properties.modDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["relationType"]) -> MetaOapg.properties.relationType: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["sortOrder"]) -> MetaOapg.properties.sortOrder: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["values"]) -> MetaOapg.properties.values: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["regexCheck"]) -> MetaOapg.properties.regexCheck: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["hint"]) -> MetaOapg.properties.hint: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fixed"]) -> MetaOapg.properties.fixed: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["contentTypeId"]) -> MetaOapg.properties.contentTypeId: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dbColumn"]) -> MetaOapg.properties.dbColumn: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["iDate"]) -> MetaOapg.properties.iDate: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["dataType"]) -> MetaOapg.properties.dataType: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["searchable", "unique", "indexed", "listed", "readOnly", "forceIncludeInApi", "owner", "id", "modDate", "name", "relationType", "required", "variable", "sortOrder", "values", "regexCheck", "hint", "defaultValue", "fixed", "contentTypeId", "dbColumn", "iDate", "dataType", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["searchable"]) -> typing.Union[MetaOapg.properties.searchable, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["unique"]) -> typing.Union[MetaOapg.properties.unique, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["indexed"]) -> typing.Union[MetaOapg.properties.indexed, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["listed"]) -> typing.Union[MetaOapg.properties.listed, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["forceIncludeInApi"]) -> typing.Union[MetaOapg.properties.forceIncludeInApi, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["modDate"]) -> typing.Union[MetaOapg.properties.modDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["relationType"]) -> typing.Union[MetaOapg.properties.relationType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["variable"]) -> typing.Union[MetaOapg.properties.variable, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["sortOrder"]) -> typing.Union[MetaOapg.properties.sortOrder, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union[MetaOapg.properties.values, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["regexCheck"]) -> typing.Union[MetaOapg.properties.regexCheck, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["hint"]) -> typing.Union[MetaOapg.properties.hint, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fixed"]) -> typing.Union[MetaOapg.properties.fixed, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["contentTypeId"]) -> typing.Union[MetaOapg.properties.contentTypeId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dbColumn"]) -> typing.Union[MetaOapg.properties.dbColumn, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["iDate"]) -> typing.Union[MetaOapg.properties.iDate, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["dataType"]) -> typing.Union[MetaOapg.properties.dataType, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["searchable", "unique", "indexed", "listed", "readOnly", "forceIncludeInApi", "owner", "id", "modDate", "name", "relationType", "required", "variable", "sortOrder", "values", "regexCheck", "hint", "defaultValue", "fixed", "contentTypeId", "dbColumn", "iDate", "dataType", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                searchable: typing.Union[MetaOapg.properties.searchable, bool, schemas.Unset] = schemas.unset,
                unique: typing.Union[MetaOapg.properties.unique, bool, schemas.Unset] = schemas.unset,
                indexed: typing.Union[MetaOapg.properties.indexed, bool, schemas.Unset] = schemas.unset,
                listed: typing.Union[MetaOapg.properties.listed, bool, schemas.Unset] = schemas.unset,
                readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
                forceIncludeInApi: typing.Union[MetaOapg.properties.forceIncludeInApi, bool, schemas.Unset] = schemas.unset,
                owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                modDate: typing.Union[MetaOapg.properties.modDate, str, datetime, schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                relationType: typing.Union[MetaOapg.properties.relationType, str, schemas.Unset] = schemas.unset,
                required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
                variable: typing.Union[MetaOapg.properties.variable, str, schemas.Unset] = schemas.unset,
                sortOrder: typing.Union[MetaOapg.properties.sortOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                values: typing.Union[MetaOapg.properties.values, str, schemas.Unset] = schemas.unset,
                regexCheck: typing.Union[MetaOapg.properties.regexCheck, str, schemas.Unset] = schemas.unset,
                hint: typing.Union[MetaOapg.properties.hint, str, schemas.Unset] = schemas.unset,
                defaultValue: typing.Union[MetaOapg.properties.defaultValue, str, schemas.Unset] = schemas.unset,
                fixed: typing.Union[MetaOapg.properties.fixed, bool, schemas.Unset] = schemas.unset,
                contentTypeId: typing.Union[MetaOapg.properties.contentTypeId, str, schemas.Unset] = schemas.unset,
                dbColumn: typing.Union[MetaOapg.properties.dbColumn, str, schemas.Unset] = schemas.unset,
                iDate: typing.Union[MetaOapg.properties.iDate, str, datetime, schemas.Unset] = schemas.unset,
                dataType: typing.Union[MetaOapg.properties.dataType, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    searchable=searchable,
                    unique=unique,
                    indexed=indexed,
                    listed=listed,
                    readOnly=readOnly,
                    forceIncludeInApi=forceIncludeInApi,
                    owner=owner,
                    id=id,
                    modDate=modDate,
                    name=name,
                    relationType=relationType,
                    required=required,
                    variable=variable,
                    sortOrder=sortOrder,
                    values=values,
                    regexCheck=regexCheck,
                    hint=hint,
                    defaultValue=defaultValue,
                    fixed=fixed,
                    contentTypeId=contentTypeId,
                    dbColumn=dbColumn,
                    iDate=iDate,
                    dataType=dataType,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                Field,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TextField':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.field import Field
