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


class WorkflowAction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            schemeId = schemas.StrSchema
            condition = schemas.StrSchema
            nextStep = schemas.StrSchema
            nextAssign = schemas.StrSchema
            icon = schemas.StrSchema
            roleHierarchyForAssign = schemas.BoolSchema
            assignable = schemas.BoolSchema
            commentable = schemas.BoolSchema
            order = schemas.Int32Schema
            saveActionlet = schemas.BoolSchema
            publishActionlet = schemas.BoolSchema
            unpublishActionlet = schemas.BoolSchema
            archiveActionlet = schemas.BoolSchema
            pushPublishActionlet = schemas.BoolSchema
            unarchiveActionlet = schemas.BoolSchema
            deleteActionlet = schemas.BoolSchema
            destroyActionlet = schemas.BoolSchema
            moveActionlet = schemas.BoolSchema
            owner = schemas.StrSchema
            moveActionletHashPath = schemas.BoolSchema
            nextStepCurrentStep = schemas.BoolSchema
            
            
            class showOn(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "NEW": "NEW",
                                "LOCKED": "LOCKED",
                                "UNLOCKED": "UNLOCKED",
                                "PUBLISHED": "PUBLISHED",
                                "UNPUBLISHED": "UNPUBLISHED",
                                "ARCHIVED": "ARCHIVED",
                                "LISTING": "LISTING",
                                "EDITING": "EDITING",
                            }
                        
                        @schemas.classproperty
                        def NEW(cls):
                            return cls("NEW")
                        
                        @schemas.classproperty
                        def LOCKED(cls):
                            return cls("LOCKED")
                        
                        @schemas.classproperty
                        def UNLOCKED(cls):
                            return cls("UNLOCKED")
                        
                        @schemas.classproperty
                        def PUBLISHED(cls):
                            return cls("PUBLISHED")
                        
                        @schemas.classproperty
                        def UNPUBLISHED(cls):
                            return cls("UNPUBLISHED")
                        
                        @schemas.classproperty
                        def ARCHIVED(cls):
                            return cls("ARCHIVED")
                        
                        @schemas.classproperty
                        def LISTING(cls):
                            return cls("LISTING")
                        
                        @schemas.classproperty
                        def EDITING(cls):
                            return cls("EDITING")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'showOn':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "name": name,
                "schemeId": schemeId,
                "condition": condition,
                "nextStep": nextStep,
                "nextAssign": nextAssign,
                "icon": icon,
                "roleHierarchyForAssign": roleHierarchyForAssign,
                "assignable": assignable,
                "commentable": commentable,
                "order": order,
                "saveActionlet": saveActionlet,
                "publishActionlet": publishActionlet,
                "unpublishActionlet": unpublishActionlet,
                "archiveActionlet": archiveActionlet,
                "pushPublishActionlet": pushPublishActionlet,
                "unarchiveActionlet": unarchiveActionlet,
                "deleteActionlet": deleteActionlet,
                "destroyActionlet": destroyActionlet,
                "moveActionlet": moveActionlet,
                "owner": owner,
                "moveActionletHashPath": moveActionletHashPath,
                "nextStepCurrentStep": nextStepCurrentStep,
                "showOn": showOn,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemeId"]) -> MetaOapg.properties.schemeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["condition"]) -> MetaOapg.properties.condition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextStep"]) -> MetaOapg.properties.nextStep: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextAssign"]) -> MetaOapg.properties.nextAssign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleHierarchyForAssign"]) -> MetaOapg.properties.roleHierarchyForAssign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignable"]) -> MetaOapg.properties.assignable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commentable"]) -> MetaOapg.properties.commentable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saveActionlet"]) -> MetaOapg.properties.saveActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publishActionlet"]) -> MetaOapg.properties.publishActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unpublishActionlet"]) -> MetaOapg.properties.unpublishActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archiveActionlet"]) -> MetaOapg.properties.archiveActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pushPublishActionlet"]) -> MetaOapg.properties.pushPublishActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unarchiveActionlet"]) -> MetaOapg.properties.unarchiveActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteActionlet"]) -> MetaOapg.properties.deleteActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destroyActionlet"]) -> MetaOapg.properties.destroyActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moveActionlet"]) -> MetaOapg.properties.moveActionlet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner"]) -> MetaOapg.properties.owner: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["moveActionletHashPath"]) -> MetaOapg.properties.moveActionletHashPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextStepCurrentStep"]) -> MetaOapg.properties.nextStepCurrentStep: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["showOn"]) -> MetaOapg.properties.showOn: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "schemeId", "condition", "nextStep", "nextAssign", "icon", "roleHierarchyForAssign", "assignable", "commentable", "order", "saveActionlet", "publishActionlet", "unpublishActionlet", "archiveActionlet", "pushPublishActionlet", "unarchiveActionlet", "deleteActionlet", "destroyActionlet", "moveActionlet", "owner", "moveActionletHashPath", "nextStepCurrentStep", "showOn", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemeId"]) -> typing.Union[MetaOapg.properties.schemeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["condition"]) -> typing.Union[MetaOapg.properties.condition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextStep"]) -> typing.Union[MetaOapg.properties.nextStep, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextAssign"]) -> typing.Union[MetaOapg.properties.nextAssign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleHierarchyForAssign"]) -> typing.Union[MetaOapg.properties.roleHierarchyForAssign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignable"]) -> typing.Union[MetaOapg.properties.assignable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commentable"]) -> typing.Union[MetaOapg.properties.commentable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saveActionlet"]) -> typing.Union[MetaOapg.properties.saveActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publishActionlet"]) -> typing.Union[MetaOapg.properties.publishActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unpublishActionlet"]) -> typing.Union[MetaOapg.properties.unpublishActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archiveActionlet"]) -> typing.Union[MetaOapg.properties.archiveActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pushPublishActionlet"]) -> typing.Union[MetaOapg.properties.pushPublishActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unarchiveActionlet"]) -> typing.Union[MetaOapg.properties.unarchiveActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteActionlet"]) -> typing.Union[MetaOapg.properties.deleteActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destroyActionlet"]) -> typing.Union[MetaOapg.properties.destroyActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moveActionlet"]) -> typing.Union[MetaOapg.properties.moveActionlet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner"]) -> typing.Union[MetaOapg.properties.owner, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["moveActionletHashPath"]) -> typing.Union[MetaOapg.properties.moveActionletHashPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextStepCurrentStep"]) -> typing.Union[MetaOapg.properties.nextStepCurrentStep, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["showOn"]) -> typing.Union[MetaOapg.properties.showOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "schemeId", "condition", "nextStep", "nextAssign", "icon", "roleHierarchyForAssign", "assignable", "commentable", "order", "saveActionlet", "publishActionlet", "unpublishActionlet", "archiveActionlet", "pushPublishActionlet", "unarchiveActionlet", "deleteActionlet", "destroyActionlet", "moveActionlet", "owner", "moveActionletHashPath", "nextStepCurrentStep", "showOn", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        schemeId: typing.Union[MetaOapg.properties.schemeId, str, schemas.Unset] = schemas.unset,
        condition: typing.Union[MetaOapg.properties.condition, str, schemas.Unset] = schemas.unset,
        nextStep: typing.Union[MetaOapg.properties.nextStep, str, schemas.Unset] = schemas.unset,
        nextAssign: typing.Union[MetaOapg.properties.nextAssign, str, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        roleHierarchyForAssign: typing.Union[MetaOapg.properties.roleHierarchyForAssign, bool, schemas.Unset] = schemas.unset,
        assignable: typing.Union[MetaOapg.properties.assignable, bool, schemas.Unset] = schemas.unset,
        commentable: typing.Union[MetaOapg.properties.commentable, bool, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        saveActionlet: typing.Union[MetaOapg.properties.saveActionlet, bool, schemas.Unset] = schemas.unset,
        publishActionlet: typing.Union[MetaOapg.properties.publishActionlet, bool, schemas.Unset] = schemas.unset,
        unpublishActionlet: typing.Union[MetaOapg.properties.unpublishActionlet, bool, schemas.Unset] = schemas.unset,
        archiveActionlet: typing.Union[MetaOapg.properties.archiveActionlet, bool, schemas.Unset] = schemas.unset,
        pushPublishActionlet: typing.Union[MetaOapg.properties.pushPublishActionlet, bool, schemas.Unset] = schemas.unset,
        unarchiveActionlet: typing.Union[MetaOapg.properties.unarchiveActionlet, bool, schemas.Unset] = schemas.unset,
        deleteActionlet: typing.Union[MetaOapg.properties.deleteActionlet, bool, schemas.Unset] = schemas.unset,
        destroyActionlet: typing.Union[MetaOapg.properties.destroyActionlet, bool, schemas.Unset] = schemas.unset,
        moveActionlet: typing.Union[MetaOapg.properties.moveActionlet, bool, schemas.Unset] = schemas.unset,
        owner: typing.Union[MetaOapg.properties.owner, str, schemas.Unset] = schemas.unset,
        moveActionletHashPath: typing.Union[MetaOapg.properties.moveActionletHashPath, bool, schemas.Unset] = schemas.unset,
        nextStepCurrentStep: typing.Union[MetaOapg.properties.nextStepCurrentStep, bool, schemas.Unset] = schemas.unset,
        showOn: typing.Union[MetaOapg.properties.showOn, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowAction':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            schemeId=schemeId,
            condition=condition,
            nextStep=nextStep,
            nextAssign=nextAssign,
            icon=icon,
            roleHierarchyForAssign=roleHierarchyForAssign,
            assignable=assignable,
            commentable=commentable,
            order=order,
            saveActionlet=saveActionlet,
            publishActionlet=publishActionlet,
            unpublishActionlet=unpublishActionlet,
            archiveActionlet=archiveActionlet,
            pushPublishActionlet=pushPublishActionlet,
            unarchiveActionlet=unarchiveActionlet,
            deleteActionlet=deleteActionlet,
            destroyActionlet=destroyActionlet,
            moveActionlet=moveActionlet,
            owner=owner,
            moveActionletHashPath=moveActionletHashPath,
            nextStepCurrentStep=nextStepCurrentStep,
            showOn=showOn,
            _configuration=_configuration,
            **kwargs,
        )
