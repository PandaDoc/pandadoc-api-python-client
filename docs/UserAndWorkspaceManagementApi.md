# pandadoc_client.UserAndWorkspaceManagementApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](UserAndWorkspaceManagementApi.md#add_member) | **POST** /public/v1/workspaces/{workspace_id}/members | Add Member to Workspace
[**create_api_key**](UserAndWorkspaceManagementApi.md#create_api_key) | **POST** /public/v1/workspaces/{workspace_id}/api-keys | Create API Key
[**create_user**](UserAndWorkspaceManagementApi.md#create_user) | **POST** /public/v1/users | Create User
[**create_workspace**](UserAndWorkspaceManagementApi.md#create_workspace) | **POST** /public/v1/workspaces | Create Workspace
[**deactivate_workspace**](UserAndWorkspaceManagementApi.md#deactivate_workspace) | **POST** /public/v1/workspaces/{workspace_id}/deactivate | Deactivate Workspace
[**details_user**](UserAndWorkspaceManagementApi.md#details_user) | **GET** /public/v1/users/{user_id} | Get User Details by ID
[**get_workspaces_list**](UserAndWorkspaceManagementApi.md#get_workspaces_list) | **GET** /public/v1/workspaces | List Workspaces
[**list_users**](UserAndWorkspaceManagementApi.md#list_users) | **GET** /public/v1/users | List Users
[**remove_member**](UserAndWorkspaceManagementApi.md#remove_member) | **DELETE** /public/v1/workspaces/{workspace_id}/members/{member_id} | Remove Member from Workspace


# **add_member**
> AddMemberResponse add_member(workspace_id, add_member_request, notify_user=notify_user, notify_ws_admins=notify_ws_admins)

Add Member to Workspace

Add an existing user to a workspace.
- You must be an organization admin or a workspace admin to add members.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.add_member_request import AddMemberRequest
from pandadoc_client.models.add_member_response import AddMemberResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    workspace_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | 
    add_member_request = {"user_id":"2eWSKSvVqmuVCnuUK3iWwD","role":"Member"} # AddMemberRequest | 
    notify_user = true # bool | Send a confirmation email to the user that was added to workspace(s). (optional)
    notify_ws_admins = false # bool | Send a confirmation email to all workspace admins indicating that the user has been added to the workspace. (optional)

    try:
        # Add Member to Workspace
        api_response = api_instance.add_member(workspace_id, add_member_request, notify_user=notify_user, notify_ws_admins=notify_ws_admins)
        print("The response of UserAndWorkspaceManagementApi->add_member:\n")
        pprint(api_response)
    except Exception as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key**
> CreateApiKeyResponse create_api_key(workspace_id, create_api_key_request)

Create API Key

Generate a new API key for the workspace.
Check out [API Key Authentication article](https://developers.pandadoc.com/reference/api-key-authentication-process) for detailed API Keys description.

> 📘 
> - Only an **Org Admin** can generate an API keys.
> - To make another user a key's owner, pass `user_id` of this user. The user should has an **Admin** role in the workspace.
> - Generating a new key invalidates existing key with the same type. Using this request, you can deactivate the key you're using for the request.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_api_key_request import CreateApiKeyRequest
from pandadoc_client.models.create_api_key_response import CreateApiKeyResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    workspace_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Workspace id.
    create_api_key_request = {"type":"production","user_id":"ajnN7eGutJZsRKjQrNuPkh"} # CreateApiKeyRequest | 

    try:
        # Create API Key
        api_response = api_instance.create_api_key(workspace_id, create_api_key_request)
        print("The response of UserAndWorkspaceManagementApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAndWorkspaceManagementApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace id. | 
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> CreateUserResponse create_user(create_user_request, notify_user=notify_user, notify_ws_admins=notify_ws_admins)

Create User

Create users, and assign them roles, licenses, and workspaces.

- You must be an organization admin to create users.
- We check that the user email domain matches your organization domain.
- We check that the user email and phone number have a valid format.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_user_request import CreateUserRequest
from pandadoc_client.models.create_user_response import CreateUserResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    create_user_request = {"user":{"email":"test@pandadoc.com","first_name":"New","last_name":"User","phone_number":""},"workspaces":[{"workspace_id":"Ab123","role":"Collaborator"}],"license":"Guest"} # CreateUserRequest | 
    notify_user = true # bool | Send a confirmation email to the user that was added to workspace(s). (optional)
    notify_ws_admins = false # bool | Send a confirmation email to all workspace admins indicating that the user has been added to the workspace. (optional)

    try:
        # Create User
        api_response = api_instance.create_user(create_user_request, notify_user=notify_user, notify_ws_admins=notify_ws_admins)
        print("The response of UserAndWorkspaceManagementApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> CreateWorkspaceResponse create_workspace(create_workspace_request)

Create Workspace

Create a workspace in your organization.

- You need to be an Org Admin to create a workspace.
- You will be added to the new workspace with an Admin role.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.create_workspace_request import CreateWorkspaceRequest
from pandadoc_client.models.create_workspace_response import CreateWorkspaceResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    create_workspace_request = {"name":"A new workspace"} # CreateWorkspaceRequest | 

    try:
        # Create Workspace
        api_response = api_instance.create_workspace(create_workspace_request)
        print("The response of UserAndWorkspaceManagementApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_workspace**
> object deactivate_workspace(workspace_id, body=body)

Deactivate Workspace

Deactivate the workspace, remove all the members from it and make it 
unavailable.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    workspace_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | 
    body = {} # object |  (optional)

    try:
        # Deactivate Workspace
        api_response = api_instance.deactivate_workspace(workspace_id, body=body)
        print("The response of UserAndWorkspaceManagementApi->deactivate_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAndWorkspaceManagementApi->deactivate_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace was deactivated successfully. |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **details_user**
> GetUserResponse details_user(user_id)

Get User Details by ID

Get detailed information about a specific user by their ID, including contact information, license type, and workspace roles.

You must be an organization admin to get user details.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.get_user_response import GetUserResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    user_id = 'ajnN7eGutJZsRKjQrNuPkh' # str | A unique identifier of the user.

    try:
        # Get User Details by ID
        api_response = api_instance.details_user(user_id)
        print("The response of UserAndWorkspaceManagementApi->details_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAndWorkspaceManagementApi->details_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A unique identifier of the user. | 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User details. |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces_list**
> ListWorkspacesResponse get_workspaces_list(count=count, page=page)

List Workspaces

Get a list of all the active workspaces in the organization.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_workspaces_response import ListWorkspacesResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    count = 50 # int | Number of elements in page. (optional) (default to 50)
    page = 1 # int | Page number. (optional) (default to 1)

    try:
        # List Workspaces
        api_response = api_instance.get_workspaces_list(count=count, page=page)
        print("The response of UserAndWorkspaceManagementApi->get_workspaces_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAndWorkspaceManagementApi->get_workspaces_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of elements in page. | [optional] [default to 50]
 **page** | **int**| Page number. | [optional] [default to 1]

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page of workspaces |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users(count=count, page=page, show_removed=show_removed)

List Users

Get a list of all users with membership in your organization, with their contact information, license type, and workspace roles.

You must be an organization admin to list users.


### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.models.list_users_response import ListUsersResponse
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    count = 50 # int | Number of elements in page. (optional) (default to 50)
    page = 1 # int | Page number. (optional) (default to 1)
    show_removed = True # bool | Filter option - show users with removed memberships. (optional) (default to True)

    try:
        # List Users
        api_response = api_instance.list_users(count=count, page=page, show_removed=show_removed)
        print("The response of UserAndWorkspaceManagementApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAndWorkspaceManagementApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of elements in page. | [optional] [default to 50]
 **page** | **int**| Page number. | [optional] [default to 1]
 **show_removed** | **bool**| Filter option - show users with removed memberships. | [optional] [default to True]

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page of users. |  -  |
**401** | Authentication error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member**
> remove_member(workspace_id, member_id)

Remove Member from Workspace

This operation removes a specified member from a workspace by providing the workspace ID and member ID.

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pandadoc.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pandadoc_client.Configuration(
    host = "https://api.pandadoc.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pandadoc_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pandadoc_client.UserAndWorkspaceManagementApi(api_client)
    workspace_id = 'BhVzRcxH9Z2LgfPPGXFUBa' # str | Workspace id
    member_id = 'nPh2PDhFdDqAES9k64h9qX' # str | Member id

    try:
        # Remove Member from Workspace
        api_instance.remove_member(workspace_id, member_id)
    except Exception as e:
        print("Exception when calling UserAndWorkspaceManagementApi->remove_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace id | 
 **member_id** | **str**| Member id | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Bad Request |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

