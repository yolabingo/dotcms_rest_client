from dotcms_rest_client.paths.vtl_dynamic_path_param.get import ApiForget
from dotcms_rest_client.paths.vtl_dynamic_path_param.put import ApiForput
from dotcms_rest_client.paths.vtl_dynamic_path_param.post import ApiForpost
from dotcms_rest_client.paths.vtl_dynamic_path_param.delete import ApiFordelete
from dotcms_rest_client.paths.vtl_dynamic_path_param.patch import ApiForpatch


class VtlDynamicPathParam(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
