<a name="__pageTop"></a>
# dotcms_rest_client.dotcms_rest_client.tags.content_type_api.ContentTypeApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_type**](#copy_type) | **post** /v1/contenttype/{baseVariableName}/_copy | 
[**create_type**](#create_type) | **post** /v1/contenttype | 
[**delete_type**](#delete_type) | **delete** /v1/contenttype/id/{idOrVar} | 
[**filtered_content_types**](#filtered_content_types) | **post** /v1/contenttype/_filter | 
[**get_content_types**](#get_content_types) | **get** /v1/contenttype | 
[**get_recent_base_types**](#get_recent_base_types) | **get** /v1/contenttype/basetypes | 
[**get_type**](#get_type) | **get** /v1/contenttype/id/{idOrVar} | 
[**update_type**](#update_type) | **put** /v1/contenttype/id/{idOrVar} | 

# **copy_type**
<a name="copy_type"></a>
> copy_type(base_variable_name)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from dotcms_rest_client.model.copy_content_type_form import CopyContentTypeForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'baseVariableName': "baseVariableName_example",
    }
    try:
        api_response = api_instance.copy_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->copy_type: %s\n" % e)

    # example passing only optional values
    path_params = {
        'baseVariableName': "baseVariableName_example",
    }
    body = CopyContentTypeForm(
        name="name_example",
        variable="variable_example",
        folder="folder_example",
        host="host_example",
        icon="icon_example",
    )
    try:
        api_response = api_instance.copy_type(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->copy_type: %s\n" % e)
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
[**CopyContentTypeForm**](../../models/CopyContentTypeForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
baseVariableName | BaseVariableNameSchema | | 

# BaseVariableNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#copy_type.ApiResponseForDefault) | default response

#### copy_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_type**
<a name="create_type"></a>
> create_type()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from dotcms_rest_client.model.content_type_form import ContentTypeForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only optional values
    body = ContentTypeForm(
        request_json=dict(),
        content_type=ContentType(),
        iterable=dict(),
        system_actions=[
            Tuple2SystemActionString(
                _1="NEW",
                _2="_2_example",
            )
        ],
        workflows_ids=[
            "workflows_ids_example"
        ],
    )
    try:
        api_response = api_instance.create_type(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->create_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContentTypeForm**](../../models/ContentTypeForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#create_type.ApiResponseForDefault) | default response

#### create_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_type**
<a name="delete_type"></a>
> delete_type(id_or_var)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idOrVar': "idOrVar_example",
    }
    try:
        api_response = api_instance.delete_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->delete_type: %s\n" % e)
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
idOrVar | IdOrVarSchema | | 

# IdOrVarSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_type.ApiResponseForDefault) | default response

#### delete_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **filtered_content_types**
<a name="filtered_content_types"></a>
> filtered_content_types()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from dotcms_rest_client.model.filtered_content_types_form import FilteredContentTypesForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only optional values
    body = FilteredContentTypesForm(
        filter=dict(
            "key": dict(),
        ),
        page=1,
        per_page=1,
        order_by="order_by_example",
        direction="direction_example",
    )
    try:
        api_response = api_instance.filtered_content_types(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->filtered_content_types: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FilteredContentTypesForm**](../../models/FilteredContentTypesForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#filtered_content_types.ApiResponseForDefault) | default response

#### filtered_content_types.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_content_types**
<a name="get_content_types"></a>
> get_content_types()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
        'page': 1,
        'per_page': 1,
        'orderby': "upper(name)",
        'direction': "ASC",
        'type': "type_example",
        'host': "host_example",
    }
    try:
        api_response = api_instance.get_content_types(
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->get_content_types: %s\n" % e)
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
filter | FilterSchema | | optional
page | PageSchema | | optional
per_page | PerPageSchema | | optional
orderby | OrderbySchema | | optional
direction | DirectionSchema | | optional
type | TypeSchema | | optional
host | HostSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OrderbySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "upper(name)"

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "ASC"

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HostSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_content_types.ApiResponseForDefault) | default response

#### get_content_types.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_recent_base_types**
<a name="get_recent_base_types"></a>
> get_recent_base_types()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_recent_base_types()
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->get_recent_base_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_recent_base_types.ApiResponseForDefault) | default response

#### get_recent_base_types.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_type**
<a name="get_type"></a>
> get_type(id_or_var)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idOrVar': "idOrVar_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_type(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->get_type: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idOrVar': "idOrVar_example",
    }
    query_params = {
        'languageId': 1,
        'live': True,
    }
    try:
        api_response = api_instance.get_type(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->get_type: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
languageId | LanguageIdSchema | | optional
live | LiveSchema | | optional


# LanguageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# LiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idOrVar | IdOrVarSchema | | 

# IdOrVarSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_type.ApiResponseForDefault) | default response

#### get_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_type**
<a name="update_type"></a>
> update_type(id_or_var)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import content_type_api
from dotcms_rest_client.model.content_type_form import ContentTypeForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = content_type_api.ContentTypeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'idOrVar': "idOrVar_example",
    }
    try:
        api_response = api_instance.update_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->update_type: %s\n" % e)

    # example passing only optional values
    path_params = {
        'idOrVar': "idOrVar_example",
    }
    body = ContentTypeForm(
        request_json=dict(),
        content_type=ContentType(),
        iterable=dict(),
        system_actions=[
            Tuple2SystemActionString(
                _1="NEW",
                _2="_2_example",
            )
        ],
        workflows_ids=[
            "workflows_ids_example"
        ],
    )
    try:
        api_response = api_instance.update_type(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling ContentTypeApi->update_type: %s\n" % e)
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
[**ContentTypeForm**](../../models/ContentTypeForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
idOrVar | IdOrVarSchema | | 

# IdOrVarSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#update_type.ApiResponseForDefault) | default response

#### update_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

