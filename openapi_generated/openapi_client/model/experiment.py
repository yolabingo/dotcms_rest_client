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


class Experiment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            identifier = schemas.StrSchema
            permissionId = schemas.StrSchema
            owner = schemas.StrSchema
            permissionType = schemas.StrSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "RUNNING": "RUNNING",
                        "SCHEDULED": "SCHEDULED",
                        "ENDED": "ENDED",
                        "DRAFT": "DRAFT",
                        "ARCHIVED": "ARCHIVED",
                    }
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def SCHEDULED(cls):
                    return cls("SCHEDULED")
                
                @schemas.classproperty
                def ENDED(cls):
                    return cls("ENDED")
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("DRAFT")
                
                @schemas.classproperty
                def ARCHIVED(cls):
                    return cls("ARCHIVED")
        
            @staticmethod
            def trafficProportion() -> typing.Type['TrafficProportion']:
                return TrafficProportion
        
            @staticmethod
            def scheduling() -> typing.Type['Scheduling']:
                return Scheduling
            trafficAllocation = schemas.Float32Schema
            creationDate = schemas.DateTimeSchema
            modDate = schemas.DateTimeSchema
            pageId = schemas.StrSchema
            createdBy = schemas.StrSchema
            lastModifiedBy = schemas.StrSchema
        
            @staticmethod
            def goals() -> typing.Type['Goals']:
                return Goals
            
            
            class targetingConditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TargetingCondition']:
                        return TargetingCondition
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TargetingCondition'], typing.List['TargetingCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetingConditions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TargetingCondition':
                    return super().__getitem__(i)
            lookbackWindow = schemas.Int32Schema
            __annotations__ = {
                "identifier": identifier,
                "permissionId": permissionId,
                "owner": owner,
                "permissionType": permissionType,
                "name": name,
                "description": description,
                "id": id,
                "status": status,
                "trafficProportion": trafficProportion,
                "scheduling": scheduling,
                "trafficAllocation": trafficAllocation,
                "creationDate": creationDate,
                "modDate": modDate,
                "pageId": pageId,
                "createdBy": createdBy,
                "lastModifiedBy": lastModifiedBy,
                "goals": goals,
                "targetingConditions": targetingConditions,
                "lookbackWindow": lookbackWindow,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissionId"]) -> MetaOapg.properties.permissionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissionType"]) -> MetaOapg.properties.permissionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trafficProportion"]) -> 'TrafficProportion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduling"]) -> 'Scheduling': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trafficAllocation"]) -> MetaOapg.properties.trafficAllocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modDate"]) -> MetaOapg.properties.modDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageId"]) -> MetaOapg.properties.pageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdBy"]) -> MetaOapg.properties.createdBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastModifiedBy"]) -> MetaOapg.properties.lastModifiedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goals"]) -> 'Goals': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetingConditions"]) -> MetaOapg.properties.targetingConditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lookbackWindow"]) -> MetaOapg.properties.lookbackWindow: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["identifier", "permissionId", "owner", "permissionType", "name", "description", "id", "status", "trafficProportion", "scheduling", "trafficAllocation", "creationDate", "modDate", "pageId", "createdBy", "lastModifiedBy", "goals", "targetingConditions", "lookbackWindow", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier"]) -> typing.Union[MetaOapg.properties.identifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissionId"]) -> typing.Union[MetaOapg.properties.permissionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissionType"]) -> typing.Union[MetaOapg.properties.permissionType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trafficProportion"]) -> typing.Union['TrafficProportion', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduling"]) -> typing.Union['Scheduling', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trafficAllocation"]) -> typing.Union[MetaOapg.properties.trafficAllocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDate"]) -> typing.Union[MetaOapg.properties.creationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modDate"]) -> typing.Union[MetaOapg.properties.modDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageId"]) -> typing.Union[MetaOapg.properties.pageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdBy"]) -> typing.Union[MetaOapg.properties.createdBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastModifiedBy"]) -> typing.Union[MetaOapg.properties.lastModifiedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goals"]) -> typing.Union['Goals', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetingConditions"]) -> typing.Union[MetaOapg.properties.targetingConditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lookbackWindow"]) -> typing.Union[MetaOapg.properties.lookbackWindow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["identifier", "permissionId", "owner", "permissionType", "name", "description", "id", "status", "trafficProportion", "scheduling", "trafficAllocation", "creationDate", "modDate", "pageId", "createdBy", "lastModifiedBy", "goals", "targetingConditions", "lookbackWindow", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        identifier: typing.Union[MetaOapg.properties.identifier, str, schemas.Unset] = schemas.unset,
        permissionId: typing.Union[MetaOapg.properties.permissionId, str, schemas.Unset] = schemas.unset,
        owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
        permissionType: typing.Union[MetaOapg.properties.permissionType, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        trafficProportion: typing.Union['TrafficProportion', schemas.Unset] = schemas.unset,
        scheduling: typing.Union['Scheduling', schemas.Unset] = schemas.unset,
        trafficAllocation: typing.Union[MetaOapg.properties.trafficAllocation, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        creationDate: typing.Union[MetaOapg.properties.creationDate, str, datetime, schemas.Unset] = schemas.unset,
        modDate: typing.Union[MetaOapg.properties.modDate, str, datetime, schemas.Unset] = schemas.unset,
        pageId: typing.Union[MetaOapg.properties.pageId, str, schemas.Unset] = schemas.unset,
        createdBy: typing.Union[MetaOapg.properties.createdBy, str, schemas.Unset] = schemas.unset,
        lastModifiedBy: typing.Union[MetaOapg.properties.lastModifiedBy, str, schemas.Unset] = schemas.unset,
        goals: typing.Union['Goals', schemas.Unset] = schemas.unset,
        targetingConditions: typing.Union[MetaOapg.properties.targetingConditions, list, tuple, schemas.Unset] = schemas.unset,
        lookbackWindow: typing.Union[MetaOapg.properties.lookbackWindow, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Experiment':
        return super().__new__(
            cls,
            *_args,
            identifier=identifier,
            permissionId=permissionId,
            owner=owner,
            permissionType=permissionType,
            name=name,
            description=description,
            id=id,
            status=status,
            trafficProportion=trafficProportion,
            scheduling=scheduling,
            trafficAllocation=trafficAllocation,
            creationDate=creationDate,
            modDate=modDate,
            pageId=pageId,
            createdBy=createdBy,
            lastModifiedBy=lastModifiedBy,
            goals=goals,
            targetingConditions=targetingConditions,
            lookbackWindow=lookbackWindow,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.goals import Goals
from openapi_client.model.scheduling import Scheduling
from openapi_client.model.targeting_condition import TargetingCondition
from openapi_client.model.traffic_proportion import TrafficProportion