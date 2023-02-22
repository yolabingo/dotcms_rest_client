<a name="__pageTop"></a>
# dotcms_rest_client.apis.tags.workflow_api.WorkflowApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_step**](#add_step) | **post** /v1/workflow/steps | 
[**copy_scheme**](#copy_scheme) | **post** /v1/workflow/schemes/{schemeId}/copy | 
[**delete_action**](#delete_action) | **delete** /v1/workflow/actions/{actionId} | 
[**delete_action1**](#delete_action1) | **delete** /v1/workflow/steps/{stepId}/actions/{actionId} | 
[**delete_actionlet**](#delete_actionlet) | **delete** /v1/workflow/actionlets/{actionletId} | 
[**delete_scheme**](#delete_scheme) | **delete** /v1/workflow/schemes/{schemeId} | 
[**delete_step**](#delete_step) | **delete** /v1/workflow/steps/{stepId} | 
[**deletes_system_action**](#deletes_system_action) | **delete** /v1/workflow/system/actions/{identifier} | 
[**evaluate_action_condition**](#evaluate_action_condition) | **get** /v1/workflow/actions/{actionId}/condition | 
[**export_scheme**](#export_scheme) | **get** /v1/workflow/schemes/{schemeId}/export | 
[**find_action**](#find_action) | **get** /v1/workflow/actions/{actionId} | 
[**find_action_by_step**](#find_action_by_step) | **get** /v1/workflow/steps/{stepId}/actions/{actionId} | 
[**find_actionlets**](#find_actionlets) | **get** /v1/workflow/actionlets | 
[**find_actionlets_by_action**](#find_actionlets_by_action) | **get** /v1/workflow/actions/{actionId}/actionlets | 
[**find_actions_by_scheme**](#find_actions_by_scheme) | **get** /v1/workflow/schemes/{schemeId}/actions | 
[**find_actions_by_schemes_and_system_action**](#find_actions_by_schemes_and_system_action) | **post** /v1/workflow/schemes/actions/{systemAction} | 
[**find_actions_by_step**](#find_actions_by_step) | **get** /v1/workflow/steps/{stepId}/actions | 
[**find_all_schemes_and_schemes_by_content_type**](#find_all_schemes_and_schemes_by_content_type) | **get** /v1/workflow/schemes/schemescontenttypes/{contentTypeId} | 
[**find_available_actions**](#find_available_actions) | **get** /v1/workflow/contentlet/{inode}/actions | 
[**find_available_default_actions_by_content_type**](#find_available_default_actions_by_content_type) | **get** /v1/workflow/defaultactions/contenttype/{contentTypeId} | 
[**find_available_default_actions_by_schemes**](#find_available_default_actions_by_schemes) | **get** /v1/workflow/defaultactions/schemes | 
[**find_initial_available_actions_by_content_type**](#find_initial_available_actions_by_content_type) | **get** /v1/workflow/initialactions/contenttype/{contentTypeId} | 
[**find_schemes**](#find_schemes) | **get** /v1/workflow/schemes | 
[**find_step_by_id**](#find_step_by_id) | **get** /v1/workflow/steps/{stepId} | 
[**find_steps_by_scheme**](#find_steps_by_scheme) | **get** /v1/workflow/schemes/{schemeId}/steps | 
[**find_system_actions_by_content_type**](#find_system_actions_by_content_type) | **get** /v1/workflow/contenttypes/{contentTypeVarOrId}/system/actions | 
[**find_system_actions_by_scheme**](#find_system_actions_by_scheme) | **get** /v1/workflow/schemes/{schemeId}/system/actions | 
[**fire_action_by_name_single_part**](#fire_action_by_name_single_part) | **put** /v1/workflow/actions/fire | Fire action by name
[**fire_action_default_multipart_new_path**](#fire_action_default_multipart_new_path) | **put** /v1/workflow/actions/default/firemultipart/{systemAction} | Fire default action by name multipart
[**fire_action_default_single_part**](#fire_action_default_single_part) | **put** /v1/workflow/actions/default/fire/{systemAction} | Fire default action by name
[**fire_action_multipart_new_path**](#fire_action_multipart_new_path) | **put** /v1/workflow/actions/{actionId}/firemultipart | Fire action by ID multipart
[**fire_action_single_part**](#fire_action_single_part) | **put** /v1/workflow/actions/{actionId}/fire | Fire action by ID
[**fire_bulk_actions**](#fire_bulk_actions) | **post** /v1/workflow/contentlet/actions/_bulkfire | 
[**fire_bulk_actions1**](#fire_bulk_actions1) | **put** /v1/workflow/contentlet/actions/bulk/fire | 
[**fire_merge_action_default**](#fire_merge_action_default) | **patch** /v1/workflow/actions/default/fire/{systemAction} | 
[**fire_multiple_action_default**](#fire_multiple_action_default) | **post** /v1/workflow/actions/default/fire/{systemAction} | Fire default action by name on multiple contents
[**get_bulk_actions**](#get_bulk_actions) | **post** /v1/workflow/contentlet/actions/bulk | 
[**get_system_actions_referred_by_workflow_action**](#get_system_actions_referred_by_workflow_action) | **get** /v1/workflow/system/actions/{workflowActionId} | 
[**import_scheme**](#import_scheme) | **post** /v1/workflow/schemes/import | 
[**reorder_action**](#reorder_action) | **put** /v1/workflow/reorder/steps/{stepId}/actions/{actionId} | 
[**reorder_step**](#reorder_step) | **put** /v1/workflow/reorder/step/{stepId}/order/{order} | 
[**save_action**](#save_action) | **post** /v1/workflow/actions | 
[**save_action_to_step**](#save_action_to_step) | **post** /v1/workflow/steps/{stepId}/actions | 
[**save_actionlet_to_action**](#save_actionlet_to_action) | **post** /v1/workflow/actions/{actionId}/actionlets | 
[**save_scheme**](#save_scheme) | **post** /v1/workflow/schemes | 
[**save_system_action**](#save_system_action) | **put** /v1/workflow/system/actions | 
[**update_action**](#update_action) | **put** /v1/workflow/actions/{actionId} | 
[**update_scheme**](#update_scheme) | **put** /v1/workflow/schemes/{schemeId} | 
[**update_step**](#update_step) | **put** /v1/workflow/steps/{stepId} | 

# **add_step**
<a name="add_step"></a>
> add_step()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_step_add_form import WorkflowStepAddForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = WorkflowStepAddForm(
        scheme_id="scheme_id_example",
        step_name="step_name_example",
        enable_escalation=True,
        escalation_action="escalation_action_example",
        escalation_time="escalation_time_example",
        step_resolved=True,
    )
    try:
        api_response = api_instance.add_step(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->add_step: %s\n" % e)
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
[**WorkflowStepAddForm**](../../models/WorkflowStepAddForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#add_step.ApiResponseForDefault) | default response

#### add_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **copy_scheme**
<a name="copy_scheme"></a>
> copy_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_copy_form import WorkflowCopyForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.copy_scheme(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->copy_scheme: %s\n" % e)

    # example passing only optional values
    path_params = {
        'schemeId': "schemeId_example",
    }
    query_params = {
        'name': "name_example",
    }
    body = WorkflowCopyForm(
        name="name_example",
    )
    try:
        api_response = api_instance.copy_scheme(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->copy_scheme: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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
[**WorkflowCopyForm**](../../models/WorkflowCopyForm.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#copy_scheme.ApiResponseForDefault) | default response

#### copy_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_action**
<a name="delete_action"></a>
> delete_action(action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.delete_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->delete_action: %s\n" % e)
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
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_action.ApiResponseForDefault) | default response

#### delete_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_action1**
<a name="delete_action1"></a>
> delete_action1(action_idstep_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
        'stepId': "stepId_example",
    }
    try:
        api_response = api_instance.delete_action1(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->delete_action1: %s\n" % e)
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
actionId | ActionIdSchema | | 
stepId | StepIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_action1.ApiResponseForDefault) | default response

#### delete_action1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_actionlet**
<a name="delete_actionlet"></a>
> delete_actionlet(actionlet_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionletId': "actionletId_example",
    }
    try:
        api_response = api_instance.delete_actionlet(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->delete_actionlet: %s\n" % e)
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
actionletId | ActionletIdSchema | | 

# ActionletIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_actionlet.ApiResponseForDefault) | default response

#### delete_actionlet.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_scheme**
<a name="delete_scheme"></a>
> delete_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    try:
        api_response = api_instance.delete_scheme(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->delete_scheme: %s\n" % e)
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
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_scheme.ApiResponseForDefault) | default response

#### delete_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_step**
<a name="delete_step"></a>
> delete_step(step_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
    }
    try:
        api_response = api_instance.delete_step(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->delete_step: %s\n" % e)
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
stepId | StepIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#delete_step.ApiResponseForDefault) | default response

#### delete_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **deletes_system_action**
<a name="deletes_system_action"></a>
> deletes_system_action(identifier)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'identifier': "identifier_example",
    }
    try:
        api_response = api_instance.deletes_system_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->deletes_system_action: %s\n" % e)
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
identifier | IdentifierSchema | | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#deletes_system_action.ApiResponseForDefault) | default response

#### deletes_system_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **evaluate_action_condition**
<a name="evaluate_action_condition"></a>
> evaluate_action_condition(action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.evaluate_action_condition(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->evaluate_action_condition: %s\n" % e)
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
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#evaluate_action_condition.ApiResponseForDefault) | default response

#### evaluate_action_condition.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export_scheme**
<a name="export_scheme"></a>
> export_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    try:
        api_response = api_instance.export_scheme(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->export_scheme: %s\n" % e)
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
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#export_scheme.ApiResponseForDefault) | default response

#### export_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_action**
<a name="find_action"></a>
> find_action(action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.find_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_action: %s\n" % e)
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
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_action.ApiResponseForDefault) | default response

#### find_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_action_by_step**
<a name="find_action_by_step"></a>
> find_action_by_step(step_idaction_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.find_action_by_step(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_action_by_step: %s\n" % e)
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
stepId | StepIdSchema | | 
actionId | ActionIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_action_by_step.ApiResponseForDefault) | default response

#### find_action_by_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_actionlets**
<a name="find_actionlets"></a>
> find_actionlets()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.find_actionlets()
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_actionlets: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_actionlets.ApiResponseForDefault) | default response

#### find_actionlets.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_actionlets_by_action**
<a name="find_actionlets_by_action"></a>
> find_actionlets_by_action(action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.find_actionlets_by_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_actionlets_by_action: %s\n" % e)
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
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_actionlets_by_action.ApiResponseForDefault) | default response

#### find_actionlets_by_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_actions_by_scheme**
<a name="find_actions_by_scheme"></a>
> find_actions_by_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    try:
        api_response = api_instance.find_actions_by_scheme(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_actions_by_scheme: %s\n" % e)
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
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_actions_by_scheme.ApiResponseForDefault) | default response

#### find_actions_by_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_actions_by_schemes_and_system_action**
<a name="find_actions_by_schemes_and_system_action"></a>
> find_actions_by_schemes_and_system_action(system_action)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_schemes_form import WorkflowSchemesForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemAction': "NEW",
    }
    try:
        api_response = api_instance.find_actions_by_schemes_and_system_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_actions_by_schemes_and_system_action: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemAction': "NEW",
    }
    body = WorkflowSchemesForm(
        schemes=[
            "schemes_example"
        ],
    )
    try:
        api_response = api_instance.find_actions_by_schemes_and_system_action(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_actions_by_schemes_and_system_action: %s\n" % e)
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
[**WorkflowSchemesForm**](../../models/WorkflowSchemesForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemAction | SystemActionSchema | | 

# SystemActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "EDIT", "PUBLISH", "UNPUBLISH", "ARCHIVE", "UNARCHIVE", "DELETE", "DESTROY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_actions_by_schemes_and_system_action.ApiResponseForDefault) | default response

#### find_actions_by_schemes_and_system_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_actions_by_step**
<a name="find_actions_by_step"></a>
> find_actions_by_step(step_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
    }
    try:
        api_response = api_instance.find_actions_by_step(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_actions_by_step: %s\n" % e)
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
stepId | StepIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_actions_by_step.ApiResponseForDefault) | default response

#### find_actions_by_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_all_schemes_and_schemes_by_content_type**
<a name="find_all_schemes_and_schemes_by_content_type"></a>
> find_all_schemes_and_schemes_by_content_type(content_type_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentTypeId': "contentTypeId_example",
    }
    try:
        api_response = api_instance.find_all_schemes_and_schemes_by_content_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_all_schemes_and_schemes_by_content_type: %s\n" % e)
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
contentTypeId | ContentTypeIdSchema | | 

# ContentTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_all_schemes_and_schemes_by_content_type.ApiResponseForDefault) | default response

#### find_all_schemes_and_schemes_by_content_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_available_actions**
<a name="find_available_actions"></a>
> find_available_actions(inode)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'inode': "inode_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.find_available_actions(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_available_actions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'inode': "inode_example",
    }
    query_params = {
        'renderMode': "renderMode_example",
    }
    try:
        api_response = api_instance.find_available_actions(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_available_actions: %s\n" % e)
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
renderMode | RenderModeSchema | | optional


# RenderModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | 

# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_available_actions.ApiResponseForDefault) | default response

#### find_available_actions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_available_default_actions_by_content_type**
<a name="find_available_default_actions_by_content_type"></a>
> find_available_default_actions_by_content_type(content_type_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentTypeId': "contentTypeId_example",
    }
    try:
        api_response = api_instance.find_available_default_actions_by_content_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_available_default_actions_by_content_type: %s\n" % e)
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
contentTypeId | ContentTypeIdSchema | | 

# ContentTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_available_default_actions_by_content_type.ApiResponseForDefault) | default response

#### find_available_default_actions_by_content_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_available_default_actions_by_schemes**
<a name="find_available_default_actions_by_schemes"></a>
> find_available_default_actions_by_schemes()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    query_params = {
        'ids': "ids_example",
    }
    try:
        api_response = api_instance.find_available_default_actions_by_schemes(
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_available_default_actions_by_schemes: %s\n" % e)
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
ids | IdsSchema | | optional


# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_available_default_actions_by_schemes.ApiResponseForDefault) | default response

#### find_available_default_actions_by_schemes.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_initial_available_actions_by_content_type**
<a name="find_initial_available_actions_by_content_type"></a>
> find_initial_available_actions_by_content_type(content_type_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentTypeId': "contentTypeId_example",
    }
    try:
        api_response = api_instance.find_initial_available_actions_by_content_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_initial_available_actions_by_content_type: %s\n" % e)
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
contentTypeId | ContentTypeIdSchema | | 

# ContentTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_initial_available_actions_by_content_type.ApiResponseForDefault) | default response

#### find_initial_available_actions_by_content_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_schemes**
<a name="find_schemes"></a>
> find_schemes()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    query_params = {
        'contentTypeId': "contentTypeId_example",
        'showArchive': True,
    }
    try:
        api_response = api_instance.find_schemes(
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_schemes: %s\n" % e)
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
contentTypeId | ContentTypeIdSchema | | optional
showArchive | ShowArchiveSchema | | optional


# ContentTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ShowArchiveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_schemes.ApiResponseForDefault) | default response

#### find_schemes.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_step_by_id**
<a name="find_step_by_id"></a>
> find_step_by_id(step_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
    }
    try:
        api_response = api_instance.find_step_by_id(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_step_by_id: %s\n" % e)
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
stepId | StepIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_step_by_id.ApiResponseForDefault) | default response

#### find_step_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_steps_by_scheme**
<a name="find_steps_by_scheme"></a>
> find_steps_by_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    try:
        api_response = api_instance.find_steps_by_scheme(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_steps_by_scheme: %s\n" % e)
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
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_steps_by_scheme.ApiResponseForDefault) | default response

#### find_steps_by_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_system_actions_by_content_type**
<a name="find_system_actions_by_content_type"></a>
> find_system_actions_by_content_type(content_type_var_or_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'contentTypeVarOrId': "contentTypeVarOrId_example",
    }
    try:
        api_response = api_instance.find_system_actions_by_content_type(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_system_actions_by_content_type: %s\n" % e)
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
contentTypeVarOrId | ContentTypeVarOrIdSchema | | 

# ContentTypeVarOrIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_system_actions_by_content_type.ApiResponseForDefault) | default response

#### find_system_actions_by_content_type.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_system_actions_by_scheme**
<a name="find_system_actions_by_scheme"></a>
> find_system_actions_by_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    try:
        api_response = api_instance.find_system_actions_by_scheme(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->find_system_actions_by_scheme: %s\n" % e)
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
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#find_system_actions_by_scheme.ApiResponseForDefault) | default response

#### find_system_actions_by_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_action_by_name_single_part**
<a name="fire_action_by_name_single_part"></a>
> ResponseEntityView fire_action_by_name_single_part()

Fire action by name

### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.response_entity_view import ResponseEntityView
from dotcms_rest_client.model.fire_action_by_name_form import FireActionByNameForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    query_params = {
        'inode': "inode_example",
        'identifier': "identifier_example",
        'indexPolicy': "indexPolicy_example",
        'language': "-1",
    }
    body = FireActionByNameForm(
        comments="comments_example",
        assign="assign_example",
        publish_date="publish_date_example",
        publish_time="publish_time_example",
        expire_date="expire_date_example",
        expire_time="expire_time_example",
        never_expire="never_expire_example",
        where_to_send="where_to_send_example",
        filter_key="filter_key_example",
        query="query_example",
        path_to_move="path_to_move_example",
        timezone_id="timezone_id_example",
        individual_permissions=dict(
            "key": [
                "key_example"
            ],
        ),
        action_name="action_name_example",
        iwant_to="iwant_to_example",
        contentlet=dict(
            "key": dict(),
        ),
    )
    try:
        # Fire action by name
        api_response = api_instance.fire_action_by_name_single_part(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_by_name_single_part: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FireActionByNameForm**](../../models/FireActionByNameForm.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | optional
identifier | IdentifierSchema | | optional
indexPolicy | IndexPolicySchema | | optional
language | LanguageSchema | | optional


# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndexPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "-1"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fire_action_by_name_single_part.ApiResponseFor200) | 
400 | [ApiResponseFor400](#fire_action_by_name_single_part.ApiResponseFor400) | Action not found

#### fire_action_by_name_single_part.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityView**](../../models/ResponseEntityView.md) |  | 


#### fire_action_by_name_single_part.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_action_default_multipart_new_path**
<a name="fire_action_default_multipart_new_path"></a>
> ResponseEntityView fire_action_default_multipart_new_path(system_action)

Fire default action by name multipart

### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.response_entity_view import ResponseEntityView
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
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemAction': "NEW",
    }
    query_params = {
    }
    try:
        # Fire default action by name multipart
        api_response = api_instance.fire_action_default_multipart_new_path(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_default_multipart_new_path: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemAction': "NEW",
    }
    query_params = {
        'inode': "inode_example",
        'identifier': "identifier_example",
        'indexPolicy': "indexPolicy_example",
        'language': "-1",
    }
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
        # Fire default action by name multipart
        api_response = api_instance.fire_action_default_multipart_new_path(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_default_multipart_new_path: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**FormDataMultiPart**](../../models/FormDataMultiPart.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | optional
identifier | IdentifierSchema | | optional
indexPolicy | IndexPolicySchema | | optional
language | LanguageSchema | | optional


# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndexPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "-1"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemAction | SystemActionSchema | | 

# SystemActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "EDIT", "PUBLISH", "UNPUBLISH", "ARCHIVE", "UNARCHIVE", "DELETE", "DESTROY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fire_action_default_multipart_new_path.ApiResponseFor200) | 
400 | [ApiResponseFor400](#fire_action_default_multipart_new_path.ApiResponseFor400) | Action not found

#### fire_action_default_multipart_new_path.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityView**](../../models/ResponseEntityView.md) |  | 


#### fire_action_default_multipart_new_path.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_action_default_single_part**
<a name="fire_action_default_single_part"></a>
> ResponseEntityView fire_action_default_single_part(system_action)

Fire default action by name

### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.response_entity_view import ResponseEntityView
from dotcms_rest_client.model.fire_action_form import FireActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemAction': "NEW",
    }
    query_params = {
    }
    try:
        # Fire default action by name
        api_response = api_instance.fire_action_default_single_part(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_default_single_part: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemAction': "NEW",
    }
    query_params = {
        'inode': "inode_example",
        'identifier': "identifier_example",
        'indexPolicy': "indexPolicy_example",
        'language': "-1",
    }
    body = FireActionForm(
        comments="comments_example",
        assign="assign_example",
        publish_date="publish_date_example",
        publish_time="publish_time_example",
        expire_date="expire_date_example",
        expire_time="expire_time_example",
        never_expire="never_expire_example",
        where_to_send="where_to_send_example",
        filter_key="filter_key_example",
        query="query_example",
        path_to_move="path_to_move_example",
        timezone_id="timezone_id_example",
        individual_permissions=dict(
            "key": [
                "key_example"
            ],
        ),
        iwant_to="iwant_to_example",
        contentlet=dict(
            "key": dict(),
        ),
    )
    try:
        # Fire default action by name
        api_response = api_instance.fire_action_default_single_part(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_default_single_part: %s\n" % e)
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
[**FireActionForm**](../../models/FireActionForm.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | optional
identifier | IdentifierSchema | | optional
indexPolicy | IndexPolicySchema | | optional
language | LanguageSchema | | optional


# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndexPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "-1"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemAction | SystemActionSchema | | 

# SystemActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "EDIT", "PUBLISH", "UNPUBLISH", "ARCHIVE", "UNARCHIVE", "DELETE", "DESTROY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fire_action_default_single_part.ApiResponseFor200) | 
400 | [ApiResponseFor400](#fire_action_default_single_part.ApiResponseFor400) | Action not found

#### fire_action_default_single_part.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityView**](../../models/ResponseEntityView.md) |  | 


#### fire_action_default_single_part.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_action_multipart_new_path**
<a name="fire_action_multipart_new_path"></a>
> ResponseEntityView fire_action_multipart_new_path(action_id)

Fire action by ID multipart

### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.response_entity_view import ResponseEntityView
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
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    query_params = {
    }
    try:
        # Fire action by ID multipart
        api_response = api_instance.fire_action_multipart_new_path(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_multipart_new_path: %s\n" % e)

    # example passing only optional values
    path_params = {
        'actionId': "actionId_example",
    }
    query_params = {
        'inode': "inode_example",
        'identifier': "identifier_example",
        'indexPolicy': "indexPolicy_example",
        'language': "-1",
    }
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
        # Fire action by ID multipart
        api_response = api_instance.fire_action_multipart_new_path(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_multipart_new_path: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**FormDataMultiPart**](../../models/FormDataMultiPart.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | optional
identifier | IdentifierSchema | | optional
indexPolicy | IndexPolicySchema | | optional
language | LanguageSchema | | optional


# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndexPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "-1"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fire_action_multipart_new_path.ApiResponseFor200) | 
404 | [ApiResponseFor404](#fire_action_multipart_new_path.ApiResponseFor404) | Action not found

#### fire_action_multipart_new_path.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityView**](../../models/ResponseEntityView.md) |  | 


#### fire_action_multipart_new_path.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_action_single_part**
<a name="fire_action_single_part"></a>
> ResponseEntityView fire_action_single_part(action_id)

Fire action by ID

### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.response_entity_view import ResponseEntityView
from dotcms_rest_client.model.fire_action_form import FireActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    query_params = {
    }
    try:
        # Fire action by ID
        api_response = api_instance.fire_action_single_part(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_single_part: %s\n" % e)

    # example passing only optional values
    path_params = {
        'actionId': "actionId_example",
    }
    query_params = {
        'inode': "inode_example",
        'identifier': "identifier_example",
        'indexPolicy': "indexPolicy_example",
        'language': "-1",
    }
    body = FireActionForm(
        comments="comments_example",
        assign="assign_example",
        publish_date="publish_date_example",
        publish_time="publish_time_example",
        expire_date="expire_date_example",
        expire_time="expire_time_example",
        never_expire="never_expire_example",
        where_to_send="where_to_send_example",
        filter_key="filter_key_example",
        query="query_example",
        path_to_move="path_to_move_example",
        timezone_id="timezone_id_example",
        individual_permissions=dict(
            "key": [
                "key_example"
            ],
        ),
        iwant_to="iwant_to_example",
        contentlet=dict(
            "key": dict(),
        ),
    )
    try:
        # Fire action by ID
        api_response = api_instance.fire_action_single_part(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_action_single_part: %s\n" % e)
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
[**FireActionForm**](../../models/FireActionForm.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | optional
identifier | IdentifierSchema | | optional
indexPolicy | IndexPolicySchema | | optional
language | LanguageSchema | | optional


# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndexPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "-1"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fire_action_single_part.ApiResponseFor200) | 
404 | [ApiResponseFor404](#fire_action_single_part.ApiResponseFor404) | Action not found

#### fire_action_single_part.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityView**](../../models/ResponseEntityView.md) |  | 


#### fire_action_single_part.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_bulk_actions**
<a name="fire_bulk_actions"></a>
> EventOutput fire_bulk_actions()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.event_output import EventOutput
from dotcms_rest_client.model.fire_bulk_actions_form import FireBulkActionsForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = FireBulkActionsForm(
        query="query_example",
        contentlet_ids=[
            "contentlet_ids_example"
        ],
        workflow_action_id="workflow_action_id_example",
        additional_params=AdditionalParamsBean(
            push_publish=PushPublishBean(
                where_to_send="where_to_send_example",
                publish_date="publish_date_example",
                publish_time="publish_time_example",
                expire_date="expire_date_example",
                expire_time="expire_time_example",
                never_expire="never_expire_example",
                filter_key="filter_key_example",
                i_want_to="i_want_to_example",
                timezone_id="timezone_id_example",
                iwant_to="iwant_to_example",
            ),
            assign_comment=AssignCommentBean(
                assign="assign_example",
                comment="comment_example",
            ),
            additional_params_map=dict(
                "key": dict(),
            ),
            push_publish_bean=PushPublishBean(),
            assign_comment_bean=AssignCommentBean(),
        ),
        popup_params_bean=AdditionalParamsBean(),
    )
    try:
        api_response = api_instance.fire_bulk_actions(
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_bulk_actions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/event-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**FireBulkActionsForm**](../../models/FireBulkActionsForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fire_bulk_actions.ApiResponseForDefault) | default response

#### fire_bulk_actions.ApiResponseForDefault
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

# **fire_bulk_actions1**
<a name="fire_bulk_actions1"></a>
> fire_bulk_actions1()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.fire_bulk_actions_form import FireBulkActionsForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = FireBulkActionsForm(
        query="query_example",
        contentlet_ids=[
            "contentlet_ids_example"
        ],
        workflow_action_id="workflow_action_id_example",
        additional_params=AdditionalParamsBean(
            push_publish=PushPublishBean(
                where_to_send="where_to_send_example",
                publish_date="publish_date_example",
                publish_time="publish_time_example",
                expire_date="expire_date_example",
                expire_time="expire_time_example",
                never_expire="never_expire_example",
                filter_key="filter_key_example",
                i_want_to="i_want_to_example",
                timezone_id="timezone_id_example",
                iwant_to="iwant_to_example",
            ),
            assign_comment=AssignCommentBean(
                assign="assign_example",
                comment="comment_example",
            ),
            additional_params_map=dict(
                "key": dict(),
            ),
            push_publish_bean=PushPublishBean(),
            assign_comment_bean=AssignCommentBean(),
        ),
        popup_params_bean=AdditionalParamsBean(),
    )
    try:
        api_response = api_instance.fire_bulk_actions1(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_bulk_actions1: %s\n" % e)
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
[**FireBulkActionsForm**](../../models/FireBulkActionsForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fire_bulk_actions1.ApiResponseForDefault) | default response

#### fire_bulk_actions1.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_merge_action_default**
<a name="fire_merge_action_default"></a>
> fire_merge_action_default(system_action)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.fire_action_form import FireActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemAction': "NEW",
    }
    query_params = {
    }
    try:
        api_response = api_instance.fire_merge_action_default(
            path_params=path_params,
            query_params=query_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_merge_action_default: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemAction': "NEW",
    }
    query_params = {
        'inode': "inode_example",
        'identifier': "identifier_example",
        'language': "-1",
        'offset': 1,
    }
    body = FireActionForm(
        comments="comments_example",
        assign="assign_example",
        publish_date="publish_date_example",
        publish_time="publish_time_example",
        expire_date="expire_date_example",
        expire_time="expire_time_example",
        never_expire="never_expire_example",
        where_to_send="where_to_send_example",
        filter_key="filter_key_example",
        query="query_example",
        path_to_move="path_to_move_example",
        timezone_id="timezone_id_example",
        individual_permissions=dict(
            "key": [
                "key_example"
            ],
        ),
        iwant_to="iwant_to_example",
        contentlet=dict(
            "key": dict(),
        ),
    )
    try:
        api_response = api_instance.fire_merge_action_default(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_merge_action_default: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**FireActionForm**](../../models/FireActionForm.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
inode | InodeSchema | | optional
identifier | IdentifierSchema | | optional
language | LanguageSchema | | optional
offset | OffsetSchema | | optional


# InodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentifierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "-1"

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemAction | SystemActionSchema | | 

# SystemActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "EDIT", "PUBLISH", "UNPUBLISH", "ARCHIVE", "UNARCHIVE", "DELETE", "DESTROY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fire_merge_action_default.ApiResponseForDefault) | default response

#### fire_merge_action_default.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fire_multiple_action_default**
<a name="fire_multiple_action_default"></a>
> ResponseEntityView fire_multiple_action_default(system_action)

Fire default action by name on multiple contents

### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.response_entity_view import ResponseEntityView
from dotcms_rest_client.model.fire_multiple_action_form import FireMultipleActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'systemAction': "NEW",
    }
    try:
        # Fire default action by name on multiple contents
        api_response = api_instance.fire_multiple_action_default(
            path_params=path_params,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_multiple_action_default: %s\n" % e)

    # example passing only optional values
    path_params = {
        'systemAction': "NEW",
    }
    body = FireMultipleActionForm(
        comments="comments_example",
        assign="assign_example",
        publish_date="publish_date_example",
        publish_time="publish_time_example",
        expire_date="expire_date_example",
        expire_time="expire_time_example",
        never_expire="never_expire_example",
        where_to_send="where_to_send_example",
        filter_key="filter_key_example",
        timezone_id="timezone_id_example",
        iwant_to="iwant_to_example",
        contentlet=[
            dict(
                "key": dict(),
            )
        ],
    )
    try:
        # Fire default action by name on multiple contents
        api_response = api_instance.fire_multiple_action_default(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->fire_multiple_action_default: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
[**FireMultipleActionForm**](../../models/FireMultipleActionForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
systemAction | SystemActionSchema | | 

# SystemActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NEW", "EDIT", "PUBLISH", "UNPUBLISH", "ARCHIVE", "UNARCHIVE", "DELETE", "DESTROY", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#fire_multiple_action_default.ApiResponseFor200) | 
400 | [ApiResponseFor400](#fire_multiple_action_default.ApiResponseFor400) | Action not found

#### fire_multiple_action_default.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseEntityView**](../../models/ResponseEntityView.md) |  | 


#### fire_multiple_action_default.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_bulk_actions**
<a name="get_bulk_actions"></a>
> get_bulk_actions()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.bulk_action_form import BulkActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = BulkActionForm(
        contentlet_ids=[
            "contentlet_ids_example"
        ],
        query="query_example",
    )
    try:
        api_response = api_instance.get_bulk_actions(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->get_bulk_actions: %s\n" % e)
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
[**BulkActionForm**](../../models/BulkActionForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_bulk_actions.ApiResponseForDefault) | default response

#### get_bulk_actions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_system_actions_referred_by_workflow_action**
<a name="get_system_actions_referred_by_workflow_action"></a>
> get_system_actions_referred_by_workflow_action(workflow_action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'workflowActionId': "workflowActionId_example",
    }
    try:
        api_response = api_instance.get_system_actions_referred_by_workflow_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->get_system_actions_referred_by_workflow_action: %s\n" % e)
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
workflowActionId | WorkflowActionIdSchema | | 

# WorkflowActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#get_system_actions_referred_by_workflow_action.ApiResponseForDefault) | default response

#### get_system_actions_referred_by_workflow_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_scheme**
<a name="import_scheme"></a>
> import_scheme()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_scheme_import_object_form import WorkflowSchemeImportObjectForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = WorkflowSchemeImportObjectForm(
        workflow_object=WorkflowSchemeImportExportObjectView(
            version="version_example",
            schemes=[
                WorkflowScheme(
                    id="id_example",
                    creation_date="1970-01-01T00:00:00.00Z",
                    name="name_example",
                    description="description_example",
                    archived=True,
                    mandatory=True,
                    default_scheme=True,
                    mod_date="1970-01-01T00:00:00.00Z",
                    entry_action_id="entry_action_id_example",
                    system=True,
                )
            ],
            steps=[
                WorkflowStep(
                    id="id_example",
                    creation_date="1970-01-01T00:00:00.00Z",
                    name="name_example",
                    scheme_id="scheme_id_example",
                    my_order=1,
                    resolved=True,
                    enable_escalation=True,
                    escalation_action="escalation_action_example",
                    escalation_time=1,
                )
            ],
            actions=[
                WorkflowAction(
                    id="id_example",
                    name="name_example",
                    scheme_id="scheme_id_example",
                    condition="condition_example",
                    next_step="next_step_example",
                    next_assign="next_assign_example",
                    icon="icon_example",
                    role_hierarchy_for_assign=True,
                    assignable=True,
                    commentable=True,
                    order=1,
                    save_actionlet=True,
                    publish_actionlet=True,
                    unpublish_actionlet=True,
                    archive_actionlet=True,
                    push_publish_actionlet=True,
                    unarchive_actionlet=True,
                    delete_actionlet=True,
                    destroy_actionlet=True,
                    move_actionlet=True,
                    owner="owner_example",
                    move_actionlet_hash_path=True,
                    next_step_current_step=True,
                    show_on=[
                        "NEW"
                    ],
                )
            ],
            action_steps=[
                dict(
                    "key": "key_example",
                )
            ],
            action_classes=[
                WorkflowActionClass(
                    id="id_example",
                    action_id="action_id_example",
                    name="name_example",
                    order=1,
                    clazz="clazz_example",
                    actionlet=WorkFlowActionlet(
                        action_class="action_class_example",
                        how_to="how_to_example",
                        localized_howto="localized_howto_example",
                        localized_name="localized_name_example",
                        name="name_example",
                        parameters=[
                            WorkflowActionletParameter(
                                display_name="display_name_example",
                                key="key_example",
                                default_value="default_value_example",
                                required=True,
                            )
                        ],
                    ),
                )
            ],
            action_class_params=[
                WorkflowActionClassParameter(
                    id="id_example",
                    action_class_id="action_class_id_example",
                    key="key_example",
                    value="value_example",
                )
            ],
            scheme_system_action_workflow_action_mappings=[
                SystemActionWorkflowActionMapping(
                    identifier="identifier_example",
                    system_action="NEW",
                    workflow_action=WorkflowAction(),
                    owner=dict(),
                    owner_content_type=True,
                    owner_scheme=True,
                )
            ],
        ),
        permissions=[
            Permission(
                id=1,
                inode="inode_example",
                permission=1,
                type="type_example",
                bit_permission=True,
                individual_permission=True,
                role_id="role_id_example",
            )
        ],
        workflow_import_object=WorkflowSchemeImportExportObjectView(),
    )
    try:
        api_response = api_instance.import_scheme(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->import_scheme: %s\n" % e)
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
[**WorkflowSchemeImportObjectForm**](../../models/WorkflowSchemeImportObjectForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#import_scheme.ApiResponseForDefault) | default response

#### import_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **reorder_action**
<a name="reorder_action"></a>
> reorder_action(step_idaction_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_reorder_workflow_action_step_form import WorkflowReorderWorkflowActionStepForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.reorder_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->reorder_action: %s\n" % e)

    # example passing only optional values
    path_params = {
        'stepId': "stepId_example",
        'actionId': "actionId_example",
    }
    body = WorkflowReorderWorkflowActionStepForm(
        order=1,
    )
    try:
        api_response = api_instance.reorder_action(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->reorder_action: %s\n" % e)
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
[**WorkflowReorderWorkflowActionStepForm**](../../models/WorkflowReorderWorkflowActionStepForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
stepId | StepIdSchema | | 
actionId | ActionIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#reorder_action.ApiResponseForDefault) | default response

#### reorder_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **reorder_step**
<a name="reorder_step"></a>
> reorder_step(step_idorder)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
        'order': 1,
    }
    try:
        api_response = api_instance.reorder_step(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->reorder_step: %s\n" % e)
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
stepId | StepIdSchema | | 
order | OrderSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#reorder_step.ApiResponseForDefault) | default response

#### reorder_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_action**
<a name="save_action"></a>
> save_action()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_action_form import WorkflowActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = WorkflowActionForm(
        action_id="action_id_example",
        scheme_id="scheme_id_example",
        step_id="step_id_example",
        action_name="action_name_example",
        who_can_use=[
            "who_can_use_example"
        ],
        action_icon="action_icon_example",
        action_assignable=True,
        action_commentable=True,
        requires_checkout=True,
        show_on=[
            "NEW"
        ],
        action_role_hierarchy_for_assign=True,
        role_hierarchy_for_assign=True,
        action_next_step="action_next_step_example",
        action_next_assign="action_next_assign_example",
        action_condition="action_condition_example",
    )
    try:
        api_response = api_instance.save_action(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_action: %s\n" % e)
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
[**WorkflowActionForm**](../../models/WorkflowActionForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_action.ApiResponseForDefault) | default response

#### save_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_action_to_step**
<a name="save_action_to_step"></a>
> save_action_to_step(step_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_action_step_form import WorkflowActionStepForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
    }
    try:
        api_response = api_instance.save_action_to_step(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_action_to_step: %s\n" % e)

    # example passing only optional values
    path_params = {
        'stepId': "stepId_example",
    }
    body = WorkflowActionStepForm(
        action_id="action_id_example",
    )
    try:
        api_response = api_instance.save_action_to_step(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_action_to_step: %s\n" % e)
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
[**WorkflowActionStepForm**](../../models/WorkflowActionStepForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
stepId | StepIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_action_to_step.ApiResponseForDefault) | default response

#### save_action_to_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_actionlet_to_action**
<a name="save_actionlet_to_action"></a>
> save_actionlet_to_action(action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_actionlet_action_form import WorkflowActionletActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.save_actionlet_to_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_actionlet_to_action: %s\n" % e)

    # example passing only optional values
    path_params = {
        'actionId': "actionId_example",
    }
    body = WorkflowActionletActionForm(
        actionlet_class="actionlet_class_example",
        order=1,
        parameters=dict(
            "key": "key_example",
        ),
    )
    try:
        api_response = api_instance.save_actionlet_to_action(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_actionlet_to_action: %s\n" % e)
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
[**WorkflowActionletActionForm**](../../models/WorkflowActionletActionForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_actionlet_to_action.ApiResponseForDefault) | default response

#### save_actionlet_to_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_scheme**
<a name="save_scheme"></a>
> save_scheme()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_scheme_form import WorkflowSchemeForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = WorkflowSchemeForm(
        scheme_name="scheme_name_example",
        scheme_description="scheme_description_example",
        scheme_archived=True,
    )
    try:
        api_response = api_instance.save_scheme(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_scheme: %s\n" % e)
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
[**WorkflowSchemeForm**](../../models/WorkflowSchemeForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_scheme.ApiResponseForDefault) | default response

#### save_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **save_system_action**
<a name="save_system_action"></a>
> save_system_action()



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_system_action_form import WorkflowSystemActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only optional values
    body = WorkflowSystemActionForm(
        action_id="action_id_example",
        scheme_id="scheme_id_example",
        content_type_variable="content_type_variable_example",
        system_action="NEW",
    )
    try:
        api_response = api_instance.save_system_action(
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->save_system_action: %s\n" % e)
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
[**WorkflowSystemActionForm**](../../models/WorkflowSystemActionForm.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#save_system_action.ApiResponseForDefault) | default response

#### save_system_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_action**
<a name="update_action"></a>
> update_action(action_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_action_form import WorkflowActionForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'actionId': "actionId_example",
    }
    try:
        api_response = api_instance.update_action(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->update_action: %s\n" % e)

    # example passing only optional values
    path_params = {
        'actionId': "actionId_example",
    }
    body = WorkflowActionForm(
        action_id="action_id_example",
        scheme_id="scheme_id_example",
        step_id="step_id_example",
        action_name="action_name_example",
        who_can_use=[
            "who_can_use_example"
        ],
        action_icon="action_icon_example",
        action_assignable=True,
        action_commentable=True,
        requires_checkout=True,
        show_on=[
            "NEW"
        ],
        action_role_hierarchy_for_assign=True,
        role_hierarchy_for_assign=True,
        action_next_step="action_next_step_example",
        action_next_assign="action_next_assign_example",
        action_condition="action_condition_example",
    )
    try:
        api_response = api_instance.update_action(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->update_action: %s\n" % e)
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
[**WorkflowActionForm**](../../models/WorkflowActionForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
actionId | ActionIdSchema | | 

# ActionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#update_action.ApiResponseForDefault) | default response

#### update_action.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_scheme**
<a name="update_scheme"></a>
> update_scheme(scheme_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_scheme_form import WorkflowSchemeForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'schemeId': "schemeId_example",
    }
    try:
        api_response = api_instance.update_scheme(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->update_scheme: %s\n" % e)

    # example passing only optional values
    path_params = {
        'schemeId': "schemeId_example",
    }
    body = WorkflowSchemeForm(
        scheme_name="scheme_name_example",
        scheme_description="scheme_description_example",
        scheme_archived=True,
    )
    try:
        api_response = api_instance.update_scheme(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->update_scheme: %s\n" % e)
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
[**WorkflowSchemeForm**](../../models/WorkflowSchemeForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
schemeId | SchemeIdSchema | | 

# SchemeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#update_scheme.ApiResponseForDefault) | default response

#### update_scheme.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_step**
<a name="update_step"></a>
> update_step(step_id)



### Example

```python
import dotcms_rest_client
from dotcms_rest_client.apis.tags import workflow_api
from dotcms_rest_client.model.workflow_step_update_form import WorkflowStepUpdateForm
from pprint import pprint
# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = dotcms_rest_client.Configuration(
    host = "/api"
)

# Enter a context with an instance of the API client
with dotcms_rest_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workflow_api.WorkflowApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stepId': "stepId_example",
    }
    try:
        api_response = api_instance.update_step(
            path_params=path_params,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->update_step: %s\n" % e)

    # example passing only optional values
    path_params = {
        'stepId': "stepId_example",
    }
    body = WorkflowStepUpdateForm(
        step_order=1,
        step_name="step_name_example",
        enable_escalation=True,
        escalation_action="escalation_action_example",
        escalation_time="escalation_time_example",
        step_resolved=True,
    )
    try:
        api_response = api_instance.update_step(
            path_params=path_params,
            body=body,
        )
    except dotcms_rest_client.ApiException as e:
        print("Exception when calling WorkflowApi->update_step: %s\n" % e)
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
[**WorkflowStepUpdateForm**](../../models/WorkflowStepUpdateForm.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
stepId | StepIdSchema | | 

# StepIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#update_step.ApiResponseForDefault) | default response

#### update_step.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

