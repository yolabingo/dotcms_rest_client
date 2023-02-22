from dotcms_rest_client.paths.v1_templates.get import ApiForget
from dotcms_rest_client.paths.v1_templates.put import ApiForput
from dotcms_rest_client.paths.v1_templates.post import ApiForpost
from dotcms_rest_client.paths.v1_templates.delete import ApiFordelete


class V1Templates(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
