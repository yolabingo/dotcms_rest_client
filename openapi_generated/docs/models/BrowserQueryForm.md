# dotcms_rest_client.model.browser_query_form.BrowserQueryForm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hostFolderId** | str,  | str,  |  | [optional] 
**filter** | str,  | str,  |  | [optional] 
**sortBy** | str,  | str,  |  | [optional] 
**offset** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**maxResults** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**showWorking** | bool,  | BoolClass,  |  | [optional] 
**showArchived** | bool,  | BoolClass,  |  | [optional] 
**showFolders** | bool,  | BoolClass,  |  | [optional] 
**showFiles** | bool,  | BoolClass,  |  | [optional] 
**showPages** | bool,  | BoolClass,  |  | [optional] 
**sortByDesc** | bool,  | BoolClass,  |  | [optional] 
**showLinks** | bool,  | BoolClass,  |  | [optional] 
**showDotAssets** | bool,  | BoolClass,  |  | [optional] 
**languageId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[extensions](#extensions)** | list, tuple,  | tuple,  |  | [optional] 
**[mimeTypes](#mimeTypes)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extensions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# mimeTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

