<a name="__pageTop"></a>
# openapi_client.apis.tags.experiment_api.ExperimentApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_variant**](#add_variant) | **post** /v1/experiments/{experimentId}/variants | 
[**archive1**](#archive1) | **put** /v1/experiments/{experimentId}/_archive | 
[**create**](#create) | **post** /v1/experiments | 
[**delete4**](#delete4) | **delete** /v1/experiments/{experimentId} | 
[**delete_goal**](#delete_goal) | **delete** /v1/experiments/{experimentId}/goals/primary | 
[**delete_targeting_condition**](#delete_targeting_condition) | **delete** /v1/experiments/{experimentId}/targetingConditions/{id} | 
[**delete_variant**](#delete_variant) | **delete** /v1/experiments/{experimentId}/variants/{name} | 
[**end**](#end) | **post** /v1/experiments/{experimentId}/_end | 
[**get1**](#get1) | **get** /v1/experiments/{id} | 
[**is_user_included**](#is_user_included) | **post** /v1/experiments/isUserIncluded | 
[**list1**](#list1) | **get** /v1/experiments | 
[**start**](#start) | **post** /v1/experiments/{experimentId}/_start | 
[**update1**](#update1) | **patch** /v1/experiments/{experimentId} | 

# **add_variant**
<a name="add_variant"></a>
> ResponseEntitySingleExperimentView add_variant(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.add_variant_form import AddVariantForm
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.add_variant(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->add_variant: %s\n" % e)

    # example passing only optional values
    path_params = {
        'experimentId': "experimentId_example",
    }
    body = AddVariantForm(
        name="name_example",
    )
    try:
        api_response = api_instance.add_variant(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->add_variant: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddVariantForm**](../../models/AddVariantForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#add_variant.ApiResponseForDefault) | default response

#### add_variant.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **archive1**
<a name="archive1"></a>
> ResponseEntityExperimentView archive1(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_experiment_view import ResponseEntityExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.archive1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->archive1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#archive1.ApiResponseForDefault) | default response

#### archive1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityExperimentView**](../../models/ResponseEntityExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityExperimentView**](../../models/ResponseEntityExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create**
<a name="create"></a>
> ResponseEntitySingleExperimentView create()



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.experiment_form import ExperimentForm
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only optional values
    body = ExperimentForm(
        name="name_example",
        description="description_example",
        page_id="page_id_example",
        traffic_allocation=3.14,
        traffic_proportion=TrafficProportion(
            type="SPLIT_EVENLY",
            variants=[
                ExperimentVariant(
                    id="id_example",
                    name="name_example",
                    weight=3.14,
                    url="url_example",
                )
            ],
        ),
        scheduling=Scheduling(
            start_date="1970-01-01T00:00:00.00Z",
            end_date="1970-01-01T00:00:00.00Z",
        ),
        goals=Goals(
            primary=Metric(
                name="name_example",
                type="REACH_PAGE",
                conditions=[
                    Condition(
                        parameter="parameter_example",
                        operator="EQUALS",
                        value="value_example",
                    )
                ],
            ),
        ),
        targeting_conditions=[
            TargetingCondition(
                id="id_example",
                condition_key="condition_key_example",
                values=dict(
                    empty=True,
                ),
                operator="AND",
            )
        ],
        lookback_window=1,
    )
    try:
        api_response = api_instance.create(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ExperimentForm**](../../models/ExperimentForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#create.ApiResponseForDefault) | default response

#### create.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete4**
<a name="delete4"></a>
> ResponseEntityViewString delete4(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_view_string import ResponseEntityViewString
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.delete4(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->delete4: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete4.ApiResponseForDefault) | default response

#### delete4.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityViewString**](../../models/ResponseEntityViewString.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityViewString**](../../models/ResponseEntityViewString.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_goal**
<a name="delete_goal"></a>
> ResponseEntitySingleExperimentView delete_goal(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.delete_goal(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->delete_goal: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_goal.ApiResponseForDefault) | default response

#### delete_goal.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_targeting_condition**
<a name="delete_targeting_condition"></a>
> ResponseEntitySingleExperimentView delete_targeting_condition(experiment_idid)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
        'id': "id_example",
    }
    try:
        api_response = api_instance.delete_targeting_condition(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->delete_targeting_condition: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 
id | IdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_targeting_condition.ApiResponseForDefault) | default response

#### delete_targeting_condition.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_variant**
<a name="delete_variant"></a>
> ResponseEntitySingleExperimentView delete_variant(experiment_idname)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
        'name': "name_example",
    }
    try:
        api_response = api_instance.delete_variant(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->delete_variant: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 
name | NameSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_variant.ApiResponseForDefault) | default response

#### delete_variant.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **end**
<a name="end"></a>
> ResponseEntitySingleExperimentView end(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.end(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->end: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#end.ApiResponseForDefault) | default response

#### end.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get1**
<a name="get1"></a>
> ResponseEntitySingleExperimentView get1(id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        api_response = api_instance.get1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->get1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get1.ApiResponseForDefault) | default response

#### get1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **is_user_included**
<a name="is_user_included"></a>
> ResponseEntityExperimentSelectedView is_user_included()



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_experiment_selected_view import ResponseEntityExperimentSelectedView
from openapi_client.model.excluded_experiment_list_form import ExcludedExperimentListForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only optional values
    body = ExcludedExperimentListForm(
        exclude=[
            "exclude_example"
        ],
    )
    try:
        api_response = api_instance.is_user_included(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->is_user_included: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExcludedExperimentListForm**](../../models/ExcludedExperimentListForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#is_user_included.ApiResponseForDefault) | default response

#### is_user_included.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityExperimentSelectedView**](../../models/ResponseEntityExperimentSelectedView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list1**
<a name="list1"></a>
> ResponseEntityExperimentView list1()



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_experiment_view import ResponseEntityExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only optional values
    query_params = {
        'pageId': "pageId_example",
        'name': "name_example",
        'status': [
        "RUNNING"
    ],
    }
    try:
        api_response = api_instance.list1(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->list1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageId | PageIdSchema | | optional
name | NameSchema | | optional
status | StatusSchema | | optional


# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["RUNNING", "SCHEDULED", "ENDED", "DRAFT", "ARCHIVED", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#list1.ApiResponseForDefault) | default response

#### list1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityExperimentView**](../../models/ResponseEntityExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityExperimentView**](../../models/ResponseEntityExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **start**
<a name="start"></a>
> ResponseEntitySingleExperimentView start(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.start(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->start: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#start.ApiResponseForDefault) | default response

#### start.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update1**
<a name="update1"></a>
> ResponseEntitySingleExperimentView update1(experiment_id)



### Example

```python
import openapi_client
from openapi_client.apis.tags import experiment_api
from openapi_client.model.experiment_form import ExperimentForm
from openapi_client.model.response_entity_single_experiment_view import ResponseEntitySingleExperimentView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = experiment_api.ExperimentApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'experimentId': "experimentId_example",
    }
    try:
        api_response = api_instance.update1(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->update1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'experimentId': "experimentId_example",
    }
    body = ExperimentForm(
        name="name_example",
        description="description_example",
        page_id="page_id_example",
        traffic_allocation=3.14,
        traffic_proportion=TrafficProportion(
            type="SPLIT_EVENLY",
            variants=[
                ExperimentVariant(
                    id="id_example",
                    name="name_example",
                    weight=3.14,
                    url="url_example",
                )
            ],
        ),
        scheduling=Scheduling(
            start_date="1970-01-01T00:00:00.00Z",
            end_date="1970-01-01T00:00:00.00Z",
        ),
        goals=Goals(
            primary=Metric(
                name="name_example",
                type="REACH_PAGE",
                conditions=[
                    Condition(
                        parameter="parameter_example",
                        operator="EQUALS",
                        value="value_example",
                    )
                ],
            ),
        ),
        targeting_conditions=[
            TargetingCondition(
                id="id_example",
                condition_key="condition_key_example",
                values=dict(
                    empty=True,
                ),
                operator="AND",
            )
        ],
        lookback_window=1,
    )
    try:
        api_response = api_instance.update1(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExperimentApi->update1: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ExperimentForm**](../../models/ExperimentForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experimentId | ExperimentIdSchema | | 

# ExperimentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#update1.ApiResponseForDefault) | default response

#### update1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntitySingleExperimentView**](../../models/ResponseEntitySingleExperimentView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

