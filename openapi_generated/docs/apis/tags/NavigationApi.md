<a name="__pageTop"></a>
# openapi_client.apis.tags.navigation_api.NavigationApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**load_json1**](#load_json1) | **get** /v1/nav/{uri} | 

# **load_json1**
<a name="load_json1"></a>
> load_json1(uri)



### Example

```python
import openapi_client
from openapi_client.apis.tags import navigation_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = navigation_api.NavigationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.load_json1(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NavigationApi->load_json1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
        'depth': "depth_example",
        'languageId': "languageId_example",
    }
    try:
        api_response = api_instance.load_json1(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NavigationApi->load_json1: %s\n" % e)
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
depth | DepthSchema | | optional
languageId | LanguageIdSchema | | optional


# DepthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uri | UriSchema | | 

# UriSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#load_json1.ApiResponseForDefault) | default response

#### load_json1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

