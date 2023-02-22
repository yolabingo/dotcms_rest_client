<a name="__pageTop"></a>
# dotcms_rest_client.dotcms_rest_client.tags.content_delivery_api.ContentDeliveryApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**can_lock_content**](#can_lock_content) | **put** /content/canLock/{params} | 
[**get_content**](#get_content) | **get** /content/{params} | 
[**index_count**](#index_count) | **get** /content/indexcount/{query} | 
[**index_search**](#index_search) | **get** /content/indexsearch/{query}/sortby/{sortby}/limit/{limit}/offset/{offset} | 
[**lock_content**](#lock_content) | **put** /content/lock/{params} | 
[**search**](#search) | **post** /content/_search | 
[**single_post**](#single_post) | **post** /content/{params} | 
[**single_put**](#single_put) | **put** /content/{params} | 
[**unlock_content**](#unlock_content) | **put** /content/unlock/{params} | 

# **can_lock_content**
<a name="can_lock_content"></a>
> can_lock_content(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.can_lock_content(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->can_lock_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params | ParamsSchema | | 

# ParamsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#can_lock_content.ApiResponseForDefault) | default response

#### can_lock_content.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_content**
<a name="get_content"></a>
> get_content(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.get_content(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->get_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params | ParamsSchema | | 

# ParamsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_content.ApiResponseForDefault) | default response

#### get_content.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **index_count**
<a name="index_count"></a>
> index_count(querytypeparam_callback)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'query': "query_example",
        'type': "type_example",
        'callback': "callback_example",
    }
    try:
        api_response = api_instance.index_count(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->index_count: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | 
type | TypeSchema | | 
callback | CallbackSchema | | 

# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CallbackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#index_count.ApiResponseForDefault) | default response

#### index_count.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **index_search**
<a name="index_search"></a>
> index_search(querysortbylimitoffsettypeparam_callback)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'query': "query_example",
        'sortby': "sortby_example",
        'limit': 1,
        'offset': 1,
        'type': "type_example",
        'callback': "callback_example",
    }
    try:
        api_response = api_instance.index_search(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->index_search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | 
sortby | SortbySchema | | 
limit | LimitSchema | | 
offset | OffsetSchema | | 
type | TypeSchema | | 
callback | CallbackSchema | | 

# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortbySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CallbackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#index_search.ApiResponseForDefault) | default response

#### index_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **lock_content**
<a name="lock_content"></a>
> lock_content(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.lock_content(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->lock_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params | ParamsSchema | | 

# ParamsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#lock_content.ApiResponseForDefault) | default response

#### lock_content.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search**
<a name="search"></a>
> search()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from dotcms_rest_client.model.search_form import SearchForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only optional values
    body = SearchForm(
        query="query_example",
        sort="sort_example",
        limit=1,
        offset=1,
        user_id="user_id_example",
        render="render_example",
        depth=1,
        language_id=1,
        all_categories_info=True,
    )
    try:
        api_response = api_instance.search(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchForm**](../../models/SearchForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#search.ApiResponseForDefault) | default response

#### search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **single_post**
<a name="single_post"></a>
> single_post(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.single_post(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->single_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params | ParamsSchema | | 

# ParamsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#single_post.ApiResponseForDefault) | default response

#### single_post.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **single_put**
<a name="single_put"></a>
> single_put(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.single_put(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->single_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params | ParamsSchema | | 

# ParamsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#single_put.ApiResponseForDefault) | default response

#### single_put.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **unlock_content**
<a name="unlock_content"></a>
> unlock_content(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_delivery_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_delivery_api.ContentDeliveryApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.unlock_content(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentDeliveryApi->unlock_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params | ParamsSchema | | 

# ParamsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#unlock_content.ApiResponseForDefault) | default response

#### unlock_content.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

