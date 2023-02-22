# openapi_client.model.workflow_action.WorkflowAction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**schemeId** | str,  | str,  |  | [optional] 
**condition** | str,  | str,  |  | [optional] 
**nextStep** | str,  | str,  |  | [optional] 
**nextAssign** | str,  | str,  |  | [optional] 
**icon** | str,  | str,  |  | [optional] 
**roleHierarchyForAssign** | bool,  | BoolClass,  |  | [optional] 
**assignable** | bool,  | BoolClass,  |  | [optional] 
**commentable** | bool,  | BoolClass,  |  | [optional] 
**order** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**saveActionlet** | bool,  | BoolClass,  |  | [optional] 
**publishActionlet** | bool,  | BoolClass,  |  | [optional] 
**unpublishActionlet** | bool,  | BoolClass,  |  | [optional] 
**archiveActionlet** | bool,  | BoolClass,  |  | [optional] 
**pushPublishActionlet** | bool,  | BoolClass,  |  | [optional] 
**unarchiveActionlet** | bool,  | BoolClass,  |  | [optional] 
**deleteActionlet** | bool,  | BoolClass,  |  | [optional] 
**destroyActionlet** | bool,  | BoolClass,  |  | [optional] 
**moveActionlet** | bool,  | BoolClass,  |  | [optional] 
**owner** | str,  | str,  |  | [optional] 
**moveActionletHashPath** | bool,  | BoolClass,  |  | [optional] 
**nextStepCurrentStep** | bool,  | BoolClass,  |  | [optional] 
**[showOn](#showOn)** | list, tuple,  | tuple,  |  | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

