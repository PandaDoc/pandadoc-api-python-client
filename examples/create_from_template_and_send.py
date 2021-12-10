from time import sleep

import pandadoc_client
from pandadoc_client.model.document_create_request_content_library_items import \
    DocumentCreateRequestContentLibraryItems
from pandadoc_client.model.document_create_request_content_placeholders import \
    DocumentCreateRequestContentPlaceholders
from pandadoc_client.model.document_create_request_images import DocumentCreateRequestImages
from pandadoc_client.model.document_create_by_template_request_tokens import \
    DocumentCreateByTemplateRequestTokens
from pandadoc_client.model.document_create_request_recipients import DocumentCreateRequestRecipients
from pandadoc_client.model.document_create_request import DocumentCreateRequest
from pandadoc_client.model.document_send_request import DocumentSendRequest
from pandadoc_client import ApiClient, Configuration
from pandadoc_client.api import documents_api
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


# place your api key here
API_KEY = 'YOUR_API_KEY'
#
# you should have an `Full API Sample Document from PandaDoc Template`
# onboarding template in your workspace just place its ID here
TEMPLATE_UUID = 'YOUR_TEMPLATE_UUID'
#
# you should have a several onboarding CLIs in your workspace
# just place an ID of any
CONTENT_LIBRARY_ITEM_ID = 'YOUR_CONTENT_LIBRARY_ITEM_ID'

MAX_CHECK_RETRIES = 5


def create_doc_from_sample_template(api_instance):
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

    document_create_request = DocumentCreateRequest(
        name='API Sample Document from PandaDoc Template',
        template_uuid=TEMPLATE_UUID,
        # specify a folder uuid if you want to document to be created
        # in specific folder otherwise it will be created in root directory
        #
        # folder_uuid='QMDSzwabfFzTgjW4kUijqQ',
        recipients=[
            DocumentCreateRequestRecipients(
                email='josh@example.com',
                first_name='Josh',
                last_name='Ron',
                role='user',
                signing_order=1,
            ),
        ],
        tokens=[DocumentCreateByTemplateRequestTokens(name='Favorite.Pet', value='Panda')],
        fields={},
        metadata={},
        tags=['created_via_api', 'test_document'],
        images=[
            DocumentCreateRequestImages(
                urls=[
                    'https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png',
                ],
                name='Image 1',
            ),
        ],
        pricing_tables=pricing_tables,
        content_placeholders=[
            DocumentCreateRequestContentPlaceholders(
                block_id='Content Placeholder 1',
                content_library_items=[
                    DocumentCreateRequestContentLibraryItems(
                        id=CONTENT_LIBRARY_ITEM_ID,
                        pricing_tables=pricing_tables,
                    ),
                ],
            ),
        ],
    )
    return api_instance.document_create(document_create_request=document_create_request)


def ensure_document_created(api_instance, document):
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

    retries = 0
    while retries < MAX_CHECK_RETRIES:
        sleep(2)
        retries += 1

        doc_status = api_instance.document_status(document['id'])
        if doc_status.status == 'document.draft':
            return

    raise RuntimeError('Document was not sent')


def send_document(api_instance, document):
    api_instance.send_document(
        document['id'],
        document_send_request=DocumentSendRequest(
            silent=False, subject='This doc was send via python SDK'
        ),
    )


def main():
    cfg = Configuration(api_key={'apiKey': f'API-Key {API_KEY}'})
    # Enter a context with an instance of the API client
    with ApiClient(cfg) as client:
        try:
            api_instance = documents_api.DocumentsApi(client)
            document = create_doc_from_sample_template(api_instance)
            print(f'Document was successfully uploaded:\n{document}')
            ensure_document_created(api_instance, document)
            send_document(api_instance, document)
            print(f'Document was successfully created and sent to the recipients!')
        except pandadoc_client.ApiException as e:
            print(f'{e.status} {e.reason} {e.body}')


if __name__ == '__main__':
    main()
