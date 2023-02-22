from openapi_client.paths.v1_categories.get import ApiForget
from openapi_client.paths.v1_categories.put import ApiForput
from openapi_client.paths.v1_categories.post import ApiForpost
from openapi_client.paths.v1_categories.delete import ApiFordelete


class V1Categories(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
