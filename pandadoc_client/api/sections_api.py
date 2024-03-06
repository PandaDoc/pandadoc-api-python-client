"""
    PandaDoc Public API

    PandaDoc Public API documentation  # noqa: E501

    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pandadoc_client.api_client import ApiClient, Endpoint as _Endpoint
from pandadoc_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pandadoc_client.model.section_info_response import SectionInfoResponse
from pandadoc_client.model.upload_section_list_response import UploadSectionListResponse
from pandadoc_client.model.upload_section_request import UploadSectionRequest
from pandadoc_client.model.upload_section_response import UploadSectionResponse
from pandadoc_client.model.upload_section_status_response import UploadSectionStatusResponse


class SectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_sections_endpoint = _Endpoint(
            settings={
                'response_type': (UploadSectionListResponse,),
                'auth': [
                    'apiKey',
                    'oauth2'
                ],
                'endpoint_path': '/public/v1/documents/{document_id}/sections',
                'operation_id': 'list_sections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_id',
                ],
                'required': [
                    'document_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_id':
                        (str,),
                },
                'attribute_map': {
                    'document_id': 'document_id',
                },
                'location_map': {
                    'document_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.section_details_endpoint = _Endpoint(
            settings={
                'response_type': (UploadSectionStatusResponse,),
                'auth': [
                    'apiKey',
                    'oauth2'
                ],
                'endpoint_path': '/public/v1/documents/{document_id}/sections/uploads/{upload_id}',
                'operation_id': 'section_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_id',
                    'upload_id',
                ],
                'required': [
                    'document_id',
                    'upload_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_id':
                        (str,),
                    'upload_id':
                        (str,),
                },
                'attribute_map': {
                    'document_id': 'document_id',
                    'upload_id': 'upload_id',
                },
                'location_map': {
                    'document_id': 'path',
                    'upload_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.section_info_endpoint = _Endpoint(
            settings={
                'response_type': (SectionInfoResponse,),
                'auth': [
                    'apiKey',
                    'oauth2'
                ],
                'endpoint_path': '/public/v1/documents/{document_id}/sections/{section_id}',
                'operation_id': 'section_info',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_id',
                    'section_id',
                ],
                'required': [
                    'document_id',
                    'section_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_id':
                        (str,),
                    'section_id':
                        (str,),
                },
                'attribute_map': {
                    'document_id': 'document_id',
                    'section_id': 'section_id',
                },
                'location_map': {
                    'document_id': 'path',
                    'section_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.upload_section_endpoint = _Endpoint(
            settings={
                'response_type': (UploadSectionResponse,),
                'auth': [
                    'apiKey',
                    'oauth2'
                ],
                'endpoint_path': '/public/v1/documents/{document_id}/sections/uploads',
                'operation_id': 'upload_section',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_id',
                    'upload_section_request',
                ],
                'required': [
                    'document_id',
                    'upload_section_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_id':
                        (str,),
                    'upload_section_request':
                        (UploadSectionRequest,),
                },
                'attribute_map': {
                    'document_id': 'document_id',
                },
                'location_map': {
                    'document_id': 'path',
                    'upload_section_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def list_sections(
        self,
        document_id,
        **kwargs
    ):
        """List sections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_sections(document_id, async_req=True)
        >>> result = thread.get()

        Args:
            document_id (str): Document ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UploadSectionListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['document_id'] = \
            document_id
        return self.list_sections_endpoint.call_with_http_info(**kwargs)

    def section_details(
        self,
        document_id,
        upload_id,
        **kwargs
    ):
        """Section details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.section_details(document_id, upload_id, async_req=True)
        >>> result = thread.get()

        Args:
            document_id (str): Document ID
            upload_id (str): Upload ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UploadSectionStatusResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['document_id'] = \
            document_id
        kwargs['upload_id'] = \
            upload_id
        return self.section_details_endpoint.call_with_http_info(**kwargs)

    def section_info(
        self,
        document_id,
        section_id,
        **kwargs
    ):
        """Section Info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.section_info(document_id, section_id, async_req=True)
        >>> result = thread.get()

        Args:
            document_id (str): Document ID
            section_id (str): Section ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            SectionInfoResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['document_id'] = \
            document_id
        kwargs['section_id'] = \
            section_id
        return self.section_info_endpoint.call_with_http_info(**kwargs)

    def upload_section(
        self,
        document_id,
        upload_section_request,
        **kwargs
    ):
        """Upload section  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_section(document_id, upload_section_request, async_req=True)
        >>> result = thread.get()

        Args:
            document_id (str): Document ID
            upload_section_request (UploadSectionRequest): Use a PandaDoc template or an existing PDF to upload a section. See the creation request examples [by template](/schemas/UploadSectionByTemplateRequest) and [by pdf](/schemas/UploadSectionByPdfRequest) 

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UploadSectionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['document_id'] = \
            document_id
        kwargs['upload_section_request'] = \
            upload_section_request
        return self.upload_section_endpoint.call_with_http_info(**kwargs)
