# openapi_client.model.workflow_system_action_form.WorkflowSystemActionForm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actionId** | str,  | str,  |  | 
**systemAction** | str,  | str,  |  | must be one of ["NEW", "EDIT", "PUBLISH", "UNPUBLISH", "ARCHIVE", "UNARCHIVE", "DELETE", "DESTROY", ] 
**schemeId** | str,  | str,  |  | [optional] 
**contentTypeVariable** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

