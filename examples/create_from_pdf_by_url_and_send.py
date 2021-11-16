from time import sleep

import pandadoc_client
from pandadoc_client import ApiClient, Configuration
from pandadoc_client.api import documents_api
from pandadoc_client.model.document_send_request import DocumentSendRequest
from pandadoc_client.model.inline_object import InlineObject
from pandadoc_client.model.public_v1_documents_recipients import (
    PublicV1DocumentsRecipients,
)


# place your api key here
API_KEY = 'YOUR_API_KEY'
DOCUMENT_PDF_URL = 'https://cdn2.hubspot.net/hubfs/2127247/public-templates/SamplePandaDocPdf_FieldTags.pdf'

_MAX_RETRY_COUNT = 5


inline_obj = InlineObject(
    name='Sample Document from PDF with Field Tags',
    url=DOCUMENT_PDF_URL,
    tags=[
        'tag_1',
        'tag_2',
    ],
    recipients=[
        PublicV1DocumentsRecipients(
            email='josh@example.com',
            first_name='Josh',
            last_name='Ron',
            role='user',
            signing_order=1,
        ),
        PublicV1DocumentsRecipients(
            email='john@example.com',
            first_name='John',
            last_name='Doe',
            signing_order=2,
        ),
    ],
    fields={
        'name': {'value': 'John', 'role': 'user'},
        'like': {'value': True, 'role': 'user'},
    },
    metadata={'salesforce.opportunity_id': '123456', 'my_favorite_pet': 'Panda'},
    parse_form_fields=False,
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


def create_document_from_sample_template_pdf_url(client, inline_object):
    api_instance = documents_api.DocumentsApi(client)
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
        document = create_document_from_sample_template_pdf_url(client, inline_obj)
        send_document(client, document)


if __name__ == '__main__':
    main()
