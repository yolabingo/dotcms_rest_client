from openapi_client.paths.v1_containers.get import ApiForget
from openapi_client.paths.v1_containers.put import ApiForput
from openapi_client.paths.v1_containers.post import ApiForpost
from openapi_client.paths.v1_containers.delete import ApiFordelete


class V1Containers(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
