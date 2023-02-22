# dotcms_rest_client.model.permission_view.PermissionView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**inode** | str,  | str,  |  | [optional] 
**roleId** | str,  | str,  |  | [optional] 
**permission** | str,  | str,  |  | [optional] must be one of ["READ", "USE", "EDIT", "WRITE", "PUBLISH", "EDIT_PERMISSIONS", "CAN_ADD_CHILDREN", ] 
**type** | str,  | str,  |  | [optional] 
**bitPermission** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

