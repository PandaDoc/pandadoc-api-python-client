from time import sleep

import pandadoc_client
from pandadoc_client.model.document_send_request import DocumentSendRequest
from pandadoc_client import ApiClient, Configuration
from pandadoc_client.api import documents_api
from pandadoc_client.model.inline_object import InlineObject
from pandadoc_client.model.pricing_table_request import PricingTableRequest
from pandadoc_client.model.pricing_table_request_data import PricingTableRequestData
from pandadoc_client.model.pricing_table_request_data_discount import (
    PricingTableRequestDataDiscount,
)
from pandadoc_client.model.pricing_table_request_options import (
    PricingTableRequestOptions,
)
from pandadoc_client.model.pricing_table_request_options1 import (
    PricingTableRequestOptions1,
)
from pandadoc_client.model.pricing_table_request_options_discount import (
    PricingTableRequestOptionsDiscount,
)
from pandadoc_client.model.pricing_table_request_options_tax_first import (
    PricingTableRequestOptionsTaxFirst,
)
from pandadoc_client.model.pricing_table_request_options_tax_second import (
    PricingTableRequestOptionsTaxSecond,
)
from pandadoc_client.model.pricing_table_request_rows import PricingTableRequestRows
from pandadoc_client.model.pricing_table_request_sections import (
    PricingTableRequestSections,
)
from pandadoc_client.model.public_v1_documents_content_library_items import (
    PublicV1DocumentsContentLibraryItems,
)
from pandadoc_client.model.public_v1_documents_content_placeholders import (
    PublicV1DocumentsContentPlaceholders,
)
from pandadoc_client.model.public_v1_documents_images import PublicV1DocumentsImages
from pandadoc_client.model.public_v1_documents_recipients import (
    PublicV1DocumentsRecipients,
)
from pandadoc_client.model.public_v1_documents_tokens import PublicV1DocumentsTokens

# place your api key here
API_KEY = 'YOUR_API_KEY'
#
# you should have an `API Sample Document from PandaDoc Template`
# onboarding template in your workspace just place its ID here
TEMPLATE_UUID = 'YOUR_API_SAMPLE_TEMPLATE_ID'
#
# you should have a several onboarding CLIs in your workspace
# just place an ID of any
CONTENT_LIBRARY_ITEM_ID = 'YOUR_CLI_ID'

_MAX_RETRY_COUNT = 5


pricing_tables = [
    PricingTableRequest(
        name='Pricing Table 1',
        options=PricingTableRequestOptions(
            currency='USD',
            discount=PricingTableRequestOptionsDiscount(
                is_global=True,
                type='absolute',
                name='Global Discount',
                value=2.26,
            ),
            tax_first=PricingTableRequestOptionsTaxFirst(
                is_global=True,
                type='percent',
                name='Tax First',
                value=2.26,
            ),
            tax_second=PricingTableRequestOptionsTaxSecond(
                is_global=True,
                type='percent',
                name='Tax Second',
                value=2.26,
            ),
        ),
        sections=[
            PricingTableRequestSections(
                title='Sample Section',
                default=True,
                multichoice_enabled=False,
                rows=[
                    PricingTableRequestRows(
                        options=PricingTableRequestOptions1(
                            qty_editable=True,
                            optional_selected=True,
                            optional=True,
                        ),
                        data=PricingTableRequestData(
                            name='Toy Panda',
                            description='Fluffy!',
                            price=10.0,
                            cost=8.5,
                            qty=3,
                            sku='toy_panda',
                            discount=PricingTableRequestDataDiscount(
                                value=7.5,
                                type='percent',
                            ),
                            tax_first=PricingTableRequestDataDiscount(
                                value=7.5,
                                type='percent',
                            ),
                            tax_second=PricingTableRequestDataDiscount(
                                value=7.5,
                                type='percent',
                            ),
                        ),
                        custom_fields={},
                    ),
                ],
            ),
        ],
    ),
]

inline_obj = InlineObject(
    name='API Sample Document from PandaDoc Template',
    template_uuid=TEMPLATE_UUID,
    # specify a folder uuid if you want to document to be created
    # in specific folder otherwise it will be created in root directory
    #
    # folder_uuid='QMDSzwabfFzTgjW4kUijqQ',
    recipients=[
        PublicV1DocumentsRecipients(
            email='josh@example.com',
            first_name='Josh',
            last_name='Ron',
            role='user',
            signing_order=1,
        ),
    ],
    tokens=[PublicV1DocumentsTokens(name='Favorite.Pet', value='Panda')],
    fields={},
    metadata={},
    tags=['created_via_api', 'test_document'],
    images=[
        PublicV1DocumentsImages(
            urls=[
                'https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png',
            ],
            name='Image 1',
        ),
    ],
    pricing_tables=pricing_tables,
    content_placeholders=[
        PublicV1DocumentsContentPlaceholders(
            block_id='Content Placeholder 1',
            content_library_items=[
                PublicV1DocumentsContentLibraryItems(
                    id=CONTENT_LIBRARY_ITEM_ID,
                    pricing_tables=pricing_tables,
                ),
            ],
        ),
    ],
)


def send_document(api_client, document):
    api_instance = documents_api.DocumentsApi(api_client)

    # Document creation is non-blocking (asynchronous) operation.
    #
    # With a successful request, you receive a response with the created
    # document's ID and status document.uploaded.
    # After processing completes on our servers, usually a few seconds,
    # the document moves to the document.draft status.
    # Please wait for the webhook call or check this document's
    # status before proceeding.
    #
    # The change of status from document.uploaded to another status signifies
    # the document is ready for further processing.
    # Attempting to use a newly created document before PandaDoc servers
    # process it will result in a '404 document not found' response.
    doc_status, retries = document['status'], _MAX_RETRY_COUNT
    while doc_status != 'document.draft' and retries > 0:
        try:
            doc_status = api_instance.document_status(document['id'])
        except pandadoc_client.ApiException as e:
            print(f'Exception when calling DocumentsApi->document_status: \n{e}')
        retries -= 1
        sleep(2)

    try:
        sent = api_instance.send_document(
            document['id'],
            document_send_request=DocumentSendRequest(
                silent=False, subject='This doc was send via python SDK'
            ),
        )
        print(f'Document was sent: \n{sent}')
        return sent
    except pandadoc_client.ApiException as e:
        print(f'Exception when calling DocumentsApi->send_document: \n{e}')


def create_doc_from_sample_template(api_client, inline_object):
    api_instance = documents_api.DocumentsApi(api_client)
    try:
        created_doc = api_instance.document_create(inline_object=inline_object)
        print(f'Document was created: \n{created_doc}')
        return created_doc
    except pandadoc_client.ApiException as e:
        print(f'Exception when calling DocumentsApi->document_create: \n{e}')
        raise e


def main():
    cfg = Configuration(api_key={'apiKey': f'API-Key {API_KEY}'})
    # Enter a context with an instance of the API client
    with ApiClient(cfg) as client:
        document = create_doc_from_sample_template(client, inline_obj)
        send_document(client, document)


if __name__ == '__main__':
    main()
