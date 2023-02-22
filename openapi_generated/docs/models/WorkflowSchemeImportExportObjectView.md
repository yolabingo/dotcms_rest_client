# dotcms_rest_client.model.workflow_scheme_import_export_object_view.WorkflowSchemeImportExportObjectView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**version** | str,  | str,  |  | [optional] 
**[schemes](#schemes)** | list, tuple,  | tuple,  |  | [optional] 
**[steps](#steps)** | list, tuple,  | tuple,  |  | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  |  | [optional] 
**[actionSteps](#actionSteps)** | list, tuple,  | tuple,  |  | [optional] 
**[actionClasses](#actionClasses)** | list, tuple,  | tuple,  |  | [optional] 
**[actionClassParams](#actionClassParams)** | list, tuple,  | tuple,  |  | [optional] 
**[schemeSystemActionWorkflowActionMappings](#schemeSystemActionWorkflowActionMappings)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# schemes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowScheme**](WorkflowScheme.md) | [**WorkflowScheme**](WorkflowScheme.md) | [**WorkflowScheme**](WorkflowScheme.md) |  | 

# steps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowStep**](WorkflowStep.md) | [**WorkflowStep**](WorkflowStep.md) | [**WorkflowStep**](WorkflowStep.md) |  | 

# actions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowAction**](WorkflowAction.md) | [**WorkflowAction**](WorkflowAction.md) | [**WorkflowAction**](WorkflowAction.md) |  | 

# actionSteps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# actionClasses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowActionClass**](WorkflowActionClass.md) | [**WorkflowActionClass**](WorkflowActionClass.md) | [**WorkflowActionClass**](WorkflowActionClass.md) |  | 

# actionClassParams

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowActionClassParameter**](WorkflowActionClassParameter.md) | [**WorkflowActionClassParameter**](WorkflowActionClassParameter.md) | [**WorkflowActionClassParameter**](WorkflowActionClassParameter.md) |  | 

# schemeSystemActionWorkflowActionMappings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SystemActionWorkflowActionMapping**](SystemActionWorkflowActionMapping.md) | [**SystemActionWorkflowActionMapping**](SystemActionWorkflowActionMapping.md) | [**SystemActionWorkflowActionMapping**](SystemActionWorkflowActionMapping.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

