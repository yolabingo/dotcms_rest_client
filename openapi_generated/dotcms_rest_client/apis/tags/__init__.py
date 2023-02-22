# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dotcms_rest_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    WORKFLOW = "Workflow"
    PAGE = "Page"
    CONTENT_TYPE = "Content Type"
    CONTENT_DELIVERY = "Content Delivery"
    BUNDLE = "Bundle"
    NAVIGATION = "Navigation"
    EXPERIMENT = "Experiment"
    TAIL_LOG = "TailLog"
    DEFAULT = "default"
