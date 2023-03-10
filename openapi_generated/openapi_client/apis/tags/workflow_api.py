# coding: utf-8

"""
    dotCMS REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.v1_workflow_steps.post import AddStep
from openapi_client.paths.v1_workflow_schemes_scheme_id_copy.post import CopyScheme
from openapi_client.paths.v1_workflow_actions_action_id.delete import DeleteAction
from openapi_client.paths.v1_workflow_steps_step_id_actions_action_id.delete import DeleteAction1
from openapi_client.paths.v1_workflow_actionlets_actionlet_id.delete import DeleteActionlet
from openapi_client.paths.v1_workflow_schemes_scheme_id.delete import DeleteScheme
from openapi_client.paths.v1_workflow_steps_step_id.delete import DeleteStep
from openapi_client.paths.v1_workflow_system_actions_identifier.delete import DeletesSystemAction
from openapi_client.paths.v1_workflow_actions_action_id_condition.get import EvaluateActionCondition
from openapi_client.paths.v1_workflow_schemes_scheme_id_export.get import ExportScheme
from openapi_client.paths.v1_workflow_actions_action_id.get import FindAction
from openapi_client.paths.v1_workflow_steps_step_id_actions_action_id.get import FindActionByStep
from openapi_client.paths.v1_workflow_actionlets.get import FindActionlets
from openapi_client.paths.v1_workflow_actions_action_id_actionlets.get import FindActionletsByAction
from openapi_client.paths.v1_workflow_schemes_scheme_id_actions.get import FindActionsByScheme
from openapi_client.paths.v1_workflow_schemes_actions_system_action.post import FindActionsBySchemesAndSystemAction
from openapi_client.paths.v1_workflow_steps_step_id_actions.get import FindActionsByStep
from openapi_client.paths.v1_workflow_schemes_schemescontenttypes_content_type_id.get import FindAllSchemesAndSchemesByContentType
from openapi_client.paths.v1_workflow_contentlet_inode_actions.get import FindAvailableActions
from openapi_client.paths.v1_workflow_defaultactions_contenttype_content_type_id.get import FindAvailableDefaultActionsByContentType
from openapi_client.paths.v1_workflow_defaultactions_schemes.get import FindAvailableDefaultActionsBySchemes
from openapi_client.paths.v1_workflow_initialactions_contenttype_content_type_id.get import FindInitialAvailableActionsByContentType
from openapi_client.paths.v1_workflow_schemes.get import FindSchemes
from openapi_client.paths.v1_workflow_steps_step_id.get import FindStepById
from openapi_client.paths.v1_workflow_schemes_scheme_id_steps.get import FindStepsByScheme
from openapi_client.paths.v1_workflow_contenttypes_content_type_var_or_id_system_actions.get import FindSystemActionsByContentType
from openapi_client.paths.v1_workflow_schemes_scheme_id_system_actions.get import FindSystemActionsByScheme
from openapi_client.paths.v1_workflow_actions_fire.put import FireActionByNameSinglePart
from openapi_client.paths.v1_workflow_actions_default_firemultipart_system_action.put import FireActionDefaultMultipartNewPath
from openapi_client.paths.v1_workflow_actions_default_fire_system_action.put import FireActionDefaultSinglePart
from openapi_client.paths.v1_workflow_actions_action_id_firemultipart.put import FireActionMultipartNewPath
from openapi_client.paths.v1_workflow_actions_action_id_fire.put import FireActionSinglePart
from openapi_client.paths.v1_workflow_contentlet_actions__bulkfire.post import FireBulkActions
from openapi_client.paths.v1_workflow_contentlet_actions_bulk_fire.put import FireBulkActions1
from openapi_client.paths.v1_workflow_actions_default_fire_system_action.patch import FireMergeActionDefault
from openapi_client.paths.v1_workflow_actions_default_fire_system_action.post import FireMultipleActionDefault
from openapi_client.paths.v1_workflow_contentlet_actions_bulk.post import GetBulkActions
from openapi_client.paths.v1_workflow_system_actions_workflow_action_id.get import GetSystemActionsReferredByWorkflowAction
from openapi_client.paths.v1_workflow_schemes_import.post import ImportScheme
from openapi_client.paths.v1_workflow_reorder_steps_step_id_actions_action_id.put import ReorderAction
from openapi_client.paths.v1_workflow_reorder_step_step_id_order_order.put import ReorderStep
from openapi_client.paths.v1_workflow_actions.post import SaveAction
from openapi_client.paths.v1_workflow_steps_step_id_actions.post import SaveActionToStep
from openapi_client.paths.v1_workflow_actions_action_id_actionlets.post import SaveActionletToAction
from openapi_client.paths.v1_workflow_schemes.post import SaveScheme
from openapi_client.paths.v1_workflow_system_actions.put import SaveSystemAction
from openapi_client.paths.v1_workflow_actions_action_id.put import UpdateAction
from openapi_client.paths.v1_workflow_schemes_scheme_id.put import UpdateScheme
from openapi_client.paths.v1_workflow_steps_step_id.put import UpdateStep


class WorkflowApi(
    AddStep,
    CopyScheme,
    DeleteAction,
    DeleteAction1,
    DeleteActionlet,
    DeleteScheme,
    DeleteStep,
    DeletesSystemAction,
    EvaluateActionCondition,
    ExportScheme,
    FindAction,
    FindActionByStep,
    FindActionlets,
    FindActionletsByAction,
    FindActionsByScheme,
    FindActionsBySchemesAndSystemAction,
    FindActionsByStep,
    FindAllSchemesAndSchemesByContentType,
    FindAvailableActions,
    FindAvailableDefaultActionsByContentType,
    FindAvailableDefaultActionsBySchemes,
    FindInitialAvailableActionsByContentType,
    FindSchemes,
    FindStepById,
    FindStepsByScheme,
    FindSystemActionsByContentType,
    FindSystemActionsByScheme,
    FireActionByNameSinglePart,
    FireActionDefaultMultipartNewPath,
    FireActionDefaultSinglePart,
    FireActionMultipartNewPath,
    FireActionSinglePart,
    FireBulkActions,
    FireBulkActions1,
    FireMergeActionDefault,
    FireMultipleActionDefault,
    GetBulkActions,
    GetSystemActionsReferredByWorkflowAction,
    ImportScheme,
    ReorderAction,
    ReorderStep,
    SaveAction,
    SaveActionToStep,
    SaveActionletToAction,
    SaveScheme,
    SaveSystemAction,
    UpdateAction,
    UpdateScheme,
    UpdateStep,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
