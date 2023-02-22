<a name="__pageTop"></a>
# dotcms_rest_client.dotcms_rest_client.tags.bundle_api.BundleApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all**](#delete_all) | **delete** /bundle/all | 
[**delete_all_fail**](#delete_all_fail) | **delete** /bundle/all/fail | 
[**delete_all_success**](#delete_all_success) | **delete** /bundle/all/success | 
[**delete_bundles_by_identifiers**](#delete_bundles_by_identifiers) | **delete** /bundle/ids | 
[**delete_bundles_older_than**](#delete_bundles_older_than) | **delete** /bundle/olderthan/{olderThan} | 
[**delete_environment_push_history**](#delete_environment_push_history) | **get** /bundle/deleteenvironmentpushhistory/{params} | 
[**delete_push_history**](#delete_push_history) | **get** /bundle/deletepushhistory/{params} | 
[**download_bundle**](#download_bundle) | **get** /bundle/_download/{bundleId} | 
[**download_manifest**](#download_manifest) | **get** /bundle/{bundleId}/manifest | 
[**generate_bundle**](#generate_bundle) | **post** /bundle/_generate | 
[**get_publish_queue_elements**](#get_publish_queue_elements) | **get** /bundle/{bundleId}/assets | 
[**get_unsend_bundles**](#get_unsend_bundles) | **get** /bundle/getunsendbundles/{params} | 
[**update_bundle**](#update_bundle) | **get** /bundle/updatebundle/{params} | 
[**upload_bundle_async**](#upload_bundle_async) | **post** /bundle | 
[**upload_bundle_sync**](#upload_bundle_sync) | **post** /bundle/sync | 

# **delete_all**
<a name="delete_all"></a>
> delete_all()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_all()
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_all: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_all.ApiResponseForDefault) | default response

#### delete_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_all_fail**
<a name="delete_all_fail"></a>
> delete_all_fail()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_all_fail()
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_all_fail: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_all_fail.ApiResponseForDefault) | default response

#### delete_all_fail.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_all_success**
<a name="delete_all_success"></a>
> delete_all_success()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.delete_all_success()
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_all_success: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_all_success.ApiResponseForDefault) | default response

#### delete_all_success.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_bundles_by_identifiers**
<a name="delete_bundles_by_identifiers"></a>
> delete_bundles_by_identifiers()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from dotcms_rest_client.model.delete_bundles_by_identifier_form import DeleteBundlesByIdentifierForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only optional values
    body = DeleteBundlesByIdentifierForm(
        identifiers=[
            "identifiers_example"
        ],
    )
    try:
        api_response = api_instance.delete_bundles_by_identifiers(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_bundles_by_identifiers: %s\n" % e)
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
[**DeleteBundlesByIdentifierForm**](../../models/DeleteBundlesByIdentifierForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_bundles_by_identifiers.ApiResponseForDefault) | default response

#### delete_bundles_by_identifiers.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_bundles_older_than**
<a name="delete_bundles_older_than"></a>
> delete_bundles_older_than(older_than)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'olderThan': "1970-01-01T00:00:00.00Z",
    }
    try:
        api_response = api_instance.delete_bundles_older_than(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_bundles_older_than: %s\n" % e)
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
olderThan | OlderThanSchema | | 

# OlderThanSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_bundles_older_than.ApiResponseForDefault) | default response

#### delete_bundles_older_than.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_environment_push_history**
<a name="delete_environment_push_history"></a>
> delete_environment_push_history(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.delete_environment_push_history(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_environment_push_history: %s\n" % e)
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
default | [ApiResponseForDefault](#delete_environment_push_history.ApiResponseForDefault) | default response

#### delete_environment_push_history.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_push_history**
<a name="delete_push_history"></a>
> delete_push_history(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.delete_push_history(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->delete_push_history: %s\n" % e)
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
default | [ApiResponseForDefault](#delete_push_history.ApiResponseForDefault) | default response

#### delete_push_history.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_bundle**
<a name="download_bundle"></a>
> download_bundle(bundle_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
    }
    try:
        api_response = api_instance.download_bundle(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->download_bundle: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bundleId | BundleIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#download_bundle.ApiResponseForDefault) | default response

#### download_bundle.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **download_manifest**
<a name="download_manifest"></a>
> download_manifest(bundle_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
    }
    try:
        api_response = api_instance.download_manifest(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->download_manifest: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bundleId | BundleIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#download_manifest.ApiResponseForDefault) | default response

#### download_manifest.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **generate_bundle**
<a name="generate_bundle"></a>
> generate_bundle()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from dotcms_rest_client.model.generate_bundle_form import GenerateBundleForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only optional values
    body = GenerateBundleForm(
        bundle_id="bundle_id_example",
        operation="PUBLISH",
        filter_key="filter_key_example",
    )
    try:
        api_response = api_instance.generate_bundle(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->generate_bundle: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GenerateBundleForm**](../../models/GenerateBundleForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#generate_bundle.ApiResponseForDefault) | default response

#### generate_bundle.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_publish_queue_elements**
<a name="get_publish_queue_elements"></a>
> get_publish_queue_elements(bundle_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_publish_queue_elements(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->get_publish_queue_elements: %s\n" % e)

    # example passing only optional values
    path_params = {
        'bundleId': "bundleId_example",
    }
    query_params = {
        'limit': 1,
    }
    try:
        api_response = api_instance.get_publish_queue_elements(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->get_publish_queue_elements: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bundleId | BundleIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_publish_queue_elements.ApiResponseForDefault) | default response

#### get_publish_queue_elements.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_unsend_bundles**
<a name="get_unsend_bundles"></a>
> get_unsend_bundles(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.get_unsend_bundles(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->get_unsend_bundles: %s\n" % e)
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
default | [ApiResponseForDefault](#get_unsend_bundles.ApiResponseForDefault) | default response

#### get_unsend_bundles.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_bundle**
<a name="update_bundle"></a>
> update_bundle(params)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'params': "params_example",
    }
    try:
        api_response = api_instance.update_bundle(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->update_bundle: %s\n" % e)
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
default | [ApiResponseForDefault](#update_bundle.ApiResponseForDefault) | default response

#### update_bundle.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_bundle_async**
<a name="upload_bundle_async"></a>
> upload_bundle_async()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from dotcms_rest_client.model.form_data_multi_part import FormDataMultiPart
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only optional values
    body = dict(
        content_disposition=ContentDisposition(
            type="type_example",
            parameters=dict(
                "key": "key_example",
            ),
            file_name="file_name_example",
            creation_date="1970-01-01T00:00:00.00Z",
            modification_date="1970-01-01T00:00:00.00Z",
            read_date="1970-01-01T00:00:00.00Z",
            size=1,
        ),
        entity=dict(),
        headers=dict(
            "key": [
                "key_example"
            ],
        ),
        media_type=dict(
            type="type_example",
            subtype="subtype_example",
            parameters=dict(),
            wildcard_type=True,
            wildcard_subtype=True,
        ),
        message_body_workers=dict(),
        parent=MultiPart(
            content_disposition=ContentDisposition(),
            entity=dict(),
            headers=dict(),
            media_type=dict(),
            message_body_workers=dict(),
,
            providers=dict(),
            body_parts=[
                BodyPart(
                    content_disposition=ContentDisposition(),
                    entity=dict(),
                    headers=dict(),
                    media_type=dict(),
                    message_body_workers=dict(),
                    parent=MultiPart(),
                    providers=dict(),
                    parameterized_headers=dict(
                        "key": [
                            ParameterizedHeader(
                                value="value_example",
                                parameters=dict(),
                            )
                        ],
                    ),
                )
            ],
            parameterized_headers=dict(),
        ),
        providers=dict(),
,
        fields=dict(
            "key": [
                FormDataBodyPart(
                    content_disposition=ContentDisposition(),
                    entity=dict(),
                    headers=dict(),
                    media_type=dict(),
                    message_body_workers=dict(),
                    parent=MultiPart(),
                    providers=dict(),
                    simple=True,
                    form_data_content_disposition=FormDataContentDisposition(
                        type="type_example",
                        parameters=dict(),
                        file_name="file_name_example",
                        creation_date="1970-01-01T00:00:00.00Z",
                        modification_date="1970-01-01T00:00:00.00Z",
                        read_date="1970-01-01T00:00:00.00Z",
                        size=1,
                        name="name_example",
                    ),
                    name="name_example",
                    value="value_example",
                    parameterized_headers=dict(),
                )
            ],
        ),
        parameterized_headers=dict(),
    )
    try:
        api_response = api_instance.upload_bundle_async(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->upload_bundle_async: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**FormDataMultiPart**](../../models/FormDataMultiPart.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#upload_bundle_async.ApiResponseForDefault) | default response

#### upload_bundle_async.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **upload_bundle_sync**
<a name="upload_bundle_sync"></a>
> upload_bundle_sync()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import bundle_api
from dotcms_rest_client.model.form_data_multi_part import FormDataMultiPart
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundle_api.BundleApi(api_client)

    # example passing only optional values
    body = dict(
        content_disposition=ContentDisposition(
            type="type_example",
            parameters=dict(
                "key": "key_example",
            ),
            file_name="file_name_example",
            creation_date="1970-01-01T00:00:00.00Z",
            modification_date="1970-01-01T00:00:00.00Z",
            read_date="1970-01-01T00:00:00.00Z",
            size=1,
        ),
        entity=dict(),
        headers=dict(
            "key": [
                "key_example"
            ],
        ),
        media_type=dict(
            type="type_example",
            subtype="subtype_example",
            parameters=dict(),
            wildcard_type=True,
            wildcard_subtype=True,
        ),
        message_body_workers=dict(),
        parent=MultiPart(
            content_disposition=ContentDisposition(),
            entity=dict(),
            headers=dict(),
            media_type=dict(),
            message_body_workers=dict(),
,
            providers=dict(),
            body_parts=[
                BodyPart(
                    content_disposition=ContentDisposition(),
                    entity=dict(),
                    headers=dict(),
                    media_type=dict(),
                    message_body_workers=dict(),
                    parent=MultiPart(),
                    providers=dict(),
                    parameterized_headers=dict(
                        "key": [
                            ParameterizedHeader(
                                value="value_example",
                                parameters=dict(),
                            )
                        ],
                    ),
                )
            ],
            parameterized_headers=dict(),
        ),
        providers=dict(),
,
        fields=dict(
            "key": [
                FormDataBodyPart(
                    content_disposition=ContentDisposition(),
                    entity=dict(),
                    headers=dict(),
                    media_type=dict(),
                    message_body_workers=dict(),
                    parent=MultiPart(),
                    providers=dict(),
                    simple=True,
                    form_data_content_disposition=FormDataContentDisposition(
                        type="type_example",
                        parameters=dict(),
                        file_name="file_name_example",
                        creation_date="1970-01-01T00:00:00.00Z",
                        modification_date="1970-01-01T00:00:00.00Z",
                        read_date="1970-01-01T00:00:00.00Z",
                        size=1,
                        name="name_example",
                    ),
                    name="name_example",
                    value="value_example",
                    parameterized_headers=dict(),
                )
            ],
        ),
        parameterized_headers=dict(),
    )
    try:
        api_response = api_instance.upload_bundle_sync(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling BundleApi->upload_bundle_sync: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**FormDataMultiPart**](../../models/FormDataMultiPart.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#upload_bundle_sync.ApiResponseForDefault) | default response

#### upload_bundle_sync.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

