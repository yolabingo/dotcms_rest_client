# coding: utf-8

"""
    dotCMS REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from dotcms_rest_client.paths.v1_page_page_id_content.post import AddContent
from dotcms_rest_client.paths.v1_page_copy_content.put import CopyContent
from dotcms_rest_client.paths.v1_page_page_id__deepcopy.put import DeepCopyPage
from dotcms_rest_client.paths.v1_page_page_id_content_tree.get import GetContentTree
from dotcms_rest_client.paths.v1_page_page_id_render_versions.get import GetHtmlVersionsPage
from dotcms_rest_client.paths.v1_page_page_id_personas.get import GetPersonalizedPersonasOnPage
from dotcms_rest_client.paths.v1_page_json_uri.get import LoadJson2
from dotcms_rest_client.paths.v1_page_render_uri.get import Render
from dotcms_rest_client.paths.v1_page_render_html_uri.get import RenderHtmlOnly
from dotcms_rest_client.paths.v1_page_layout.post import SaveLayout
from dotcms_rest_client.paths.v1_page_page_id_layout.post import SaveLayout1
from dotcms_rest_client.paths.v1_page_search.get import SearchPage


class PageApi(
    AddContent,
    CopyContent,
    DeepCopyPage,
    GetContentTree,
    GetHtmlVersionsPage,
    GetPersonalizedPersonasOnPage,
    LoadJson2,
    Render,
    RenderHtmlOnly,
    SaveLayout,
    SaveLayout1,
    SearchPage,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass