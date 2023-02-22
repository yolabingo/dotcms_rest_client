# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dotcms_rest_client.paths.osgi__process_exports_bundle import Api

from dotcms_rest_client.paths import PathValues

path = PathValues.OSGI__PROCESS_EXPORTS_BUNDLE