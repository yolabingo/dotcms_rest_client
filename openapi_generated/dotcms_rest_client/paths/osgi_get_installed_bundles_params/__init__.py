# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dotcms_rest_client.paths.osgi_get_installed_bundles_params import Api

from dotcms_rest_client.paths import PathValues

path = PathValues.OSGI_GET_INSTALLED_BUNDLES_PARAMS