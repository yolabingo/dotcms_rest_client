<a name="__pageTop"></a>
# dotcms_rest_client.apis.tags.tail_log_api.TailLogApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logs**](#get_logs) | **get** /v1/logs/{fileName}/_tail | 

# **get_logs**
<a name="get_logs"></a>
> EventOutput get_logs(file_name)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import tail_log_api
from dotcms_rest_client.model.event_output import EventOutput
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tail_log_api.TailLogApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'fileName': "fileName_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling TailLogApi->get_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'fileName': "fileName_example",
    }
    query_params = {
        'linesBack': 1,
    }
    try:
        api_response = api_instance.get_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling TailLogApi->get_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/event-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
linesBack | LinesBackSchema | | optional


# LinesBackSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fileName | FileNameSchema | | 

# FileNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_logs.ApiResponseForDefault) | default response

#### get_logs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextEventStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextEventStream
Type | Description  | Notes
------------- | ------------- | -------------
[**EventOutput**](../../models/EventOutput.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

