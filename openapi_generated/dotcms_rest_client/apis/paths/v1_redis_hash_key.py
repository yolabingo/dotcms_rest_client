from dotcms_rest_client.paths.v1_redis_hash_key.get import ApiForget
from dotcms_rest_client.paths.v1_redis_hash_key.delete import ApiFordelete


class V1RedisHashKey(
    ApiForget,
    ApiFordelete,
):
    pass
