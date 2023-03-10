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


class FormDataMultiPart(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def contentDisposition() -> typing.Type['ContentDisposition']:
                return ContentDisposition
            entity = schemas.DictSchema
            
            
            class headers(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'headers':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class mediaType(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        type = schemas.StrSchema
                        subtype = schemas.StrSchema
                        
                        
                        class parameters(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                additional_properties = schemas.StrSchema
                            
                            def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                return super().get_item_oapg(name)
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                            ) -> 'parameters':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        wildcardType = schemas.BoolSchema
                        wildcardSubtype = schemas.BoolSchema
                        __annotations__ = {
                            "type": type,
                            "subtype": subtype,
                            "parameters": parameters,
                            "wildcardType": wildcardType,
                            "wildcardSubtype": wildcardSubtype,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["subtype"]) -> MetaOapg.properties.subtype: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["wildcardType"]) -> MetaOapg.properties.wildcardType: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["wildcardSubtype"]) -> MetaOapg.properties.wildcardSubtype: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "subtype", "parameters", "wildcardType", "wildcardSubtype", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["subtype"]) -> typing.Union[MetaOapg.properties.subtype, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> typing.Union[MetaOapg.properties.parameters, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["wildcardType"]) -> typing.Union[MetaOapg.properties.wildcardType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["wildcardSubtype"]) -> typing.Union[MetaOapg.properties.wildcardSubtype, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "subtype", "parameters", "wildcardType", "wildcardSubtype", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    subtype: typing.Union[MetaOapg.properties.subtype, str, schemas.Unset] = schemas.unset,
                    parameters: typing.Union[MetaOapg.properties.parameters, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    wildcardType: typing.Union[MetaOapg.properties.wildcardType, bool, schemas.Unset] = schemas.unset,
                    wildcardSubtype: typing.Union[MetaOapg.properties.wildcardSubtype, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'mediaType':
                    return super().__new__(
                        cls,
                        *_args,
                        type=type,
                        subtype=subtype,
                        parameters=parameters,
                        wildcardType=wildcardType,
                        wildcardSubtype=wildcardSubtype,
                        _configuration=_configuration,
                        **kwargs,
                    )
            messageBodyWorkers = schemas.DictSchema
        
            @staticmethod
            def parent() -> typing.Type['MultiPart']:
                return MultiPart
            providers = schemas.DictSchema
            
            
            class bodyParts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BodyPart']:
                        return BodyPart
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BodyPart'], typing.List['BodyPart']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bodyParts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BodyPart':
                    return super().__getitem__(i)
            
            
            class fields(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['FormDataBodyPart']:
                                return FormDataBodyPart
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['FormDataBodyPart'], typing.List['FormDataBodyPart']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'FormDataBodyPart':
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'fields':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class parameterizedHeaders(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ParameterizedHeader']:
                                return ParameterizedHeader
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['ParameterizedHeader'], typing.List['ParameterizedHeader']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ParameterizedHeader':
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'parameterizedHeaders':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "contentDisposition": contentDisposition,
                "entity": entity,
                "headers": headers,
                "mediaType": mediaType,
                "messageBodyWorkers": messageBodyWorkers,
                "parent": parent,
                "providers": providers,
                "bodyParts": bodyParts,
                "fields": fields,
                "parameterizedHeaders": parameterizedHeaders,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentDisposition"]) -> 'ContentDisposition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity"]) -> MetaOapg.properties.entity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headers"]) -> MetaOapg.properties.headers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mediaType"]) -> MetaOapg.properties.mediaType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageBodyWorkers"]) -> MetaOapg.properties.messageBodyWorkers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'MultiPart': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providers"]) -> MetaOapg.properties.providers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyParts"]) -> MetaOapg.properties.bodyParts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameterizedHeaders"]) -> MetaOapg.properties.parameterizedHeaders: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contentDisposition", "entity", "headers", "mediaType", "messageBodyWorkers", "parent", "providers", "bodyParts", "fields", "parameterizedHeaders", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentDisposition"]) -> typing.Union['ContentDisposition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity"]) -> typing.Union[MetaOapg.properties.entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headers"]) -> typing.Union[MetaOapg.properties.headers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mediaType"]) -> typing.Union[MetaOapg.properties.mediaType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageBodyWorkers"]) -> typing.Union[MetaOapg.properties.messageBodyWorkers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['MultiPart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providers"]) -> typing.Union[MetaOapg.properties.providers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyParts"]) -> typing.Union[MetaOapg.properties.bodyParts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union[MetaOapg.properties.fields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameterizedHeaders"]) -> typing.Union[MetaOapg.properties.parameterizedHeaders, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contentDisposition", "entity", "headers", "mediaType", "messageBodyWorkers", "parent", "providers", "bodyParts", "fields", "parameterizedHeaders", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        contentDisposition: typing.Union['ContentDisposition', schemas.Unset] = schemas.unset,
        entity: typing.Union[MetaOapg.properties.entity, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        headers: typing.Union[MetaOapg.properties.headers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        mediaType: typing.Union[MetaOapg.properties.mediaType, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        messageBodyWorkers: typing.Union[MetaOapg.properties.messageBodyWorkers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        parent: typing.Union['MultiPart', schemas.Unset] = schemas.unset,
        providers: typing.Union[MetaOapg.properties.providers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        bodyParts: typing.Union[MetaOapg.properties.bodyParts, list, tuple, schemas.Unset] = schemas.unset,
        fields: typing.Union[MetaOapg.properties.fields, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        parameterizedHeaders: typing.Union[MetaOapg.properties.parameterizedHeaders, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormDataMultiPart':
        return super().__new__(
            cls,
            *_args,
            contentDisposition=contentDisposition,
            entity=entity,
            headers=headers,
            mediaType=mediaType,
            messageBodyWorkers=messageBodyWorkers,
            parent=parent,
            providers=providers,
            bodyParts=bodyParts,
            fields=fields,
            parameterizedHeaders=parameterizedHeaders,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.body_part import BodyPart
from openapi_client.model.content_disposition import ContentDisposition
from openapi_client.model.form_data_body_part import FormDataBodyPart
from openapi_client.model.multi_part import MultiPart
from openapi_client.model.parameterized_header import ParameterizedHeader
