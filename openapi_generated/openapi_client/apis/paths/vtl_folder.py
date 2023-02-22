from openapi_client.paths.vtl_folder.get import ApiForget
from openapi_client.paths.vtl_folder.put import ApiForput
from openapi_client.paths.vtl_folder.post import ApiForpost
from openapi_client.paths.vtl_folder.delete import ApiFordelete
from openapi_client.paths.vtl_folder.patch import ApiForpatch


class VtlFolder(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
