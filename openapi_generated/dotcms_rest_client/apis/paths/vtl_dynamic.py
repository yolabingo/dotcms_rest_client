from dotcms_rest_client.paths.vtl_dynamic.get import ApiForget
from dotcms_rest_client.paths.vtl_dynamic.put import ApiForput
from dotcms_rest_client.paths.vtl_dynamic.post import ApiForpost


class VtlDynamic(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
