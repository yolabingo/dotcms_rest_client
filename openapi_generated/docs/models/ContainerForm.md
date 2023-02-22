# openapi_client.model.container_form.ContainerForm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**identifier** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**friendlyName** | str,  | str,  |  | [optional] 
**maxContentlets** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**code** | str,  | str,  |  | [optional] 
**notes** | str,  | str,  |  | [optional] 
**preLoop** | str,  | str,  |  | [optional] 
**postLoop** | str,  | str,  |  | [optional] 
**showOnMenu** | bool,  | BoolClass,  |  | [optional] 
**sortOrder** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**sortContentletsBy** | str,  | str,  |  | [optional] 
**structureInode** | str,  | str,  |  | [optional] 
**[containerStructures](#containerStructures)** | list, tuple,  | tuple,  |  | [optional] 
**owner** | str,  | str,  |  | [optional] 
**hostId** | str,  | str,  |  | [optional] 
**staticify** | bool,  | BoolClass,  |  | [optional] 
**useDiv** | bool,  | BoolClass,  |  | [optional] 
**dynamic** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# containerStructures

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ContainerStructure**](ContainerStructure.md) | [**ContainerStructure**](ContainerStructure.md) | [**ContainerStructure**](ContainerStructure.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

