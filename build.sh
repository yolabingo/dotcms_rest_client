git clone git@github.com:yolabingo/dotcms_rest_client.git
cd dotcms_rest_client
export DOTCMS_OPENAPI_GENERATED="$(pwd)/openapi_generated"
pushd /var/tmp
git clone https://github.com/OpenAPITools/openapi-generator.git --depth 1
cd openapi-generator
mvn clean package 
curl -o dotcms_openapi.yaml https://dotcms-qa-lts2301.dotcms.site/api/openapi.yaml
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate \
    --skip-validate-spec \
    -i  dotcms_openapi.yaml \
    -g python \
    --api-package dotcms_rest_client \
    --package-name dotcms_rest_client \
    -o $DOTCMS_OPENAPI_GENERATED
cd $DOTCMS_OPENAPI_GENERATED && python setup.py bdist_wheel && pip wheel --no-deps -w ../dist .

