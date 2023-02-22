# openapi_client.model.checkbox_field.CheckboxField

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Field](Field.md) | [**Field**](Field.md) | [**Field**](Field.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**searchable** | bool,  | BoolClass,  |  | [optional] 
**unique** | bool,  | BoolClass,  |  | [optional] 
**indexed** | bool,  | BoolClass,  |  | [optional] 
**listed** | bool,  | BoolClass,  |  | [optional] 
**readOnly** | bool,  | BoolClass,  |  | [optional] 
**forceIncludeInApi** | bool,  | BoolClass,  |  | [optional] 
**owner** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**modDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**name** | str,  | str,  |  | [optional] 
**relationType** | str,  | str,  |  | [optional] 
**required** | bool,  | BoolClass,  |  | [optional] 
**variable** | str,  | str,  |  | [optional] 
**sortOrder** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**values** | str,  | str,  |  | [optional] 
**regexCheck** | str,  | str,  |  | [optional] 
**hint** | str,  | str,  |  | [optional] 
**defaultValue** | str,  | str,  |  | [optional] 
**fixed** | bool,  | BoolClass,  |  | [optional] 
**contentTypeId** | str,  | str,  |  | [optional] 
**dbColumn** | str,  | str,  |  | [optional] 
**iDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**dataType** | str,  | str,  |  | [optional] must be one of ["none", "bool", "date", "float", "integer", "text", "text_area", "system_field", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

