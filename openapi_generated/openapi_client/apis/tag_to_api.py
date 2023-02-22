import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.workflow_api import WorkflowApi
from openapi_client.apis.tags.page_api import PageApi
from openapi_client.apis.tags.content_type_api import ContentTypeApi
from openapi_client.apis.tags.content_delivery_api import ContentDeliveryApi
from openapi_client.apis.tags.bundle_api import BundleApi
from openapi_client.apis.tags.navigation_api import NavigationApi
from openapi_client.apis.tags.experiment_api import ExperimentApi
from openapi_client.apis.tags.tail_log_api import TailLogApi
from openapi_client.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.PAGE: PageApi,
        TagValues.CONTENT_TYPE: ContentTypeApi,
        TagValues.CONTENT_DELIVERY: ContentDeliveryApi,
        TagValues.BUNDLE: BundleApi,
        TagValues.NAVIGATION: NavigationApi,
        TagValues.EXPERIMENT: ExperimentApi,
        TagValues.TAIL_LOG: TailLogApi,
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.PAGE: PageApi,
        TagValues.CONTENT_TYPE: ContentTypeApi,
        TagValues.CONTENT_DELIVERY: ContentDeliveryApi,
        TagValues.BUNDLE: BundleApi,
        TagValues.NAVIGATION: NavigationApi,
        TagValues.EXPERIMENT: ExperimentApi,
        TagValues.TAIL_LOG: TailLogApi,
        TagValues.DEFAULT: DefaultApi,
    }
)
