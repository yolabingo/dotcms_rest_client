from dotcms_rest_client.paths.vtl_folder.get import ApiForget
from dotcms_rest_client.paths.vtl_folder.put import ApiForput
from dotcms_rest_client.paths.vtl_folder.post import ApiForpost
from dotcms_rest_client.paths.vtl_folder.delete import ApiFordelete
from dotcms_rest_client.paths.vtl_folder.patch import ApiForpatch


class VtlFolder(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
