# dotcms_rest_client.model.container.Container

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**getiDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**type** | str,  | str,  |  | [optional] 
**owner** | str,  | str,  |  | [optional] 
**inode** | str,  | str,  |  | [optional] 
**identifier** | str,  | str,  |  | [optional] 
**source** | str,  | str,  |  | [optional] must be one of ["UNKNOWN", "DB", "FILE", ] 
**title** | str,  | str,  |  | [optional] 
**friendlyName** | str,  | str,  |  | [optional] 
**modDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**modUser** | str,  | str,  |  | [optional] 
**sortOrder** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**showOnMenu** | bool,  | BoolClass,  |  | [optional] 
**code** | str,  | str,  |  | [optional] 
**maxContentlets** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**useDiv** | bool,  | BoolClass,  |  | [optional] 
**sortContentletsBy** | str,  | str,  |  | [optional] 
**preLoop** | str,  | str,  |  | [optional] 
**postLoop** | str,  | str,  |  | [optional] 
**staticify** | bool,  | BoolClass,  |  | [optional] 
**luceneQuery** | str,  | str,  |  | [optional] 
**notes** | str,  | str,  |  | [optional] 
**parentPermissionable** | [**Permissionable**](Permissionable.md) | [**Permissionable**](Permissionable.md) |  | [optional] 
**live** | bool,  | BoolClass,  |  | [optional] 
**deleted** | bool,  | BoolClass,  |  | [optional] 
**working** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**versionType** | str,  | str,  |  | [optional] 
**permissionId** | str,  | str,  |  | [optional] 
**versionId** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**locked** | bool,  | BoolClass,  |  | [optional] 
**permissionType** | str,  | str,  |  | [optional] 
**new** | bool,  | BoolClass,  |  | [optional] 
**[parents](#parents)** | list, tuple,  | tuple,  |  | [optional] 
**categoryId** | str,  | str,  |  | [optional] 
**idate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parents

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

