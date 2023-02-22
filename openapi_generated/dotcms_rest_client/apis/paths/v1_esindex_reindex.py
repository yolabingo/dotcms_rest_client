from dotcms_rest_client.paths.v1_esindex_reindex.get import ApiForget
from dotcms_rest_client.paths.v1_esindex_reindex.post import ApiForpost
from dotcms_rest_client.paths.v1_esindex_reindex.delete import ApiFordelete


class V1EsindexReindex(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
