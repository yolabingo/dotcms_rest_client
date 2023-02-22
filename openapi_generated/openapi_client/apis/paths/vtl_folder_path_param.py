from openapi_client.paths.vtl_folder_path_param.get import ApiForget
from openapi_client.paths.vtl_folder_path_param.put import ApiForput
from openapi_client.paths.vtl_folder_path_param.post import ApiForpost
from openapi_client.paths.vtl_folder_path_param.delete import ApiFordelete
from openapi_client.paths.vtl_folder_path_param.patch import ApiForpatch


class VtlFolderPathParam(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
