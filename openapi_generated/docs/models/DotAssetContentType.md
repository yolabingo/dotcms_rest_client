# openapi_client.model.dot_asset_content_type.DotAssetContentType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ContentType](ContentType.md) | [**ContentType**](ContentType.md) | [**ContentType**](ContentType.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**defaultType** | bool,  | BoolClass,  |  | [optional] 
**detailPage** | str,  | str,  |  | [optional] 
**fixed** | bool,  | BoolClass,  |  | [optional] 
**iDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**system** | bool,  | BoolClass,  |  | [optional] 
**versionable** | bool,  | BoolClass,  |  | [optional] 
**multilingualable** | bool,  | BoolClass,  |  | [optional] 
**variable** | str,  | str,  |  | [optional] 
**urlMapPattern** | str,  | str,  |  | [optional] 
**publishDateVar** | str,  | str,  |  | [optional] 
**expireDateVar** | str,  | str,  |  | [optional] 
**modDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**host** | str,  | str,  |  | [optional] 
**icon** | str,  | str,  |  | [optional] 
**sortOrder** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**folder** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

