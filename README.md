# dotcms_rest_client
DotCMS python rest client, from openapi-generator https://github.com/openapitools/openapi-generator

To build 
```bash
git clone git@github.com:yolabingo/dotcms_rest_client.git
(cd dotcms_rest_client/openapi_generated && export DOTCMS_OPENAPI_GENERATED=`pwd`)
git clone https://github.com/OpenAPITools/openapi-generator.git 
(cd openapi-generator && mvn clean package && \
  java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar \
  generate \
  --skip-validate-spec \
  -i https://demo.dotcms.com/api/openapi.yaml \
  -g python \
  --api-package dotcms_rest_client \
  --package-name dotcms_rest_client \
  -o $DOTCMS_OPENAPI_GENERATED )
(cd $DOTCMS_OPENAPI_GENERATED && python setup.py bdist_wheel && pip wheel --no-deps -w ../dist .)
```
