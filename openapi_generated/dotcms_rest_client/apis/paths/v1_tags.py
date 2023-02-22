from dotcms_rest_client.paths.v1_tags.get import ApiForget
from dotcms_rest_client.paths.v1_tags.put import ApiForput
from dotcms_rest_client.paths.v1_tags.post import ApiForpost


class V1Tags(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
