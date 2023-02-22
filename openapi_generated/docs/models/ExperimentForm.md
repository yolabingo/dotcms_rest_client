# dotcms_rest_client.model.experiment_form.ExperimentForm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**pageId** | str,  | str,  |  | [optional] 
**trafficAllocation** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**trafficProportion** | [**TrafficProportion**](TrafficProportion.md) | [**TrafficProportion**](TrafficProportion.md) |  | [optional] 
**scheduling** | [**Scheduling**](Scheduling.md) | [**Scheduling**](Scheduling.md) |  | [optional] 
**goals** | [**Goals**](Goals.md) | [**Goals**](Goals.md) |  | [optional] 
**[targetingConditions](#targetingConditions)** | list, tuple,  | tuple,  |  | [optional] 
**lookbackWindow** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetingConditions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TargetingCondition**](TargetingCondition.md) | [**TargetingCondition**](TargetingCondition.md) | [**TargetingCondition**](TargetingCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

