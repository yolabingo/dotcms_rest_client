from openapi_client.paths.v1_templates.get import ApiForget
from openapi_client.paths.v1_templates.put import ApiForput
from openapi_client.paths.v1_templates.post import ApiForpost
from openapi_client.paths.v1_templates.delete import ApiFordelete


class V1Templates(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
