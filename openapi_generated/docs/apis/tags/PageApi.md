<a name="__pageTop"></a>
# dotcms_rest_client.dotcms_rest_client.tags.page_api.PageApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_content**](#add_content) | **post** /v1/page/{pageId}/content | 
[**copy_content**](#copy_content) | **put** /v1/page/copyContent | 
[**deep_copy_page**](#deep_copy_page) | **put** /v1/page/{pageId}/_deepcopy | 
[**get_content_tree**](#get_content_tree) | **get** /v1/page/{pageId}/content/tree | 
[**get_html_versions_page**](#get_html_versions_page) | **get** /v1/page/{pageId}/render/versions | 
[**get_personalized_personas_on_page**](#get_personalized_personas_on_page) | **get** /v1/page/{pageId}/personas | 
[**load_json2**](#load_json2) | **get** /v1/page/json/{uri} | 
[**render**](#render) | **get** /v1/page/render/{uri} | 
[**render_html_only**](#render_html_only) | **get** /v1/page/renderHTML/{uri} | 
[**save_layout**](#save_layout) | **post** /v1/page/layout | 
[**save_layout1**](#save_layout1) | **post** /v1/page/{pageId}/layout | 
[**search_page**](#search_page) | **get** /v1/page/search | 

# **add_content**
<a name="add_content"></a>
> add_content(page_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from dotcms_rest_client.model.page_container_form import PageContainerForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pageId': "pageId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.add_content(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->add_content: %s\n" % e)

    # example passing only optional values
    path_params = {
        'pageId': "pageId_example",
    }
    query_params = {
        'variantName': "variantName_example",
    }
    body = PageContainerForm(
        request_json="request_json_example",
        container_entries=[
            ContainerEntry(
                persona_tag="persona_tag_example",
                content_ids=[
                    "content_ids_example"
                ],
                container_id="container_id_example",
                container_uuid="container_uuid_example",
            )
        ],
    )
    try:
        api_response = api_instance.add_content(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->add_content: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageContainerForm**](../../models/PageContainerForm.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
variantName | VariantNameSchema | | optional


# VariantNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageId | PageIdSchema | | 

# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#add_content.ApiResponseForDefault) | default response

#### add_content.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **copy_content**
<a name="copy_content"></a>
> ResponseEntityViewMapStringObject copy_content()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from dotcms_rest_client.model.copy_contentlet_form import CopyContentletForm
from dotcms_rest_client.model.response_entity_view_map_string_object import ResponseEntityViewMapStringObject
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only optional values
    body = CopyContentletForm(
        content_id="content_id_example",
        page_id="page_id_example",
        container_id="container_id_example",
        relation_type="relation_type_example",
        personalization="personalization_example",
        variant_id="variant_id_example",
        tree_order=1,
    )
    try:
        api_response = api_instance.copy_content(
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->copy_content: %s\n" % e)
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
[**CopyContentletForm**](../../models/CopyContentletForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#copy_content.ApiResponseForDefault) | default response

#### copy_content.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityViewMapStringObject**](../../models/ResponseEntityViewMapStringObject.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **deep_copy_page**
<a name="deep_copy_page"></a>
> ResponseEntityViewMapStringObject deep_copy_page(page_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from dotcms_rest_client.model.response_entity_view_map_string_object import ResponseEntityViewMapStringObject
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pageId': "pageId_example",
    }
    try:
        api_response = api_instance.deep_copy_page(
            path_params=path_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->deep_copy_page: %s\n" % e)
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
pageId | PageIdSchema | | 

# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#deep_copy_page.ApiResponseForDefault) | default response

#### deep_copy_page.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityViewMapStringObject**](../../models/ResponseEntityViewMapStringObject.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_content_tree**
<a name="get_content_tree"></a>
> ResponseEntityViewListMulitreeView get_content_tree(page_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from dotcms_rest_client.model.response_entity_view_list_mulitree_view import ResponseEntityViewListMulitreeView
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pageId': "pageId_example",
    }
    try:
        api_response = api_instance.get_content_tree(
            path_params=path_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->get_content_tree: %s\n" % e)
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
pageId | PageIdSchema | | 

# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_content_tree.ApiResponseForDefault) | default response

#### get_content_tree.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, SchemaFor0ResponseBodyApplicationJavascript, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityViewListMulitreeView**](../../models/ResponseEntityViewListMulitreeView.md) |  | 


# SchemaFor0ResponseBodyApplicationJavascript
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityViewListMulitreeView**](../../models/ResponseEntityViewListMulitreeView.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_html_versions_page**
<a name="get_html_versions_page"></a>
> get_html_versions_page(page_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pageId': "pageId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_html_versions_page(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->get_html_versions_page: %s\n" % e)

    # example passing only optional values
    path_params = {
        'pageId': "pageId_example",
    }
    query_params = {
        'langId': "langId_example",
    }
    try:
        api_response = api_instance.get_html_versions_page(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->get_html_versions_page: %s\n" % e)
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
langId | LangIdSchema | | optional


# LangIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageId | PageIdSchema | | 

# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_html_versions_page.ApiResponseForDefault) | default response

#### get_html_versions_page.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_personalized_personas_on_page**
<a name="get_personalized_personas_on_page"></a>
> get_personalized_personas_on_page(page_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pageId': "pageId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_personalized_personas_on_page(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->get_personalized_personas_on_page: %s\n" % e)

    # example passing only optional values
    path_params = {
        'pageId': "pageId_example",
    }
    query_params = {
        'filter': "filter_example",
        'page': 1,
        'per_page': 1,
        'orderby': "title",
        'direction': "ASC",
        'hostId': "hostId_example",
        'respectFrontEndRoles': True,
    }
    try:
        api_response = api_instance.get_personalized_personas_on_page(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->get_personalized_personas_on_page: %s\n" % e)
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
filter | FilterSchema | | optional
page | PageSchema | | optional
per_page | PerPageSchema | | optional
orderby | OrderbySchema | | optional
direction | DirectionSchema | | optional
hostId | HostIdSchema | | optional
respectFrontEndRoles | RespectFrontEndRolesSchema | | optional


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
str,  | str,  |  | if omitted the server will use the default value of "title"

# DirectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "ASC"

# HostIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RespectFrontEndRolesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageId | PageIdSchema | | 

# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_personalized_personas_on_page.ApiResponseForDefault) | default response

#### get_personalized_personas_on_page.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **load_json2**
<a name="load_json2"></a>
> load_json2(uri)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.load_json2(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->load_json2: %s\n" % e)

    # example passing only optional values
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
        'mode': "mode_example",
        'com.dotmarketing.persona.id': "com.dotmarketing.persona.id_example",
        'language_id': "language_id_example",
        'device_inode': "device_inode_example",
    }
    try:
        api_response = api_instance.load_json2(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->load_json2: %s\n" % e)
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
mode | ModeSchema | | optional
com.dotmarketing.persona.id | ComDotmarketingPersonaIdSchema | | optional
language_id | LanguageIdSchema | | optional
device_inode | DeviceInodeSchema | | optional


# ModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ComDotmarketingPersonaIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeviceInodeSchema

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
default | [ApiResponseForDefault](#load_json2.ApiResponseForDefault) | default response

#### load_json2.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **render**
<a name="render"></a>
> render(uri)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.render(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->render: %s\n" % e)

    # example passing only optional values
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
        'mode': "mode_example",
        'com.dotmarketing.persona.id': "com.dotmarketing.persona.id_example",
        'language_id': "language_id_example",
        'device_inode': "device_inode_example",
    }
    try:
        api_response = api_instance.render(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->render: %s\n" % e)
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
mode | ModeSchema | | optional
com.dotmarketing.persona.id | ComDotmarketingPersonaIdSchema | | optional
language_id | LanguageIdSchema | | optional
device_inode | DeviceInodeSchema | | optional


# ModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ComDotmarketingPersonaIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeviceInodeSchema

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
default | [ApiResponseForDefault](#render.ApiResponseForDefault) | default response

#### render.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **render_html_only**
<a name="render_html_only"></a>
> render_html_only(uri)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.render_html_only(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->render_html_only: %s\n" % e)

    # example passing only optional values
    path_params = {
        'uri': "uri_example",
    }
    query_params = {
        'mode': "LIVE_ADMIN",
    }
    try:
        api_response = api_instance.render_html_only(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->render_html_only: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/html', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
mode | ModeSchema | | optional


# ModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "LIVE_ADMIN"

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
default | [ApiResponseForDefault](#render_html_only.ApiResponseForDefault) | default response

#### render_html_only.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_layout**
<a name="save_layout"></a>
> save_layout()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from dotcms_rest_client.model.page_form import PageForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only optional values
    body = PageForm(
        theme_id="theme_id_example",
        title="title_example",
        host_id="host_id_example",
        layout=TemplateLayout(
            width="width_example",
            title="title_example",
            header=True,
            footer=True,
            body=Body(
                rows=[
                    TemplateLayoutRow(
                        columns=[
                            TemplateLayoutColumn(
                                containers=[
                                    ContainerUUID(
                                        identifier="identifier_example",
                                        uuid="uuid_example",
                                    )
                                ],
                                width_percent=1,
                                left_offset=1,
                                style_class="style_class_example",
                                preview=True,
                                width=1,
                                left=1,
                            )
                        ],
                        style_class="style_class_example",
                    )
                ],
            ),
            sidebar=Sidebar(
,
                location="location_example",
                width="width_example",
                width_percent=1,
                preview=True,
            ),
            body_rows=[
                TemplateLayoutRow()
            ],
        ),
        anonymous_layout=True,
    )
    try:
        api_response = api_instance.save_layout(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->save_layout: %s\n" % e)
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
[**PageForm**](../../models/PageForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_layout.ApiResponseForDefault) | default response

#### save_layout.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_layout1**
<a name="save_layout1"></a>
> save_layout1(page_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from dotcms_rest_client.model.page_form import PageForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pageId': "pageId_example",
    }
    try:
        api_response = api_instance.save_layout1(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->save_layout1: %s\n" % e)

    # example passing only optional values
    path_params = {
        'pageId': "pageId_example",
    }
    body = PageForm(
        theme_id="theme_id_example",
        title="title_example",
        host_id="host_id_example",
        layout=TemplateLayout(
            width="width_example",
            title="title_example",
            header=True,
            footer=True,
            body=Body(
                rows=[
                    TemplateLayoutRow(
                        columns=[
                            TemplateLayoutColumn(
                                containers=[
                                    ContainerUUID(
                                        identifier="identifier_example",
                                        uuid="uuid_example",
                                    )
                                ],
                                width_percent=1,
                                left_offset=1,
                                style_class="style_class_example",
                                preview=True,
                                width=1,
                                left=1,
                            )
                        ],
                        style_class="style_class_example",
                    )
                ],
            ),
            sidebar=Sidebar(
,
                location="location_example",
                width="width_example",
                width_percent=1,
                preview=True,
            ),
            body_rows=[
                TemplateLayoutRow()
            ],
        ),
        anonymous_layout=True,
    )
    try:
        api_response = api_instance.save_layout1(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->save_layout1: %s\n" % e)
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
[**PageForm**](../../models/PageForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pageId | PageIdSchema | | 

# PageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_layout1.ApiResponseForDefault) | default response

#### save_layout1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_page**
<a name="search_page"></a>
> search_page()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.dotcms_rest_client.tags import page_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = page_api.PageApi(api_client)

    # example passing only optional values
    query_params = {
        'path': "path_example",
        'live': True,
        'onlyLiveSites': True,
    }
    try:
        api_response = api_instance.search_page(
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling PageApi->search_page: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/html', 'application/javascript', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path | PathSchema | | optional
live | LiveSchema | | optional
onlyLiveSites | OnlyLiveSitesSchema | | optional


# PathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# OnlyLiveSitesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#search_page.ApiResponseForDefault) | default response

#### search_page.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

