from dotcms_rest_client.paths.v1_redis_key.get import ApiForget
from dotcms_rest_client.paths.v1_redis_key.delete import ApiFordelete


class V1RedisKey(
    ApiForget,
    ApiFordelete,
):
    pass
