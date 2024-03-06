# pandadoc_client.QuotesApi

All URIs are relative to *https://api.pandadoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_update**](QuotesApi.md#quote_update) | **PUT** /public/v1/documents/{document_id}/quotes/{quote_id} | Quote update


# **quote_update**
> QuoteResponse quote_update(document_id, quote_id, quote_update_request)

Quote update

### Example

* Api Key Authentication (apiKey):
* OAuth Authentication (oauth2):

```python
import pandadoc_client
from pandadoc_client.api import quotes_api
from pandadoc_client.model.quote_update_request import QuoteUpdateRequest
from pandadoc_client.model.quote_response import QuoteResponse
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
    api_instance = quotes_api.QuotesApi(api_client)
    document_id = "BhVzRcxH9Z2LgfPPGXFUBa"  # str | Document ID
    quote_id = "99aaa4f9-3250-4f5b-a953-6d7bfc5d8c9e"  # str | Quote ID
    quote_update_request = QuoteUpdateRequest(
        sections=[
            UpdateIntegrationQuoteSection(
                id="id_example",
                name="Section name",
                items=[
                    UpdateIntegrationQuoteSectionItem(
                        id="id_example",
                        sku="#",
                        name="",
                        description="",
                        qty=10,
                        price=42.42,
                        price_settings=QuoteUpdateRequestPriceSettings(
                            base_value=3.14,
                            tiers=[
                                QuoteUpdateRequestPriceSettingsTiers(
                                    min_qty=1,
                                    value=3.14,
                                ),
                            ],
                        ),
                        cost=42.42,
                        billing_frequency="weekly",
                        contract_term=1,
                        reference_id="reference_id_example",
                        options=QuoteUpdateRequestOptions(
                            selected=True,
                            qty_editable=True,
                            optional=False,
                        ),
                        custom_columns={
                            "key": "key_example",
                        },
                        discounts={
                            "key": QuoteUpdateRequestDiscounts(
                                type="percent",
                                value=3.14,
                            ),
                        },
                        taxes={
                            "key": QuoteUpdateRequestDiscounts(
                                type="percent",
                                value=3.14,
                            ),
                        },
                        fees={
                            "key": QuoteUpdateRequestDiscounts(
                                type="percent",
                                value=3.14,
                            ),
                        },
                        multipliers={
                            "key": 3.14,
                        },
                    ),
                ],
                settings=QuoteUpdateRequestSettings(
                    optional=True,
                    selected=True,
                    selection_type="custom",
                ),
            ),
        ],
        settings=QuoteUpdateRequestSettings1(
            selection_type="custom",
        ),
    )  # QuoteUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Quote update
        api_response = api_instance.quote_update(document_id, quote_id, quote_update_request)
        pprint(api_response)
    except pandadoc_client.ApiException as e:
        print("Exception when calling QuotesApi->quote_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document ID |
 **quote_id** | **str**| Quote ID |
 **quote_update_request** | [**QuoteUpdateRequest**](QuoteUpdateRequest.md)|  |

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication error |  -  |
**403** | Permission error |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

