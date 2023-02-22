# dotcms_rest_client.model.user_api.UserAPI

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**systemUser** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**anonymousUser** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**[unDeletedUsers](#unDeletedUsers)** | list, tuple,  | tuple,  |  | [optional] 
**defaultUser** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**anonymousUserNoThrow** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# unDeletedUsers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**User**](User.md) | [**User**](User.md) | [**User**](User.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

