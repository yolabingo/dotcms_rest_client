# openapi_client.model.workflow_action_form.WorkflowActionForm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actionAssignable** | bool,  | BoolClass,  |  | 
**actionNextStep** | str,  | str,  |  | 
**actionRoleHierarchyForAssign** | bool,  | BoolClass,  |  | 
**[showOn](#showOn)** | list, tuple,  | tuple,  |  | 
**schemeId** | str,  | str,  |  | 
**requiresCheckout** | bool,  | BoolClass,  |  | 
**actionCommentable** | bool,  | BoolClass,  |  | 
**actionName** | str,  | str,  |  | 
**actionId** | str,  | str,  |  | [optional] 
**stepId** | str,  | str,  |  | [optional] 
**[whoCanUse](#whoCanUse)** | list, tuple,  | tuple,  |  | [optional] 
**actionIcon** | str,  | str,  |  | [optional] 
**roleHierarchyForAssign** | bool,  | BoolClass,  |  | [optional] 
**actionNextAssign** | str,  | str,  |  | [optional] 
**actionCondition** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# showOn

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NEW", "LOCKED", "UNLOCKED", "PUBLISHED", "UNPUBLISHED", "ARCHIVED", "LISTING", "EDITING", ] 

# whoCanUse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

