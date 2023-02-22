# dotcms_rest_client.model.persona.Persona

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[map](#map)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**lowIndexPriority** | bool,  | BoolClass,  |  | [optional] 
**userAPI** | [**UserAPI**](UserAPI.md) | [**UserAPI**](UserAPI.md) |  | [optional] 
**indexPolicyDependencies** | str,  | str,  |  | [optional] must be one of ["DEFER", "WAIT_FOR", "FORCE", ] 
**description** | str,  | str,  |  | [optional] 
**tags** | str,  | str,  |  | [optional] 
**keyTag** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**identifier** | str,  | str,  |  | [optional] 
**inode** | str,  | str,  |  | [optional] 
**live** | bool,  | BoolClass,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**working** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**versionType** | str,  | str,  |  | [optional] 
**modDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**versionId** | str,  | str,  |  | [optional] 
**modUser** | str,  | str,  |  | [optional] 
**locked** | bool,  | BoolClass,  |  | [optional] 
**owner** | str,  | str,  |  | [optional] 
**permissionId** | str,  | str,  |  | [optional] 
**permissionType** | str,  | str,  |  | [optional] 
**host** | str,  | str,  |  | [optional] 
**new** | bool,  | BoolClass,  |  | [optional] 
**languageId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**folder** | str,  | str,  |  | [optional] 
**fileAsset** | bool,  | BoolClass,  |  | [optional] 
**structureInode** | str,  | str,  |  | [optional] 
**systemHost** | bool,  | BoolClass,  |  | [optional] 
**categoryId** | str,  | str,  |  | [optional] 
**contentTypeId** | str,  | str,  |  | [optional] 
**sortOrder** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**titleImage** | [**Field**](Field.md) | [**Field**](Field.md) |  | [optional] 
**htmlpage** | bool,  | BoolClass,  |  | [optional] 
**dotAsset** | bool,  | BoolClass,  |  | [optional] 
**persona** | bool,  | BoolClass,  |  | [optional] 
**form** | bool,  | BoolClass,  |  | [optional] 
**variantId** | str,  | str,  |  | [optional] 
**vanityUrl** | bool,  | BoolClass,  |  | [optional] 
**keyValue** | bool,  | BoolClass,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# map

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

