# pandadoc_client.UserAndWorkspaceManagementApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](UserAndWorkspaceManagementApi.md#add_member) | **POST** /public/v1/workspaces/{workspace_id}/members | Add member
[**create_user**](UserAndWorkspaceManagementApi.md#create_user) | **POST** /public/v1/users | Create User
[**create_workspace**](UserAndWorkspaceManagementApi.md#create_workspace) | **POST** /public/v1/workspaces | Create Workspace


# **add_member**
> AddMemberResponse add_member(workspace_id, add_member_request)

Add member

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import user_and_workspace_management_api
from pandadoc_client.model.add_member_response import AddMemberResponse
from pandadoc_client.model.add_member_request import AddMemberRequest
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_and_workspace_management_api.UserAndWorkspaceManagementApi(api_client)
    workspace_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | 
    add_member_request = AddMemberRequest(
        user_id="2eWSKSvVqmuVCnuUK3iWwD",
        role="Admin",
    )  # AddMemberRequest | 
    notify_user = True  # bool | Send a confirmation email to the user that was added to workspace(s). (optional)
    notify_ws_admins = True  # bool | Send a confirmation email to all workspace admins indicating that the user has been added to the workspace. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add member
        api_response = api_instance.add_member(workspace_id, add_member_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling UserAndWorkspaceManagementApi->add_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add member
        api_response = api_instance.add_member(
            workspace_id,
            add_member_request,
            notify_user=notify_user,
            notify_ws_admins=notify_ws_admins,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling UserAndWorkspaceManagementApi->add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  |
 **add_member_request** | [**AddMemberRequest**](AddMemberRequest.md)|  |
 **notify_user** | **bool**| Send a confirmation email to the user that was added to workspace(s). | [optional]
 **notify_ws_admins** | **bool**| Send a confirmation email to all workspace admins indicating that the user has been added to the workspace. | [optional]

### Return type

[**AddMemberResponse**](AddMemberResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_user**
> CreateUserResponse create_user(create_user_request)

Create User

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import user_and_workspace_management_api
from pandadoc_client.model.create_user_request import CreateUserRequest
from pandadoc_client.model.create_user_response import CreateUserResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_and_workspace_management_api.UserAndWorkspaceManagementApi(api_client)
    create_user_request = CreateUserRequest(
        user=CreateUserRequestUser(
            email="email@example.com",
            first_name="John",
            last_name="Doe",
            phone_number="+14842634627",
        ),
        workspaces=[
            CreateUserRequestWorkspaces(
                workspace_id="2eWSKSvVqmuVCnuUK3iWwD",
                role="Admin",
            ),
        ],
        license="Full",
    )  # CreateUserRequest | 
    notify_user = True  # bool | Send a confirmation email to the user that was added to workspace(s). (optional)
    notify_ws_admins = True  # bool | Send a confirmation email to all workspace admins indicating that the user has been added to the workspace. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.create_user(create_user_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling UserAndWorkspaceManagementApi->create_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create User
        api_response = api_instance.create_user(
            create_user_request,
            notify_user=notify_user,
            notify_ws_admins=notify_ws_admins,
        )
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling UserAndWorkspaceManagementApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  |
 **notify_user** | **bool**| Send a confirmation email to the user that was added to workspace(s). | [optional]
 **notify_ws_admins** | **bool**| Send a confirmation email to all workspace admins indicating that the user has been added to the workspace. | [optional]

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_workspace**
> CreateWorkspaceResponse create_workspace(create_workspace_request)

Create Workspace

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import user_and_workspace_management_api
from pandadoc_client.model.create_workspace_request import CreateWorkspaceRequest
from pandadoc_client.model.create_workspace_response import CreateWorkspaceResponse
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host="https://api.pandadoc.com",
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key_prefix['apiKey'] = 'API-Key'

# Configure OAuth2 access token for authorization: oauth2
# configuration = pandadoc_client.Configuration(
#    host="https://api.pandadoc.com",
# )
# configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_and_workspace_management_api.UserAndWorkspaceManagementApi(api_client)
    create_workspace_request = CreateWorkspaceRequest(
        name="A new workspace",
    )  # CreateWorkspaceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Workspace
        api_response = api_instance.create_workspace(create_workspace_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling UserAndWorkspaceManagementApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)|  |

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

