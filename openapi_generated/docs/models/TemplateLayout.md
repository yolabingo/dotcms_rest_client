# dotcms_rest_client.model.template_layout.TemplateLayout

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**width** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**header** | bool,  | BoolClass,  |  | [optional] 
**footer** | bool,  | BoolClass,  |  | [optional] 
**body** | [**Body**](Body.md) | [**Body**](Body.md) |  | [optional] 
**sidebar** | [**Sidebar**](Sidebar.md) | [**Sidebar**](Sidebar.md) |  | [optional] 
**[bodyRows](#bodyRows)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bodyRows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TemplateLayoutRow**](TemplateLayoutRow.md) | [**TemplateLayoutRow**](TemplateLayoutRow.md) | [**TemplateLayoutRow**](TemplateLayoutRow.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

