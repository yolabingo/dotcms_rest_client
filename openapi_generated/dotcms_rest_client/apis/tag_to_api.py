import typing_extensions

from dotcms_rest_client.apis.tags import TagValues
from dotcms_rest_client.apis.tags.workflow_api import WorkflowApi
from dotcms_rest_client.apis.tags.page_api import PageApi
from dotcms_rest_client.apis.tags.content_type_api import ContentTypeApi
from dotcms_rest_client.apis.tags.content_delivery_api import ContentDeliveryApi
from dotcms_rest_client.apis.tags.bundle_api import BundleApi
from dotcms_rest_client.apis.tags.navigation_api import NavigationApi
from dotcms_rest_client.apis.tags.experiment_api import ExperimentApi
from dotcms_rest_client.apis.tags.tail_log_api import TailLogApi
from dotcms_rest_client.apis.tags.default_api import DefaultApi

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
