# dotcms_rest_client.model.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modificationDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**fullName** | str,  | str,  |  | [optional] 
**[locale](#locale)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[timeZone](#timeZone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**defaultUser** | bool,  | BoolClass,  |  | [optional] 
**companyId** | str,  | str,  |  | [optional] 
**actualCompanyId** | str,  | str,  |  | [optional] 
**passwordExpired** | bool,  | BoolClass,  |  | [optional] 
**female** | bool,  | BoolClass,  |  | [optional] 
**languageId** | str,  | str,  |  | [optional] 
**timeZoneId** | str,  | str,  |  | [optional] 
**resolution** | str,  | str,  |  | [optional] 
**refreshRate** | str,  | str,  |  | [optional] 
**recipientId** | str,  | str,  |  | [optional] 
**recipientName** | str,  | str,  |  | [optional] 
**recipientAddress** | str,  | str,  |  | [optional] 
**recipientInternetAddress** | str,  | str,  |  | [optional] 
**multipleRecipients** | bool,  | BoolClass,  |  | [optional] 
**anonymousUser** | bool,  | BoolClass,  |  | [optional] 
**userRole** | [**Role**](Role.md) | [**Role**](Role.md) |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**firstName** | str,  | str,  |  | [optional] 
**lastName** | str,  | str,  |  | [optional] 
**emailAddress** | str,  | str,  |  | [optional] 
**userId** | str,  | str,  |  | [optional] 
**[additionalInfo](#additionalInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**passwordExpirationDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**middleName** | str,  | str,  |  | [optional] 
**male** | bool,  | BoolClass,  |  | [optional] 
**skinId** | str,  | str,  |  | [optional] 
**createDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**loginDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**loginIP** | str,  | str,  |  | [optional] 
**lastLoginDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastLoginIP** | str,  | str,  |  | [optional] 
**failedLoginAttempts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**agreedToTermsOfUse** | bool,  | BoolClass,  |  | [optional] 
**active** | bool,  | BoolClass,  |  | [optional] 
**birthday** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**comments** | str,  | str,  |  | [optional] 
**nickName** | str,  | str,  |  | [optional] 
**deleteInProgress** | bool,  | BoolClass,  |  | [optional] 
**deleteDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**passwordReset** | bool,  | BoolClass,  |  | [optional] 
**passwordEncrypted** | bool,  | BoolClass,  |  | [optional] 
**smsId** | str,  | str,  |  | [optional] 
**aimId** | str,  | str,  |  | [optional] 
**icqId** | str,  | str,  |  | [optional] 
**msnId** | str,  | str,  |  | [optional] 
**ymId** | str,  | str,  |  | [optional] 
**favoriteActivity** | str,  | str,  |  | [optional] 
**favoriteBibleVerse** | str,  | str,  |  | [optional] 
**favoriteFood** | str,  | str,  |  | [optional] 
**favoriteMovie** | str,  | str,  |  | [optional] 
**favoriteMusic** | str,  | str,  |  | [optional] 
**dottedSkins** | bool,  | BoolClass,  |  | [optional] 
**roundedSkins** | bool,  | BoolClass,  |  | [optional] 
**greeting** | str,  | str,  |  | [optional] 
**layoutIds** | str,  | str,  |  | [optional] 
**new** | bool,  | BoolClass,  |  | [optional] 
**modified** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locale

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  |  | [optional] 
**script** | str,  | str,  |  | [optional] 
**country** | str,  | str,  |  | [optional] 
**variant** | str,  | str,  |  | [optional] 
**[extensionKeys](#extensionKeys)** | list, tuple,  | tuple,  |  | [optional] 
**[unicodeLocaleAttributes](#unicodeLocaleAttributes)** | list, tuple,  | tuple,  |  | [optional] 
**[unicodeLocaleKeys](#unicodeLocaleKeys)** | list, tuple,  | tuple,  |  | [optional] 
**iso3Language** | str,  | str,  |  | [optional] 
**iso3Country** | str,  | str,  |  | [optional] 
**displayLanguage** | str,  | str,  |  | [optional] 
**displayScript** | str,  | str,  |  | [optional] 
**displayCountry** | str,  | str,  |  | [optional] 
**displayVariant** | str,  | str,  |  | [optional] 
**language** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extensionKeys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# unicodeLocaleAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# unicodeLocaleKeys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# timeZone

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayName** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**rawOffset** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**dstsavings** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# additionalInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

