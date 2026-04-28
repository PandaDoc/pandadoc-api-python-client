from time import sleep

from pandadoc_client import (
    ApiClient,
    Configuration,
    ApiException,
    DocumentCreateRequest,
    DocumentCreateRequestOneOf,
    CreateDocumentActor,
    CreateDocumentRecipient,
    DocumentCreateByTemplateRequestTokensInner,
    DocumentCreateByTemplateRequestImagesInner,
    PricingTableRequest,
    PricingTableRequestRowOptions,
    PricingTableRequestSectionsInnerRowsInner,
    PricingTableRequestSectionsInner,
    DocumentCreateByTemplateRequestContentPlaceholdersInner,
    DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner,
    DocumentCreateResponse,
    DocumentSendRequest,
)
from pandadoc_client.api import documents_api


# Place your api key here
API_KEY = "YOUR_API_KEY"
# You should have an `Full API Sample Document from PandaDoc Template` 
# onboarding template in your workspace just place its ID here
TEMPLATE_UUID = "YOUR_TEMPLATE_UUID"
# You should have a several onboarding CLIs in your workspace
# just place an ID of any
CONTENT_LIBRARY_ITEM_ID = "YOUR_CONTENT_LIBRARY_ITEM_ID"

MAX_CHECK_RETRIES = 5


def create_doc_from_sample_template(api_instance) -> DocumentCreateResponse:

    pricing_tables = [
        PricingTableRequest(
            name="Pricing Table 1",
            data_merge=False,
            options={
                "Discount": {
                    "type": "absolute",
                    "name": "Global Discount",
                    "value": 10,
                },
                "Tax": {"type": "percent", "name": "Tax First", "value": 15},
            },
            sections=[
                PricingTableRequestSectionsInner(
                    title="Sample Section",
                    default=True,
                    multichoice_enabled=False,
                    rows=[
                        PricingTableRequestSectionsInnerRowsInner(
                            options=PricingTableRequestRowOptions(
                                qty_editable=True,
                                optional_selected=True,
                                optional=True,
                            ),
                            data={
                                "name": "Toy Panda",
                                "Description": "Fluffy",
                                "price": 10,
                                "Cost": 8.5,
                                "qty": 3,
                                "SKU": "toy_panda",
                                "Discount": {"value": 10, "type": "percent"},
                                "Tax": {"value": 10, "type": "percent"},
                            },
                        ),
                    ],
                ),
            ],
        ),
    ]

    document_create_request = DocumentCreateRequestOneOf(
        name="API Sample Document from PandaDoc Template",
        template_uuid=TEMPLATE_UUID,
        # specify a folder uuid if you want to document to be created
        # in specific folder otherwise it will be created in root directory
        # i.e. folder_uuid='QMDSzwabfFzTgjW4kUijqQ',
        recipients=[
            CreateDocumentActor(
                actual_instance=CreateDocumentRecipient(
                    email="josh@example.com",
                    first_name="Josh",
                    last_name="Ron",
                    role="user",
                    signing_order=1,
                )
            )
        ],
        tokens=[
            DocumentCreateByTemplateRequestTokensInner(
                name="Favorite.Pet", value="Panda"
            ),
        ],
        tags=[
            "created_via_api",
            "created_via_python_sdk",
            "test_document",
        ],
        images=[
            DocumentCreateByTemplateRequestImagesInner(
                urls=[
                    "https://s3.amazonaws.com/pd-static-content/public-docs/pandadoc-panda-bear.png",
                ],
                name="Image 1",
            ),
        ],
        pricing_tables=pricing_tables,
        content_placeholders=[
            DocumentCreateByTemplateRequestContentPlaceholdersInner(
                block_id="Content Placeholder 1",
                content_library_items=[
                    DocumentCreateByTemplateRequestContentPlaceholdersInnerContentLibraryItemsInner(
                        id=CONTENT_LIBRARY_ITEM_ID,
                        pricing_tables=pricing_tables,
                    ),
                ],
            ),
        ],
    )
    return api_instance.create_document(
        document_create_request=DocumentCreateRequest(document_create_request)
    )


def ensure_document_created(api_instance, document_id):
    """
    Document creation is non-blocking (asynchronous) operation.

    With a successful request, you receive a response with the created
    document's ID and status document.uploaded.
    After processing completes on our servers, usually a few seconds,
    the document moves to the document.draft status.
    Please wait for the webhook call or check this document's
    status before proceeding.

    The change of status from document.uploaded to another status signifies
    the document is ready for further processing.
    Attempting to use a newly created document before PandaDoc servers
    process it will result in a '404 document not found' response.
    """

    retries = 0
    while retries < MAX_CHECK_RETRIES:
        sleep(2)
        retries += 1

        doc_status = api_instance.status_document(document_id)
        if doc_status.status == "document.draft":
            return

    raise RuntimeError("Document was not sent")


def send_document(api_instance, document_id):
    api_instance.send_document(
        document_id,
        document_send_request=DocumentSendRequest(
            subject="This doc was send via python SDK",
            silent=False,
        ),
    )


def main():
    cfg = Configuration(api_key={'apiKey': f'API-Key {API_KEY}'})
    # Enter a context with an instance of the API client
    with ApiClient(cfg) as client:
        try:
            api_instance = documents_api.DocumentsApi(client)
            document_response: DocumentCreateResponse = create_doc_from_sample_template(
                api_instance
            )
            print(f"Document was successfully uploaded:\n{document_response}")
            ensure_document_created(api_instance, document_response.id)
            print(f"Document was successfully created and is in draft status.")
            send_document(api_instance, document_response.id)
            print(f"Document was successfully created and sent to the recipients!")
        except ApiException as e:
            print(f"{e.status} {e.reason} {e.body}")


if __name__ == "__main__":
    main()
