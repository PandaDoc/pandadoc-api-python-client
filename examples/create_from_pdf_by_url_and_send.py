from time import sleep

from pandadoc_client import (
    ApiClient,
    Configuration,
    ApiException,
    DocumentCreateRequest,
    DocumentCreateRequestOneOf1,
    CreateDocumentActor,
    CreateDocumentRecipient,
    DocumentCreateByTemplateRequestFieldsValue,
    DocumentCreateByTemplateRequestFieldsValueValue,
    DocumentCreateResponse,
    DocumentSendRequest,
)
from pandadoc_client.api import documents_api

# place your api key here
API_KEY = 'YOUR_API_KEY'
DOCUMENT_PDF_URL = "https://cdn2.hubspot.net/hubfs/2127247/public-templates/SamplePandaDocPdf_FieldTags.pdf"
MAX_CHECK_RETRIES = 5


def create_document_from_sample_template_pdf_url(
    api_instance,
) -> DocumentCreateResponse:
    document_create_request = DocumentCreateRequestOneOf1(
        name="Sample Document from PDF with Field Tags",
        url=DOCUMENT_PDF_URL,
        recipients=[
            CreateDocumentActor(
                actual_instance=CreateDocumentRecipient(
                    email='josh@example.com',
                    first_name="Josh",
                    last_name="Ron",
                    role="user",
                    signing_order=1,
                )
            ),
            CreateDocumentActor(
                actual_instance=CreateDocumentRecipient(
                    email='john@example.com',
                    first_name="John",
                    last_name="Doe",
                    signing_order=2,
                )
            ),
        ],
        fields={
            "name": DocumentCreateByTemplateRequestFieldsValue(
                value=DocumentCreateByTemplateRequestFieldsValueValue("John"),
                role="user",
            ),
            "like": DocumentCreateByTemplateRequestFieldsValue(
                value=DocumentCreateByTemplateRequestFieldsValueValue(True),
                role="user",
            ),
        },
        tags=[
            "created_via_api",
            "created_via_python_sdk",
            "test_document",
        ],
        metadata={"salesforce.opportunity_id": "123456", "my_favorite_pet": "Panda"},
        parse_form_fields=False,
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
    cfg = Configuration(api_key={"apiKey": f"API-Key {API_KEY}"})
    # Enter a context with an instance of the API client
    with ApiClient(cfg) as client:
        try:
            api_instance = documents_api.DocumentsApi(client)
            document_response = create_document_from_sample_template_pdf_url(
                api_instance
            )
            print(f"Document was successfully uploaded:\n{document_response}")
            ensure_document_created(api_instance, document_response.id)
            send_document(api_instance, document_response.id)
            print(f"Document was successfully created and sent to the recipients!")
        except ApiException as e:
            print(f"{e.status} {e.reason} {e.body}")


if __name__ == "__main__":
    main()
