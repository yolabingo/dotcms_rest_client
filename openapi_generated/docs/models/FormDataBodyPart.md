# openapi_client.model.form_data_body_part.FormDataBodyPart

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contentDisposition** | [**ContentDisposition**](ContentDisposition.md) | [**ContentDisposition**](ContentDisposition.md) |  | [optional] 
**[entity](#entity)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[mediaType](#mediaType)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[messageBodyWorkers](#messageBodyWorkers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**parent** | [**MultiPart**](MultiPart.md) | [**MultiPart**](MultiPart.md) |  | [optional] 
**[providers](#providers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**simple** | bool,  | BoolClass,  |  | [optional] 
**formDataContentDisposition** | [**FormDataContentDisposition**](FormDataContentDisposition.md) | [**FormDataContentDisposition**](FormDataContentDisposition.md) |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**[parameterizedHeaders](#parameterizedHeaders)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# entity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# mediaType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] 
**subtype** | str,  | str,  |  | [optional] 
**[parameters](#parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**wildcardType** | bool,  | BoolClass,  |  | [optional] 
**wildcardSubtype** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# messageBodyWorkers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# providers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# parameterizedHeaders

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ParameterizedHeader**](ParameterizedHeader.md) | [**ParameterizedHeader**](ParameterizedHeader.md) | [**ParameterizedHeader**](ParameterizedHeader.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

