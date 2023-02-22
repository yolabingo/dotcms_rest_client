from dotcms_rest_client.paths.v1_categories.get import ApiForget
from dotcms_rest_client.paths.v1_categories.put import ApiForput
from dotcms_rest_client.paths.v1_categories.post import ApiForpost
from dotcms_rest_client.paths.v1_categories.delete import ApiFordelete


class V1Categories(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
