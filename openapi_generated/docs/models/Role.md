# dotcms_rest_client.model.role.Role

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**roleKey** | str,  | str,  |  | [optional] 
**parent** | str,  | str,  |  | [optional] 
**editPermissions** | bool,  | BoolClass,  |  | [optional] 
**editUsers** | bool,  | BoolClass,  |  | [optional] 
**editLayouts** | bool,  | BoolClass,  |  | [optional] 
**locked** | bool,  | BoolClass,  |  | [optional] 
**system** | bool,  | BoolClass,  |  | [optional] 
**[roleChildren](#roleChildren)** | list, tuple,  | tuple,  |  | [optional] 
**fqn** | str,  | str,  |  | [optional] 
**dbfqn** | str,  | str,  |  | [optional] 
**user** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# roleChildren

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

