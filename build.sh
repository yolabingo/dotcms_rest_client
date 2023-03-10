#!/bin/bash 

DOTCMS_VERSION="23.01"
DOTCMS_URL="https://dotcms-qa-lts2301.dotcms.site/api/openapi.yaml"

export DOTCMS_OPENAPI_GENERATED="$(pwd)/openapi_generated"
pushd /var/tmp
if [ ! -d openapi-generator ]
then
    git clone https://github.com/OpenAPITools/openapi-generator.git --depth 1
fi

cd openapi-generator

if [ ! -f modules/openapi-generator-cli/target/openapi-generator-cli.jar ]
then
    mvn clean package
fi

# fetch dotcms openapi spec
# curl -o dotcms_openapi.yaml $DOTCMS_URL

# generate python client
java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar \
    generate \
    --global-property skipFormModel=false \
    --skip-validate-spec \
    -i  dotcms_openapi.yaml \
    -g python \
    -o $DOTCMS_OPENAPI_GENERATED

# --package-name dotcms_rest_client \
# --api-package dotcms_rest_client \

cd /var/tmp
# create python venv
python -m venv dotcms_openapi_generated
. dotcms_openapi_generated/bin/activate
pip install -U pip
pip install wheel
cd $DOTCMS_OPENAPI_GENERATED

## TODO: find and fix this in the python openapi-generator template
# touch openapi_generated/dotcms_rest_client/dotcms_rest_client/tags/__init__.py

sed -i '' 's/No description provided/DotCMS Rest Client/' setup.py
sed -i '' 's/No description provided/DotCMS Rest Client/' README.md
sed -i '' "s/^VERSION.*/VERSION = '$DOTCMS_VERSION'/" setup.py
python setup.py bdist_wheel
pip wheel --no-deps -w ../dist . && rm -rf build dist
deactivate
pushd
