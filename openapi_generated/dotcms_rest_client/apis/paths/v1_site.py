from dotcms_rest_client.paths.v1_site.get import ApiForget
from dotcms_rest_client.paths.v1_site.put import ApiForput
from dotcms_rest_client.paths.v1_site.post import ApiForpost


class V1Site(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
