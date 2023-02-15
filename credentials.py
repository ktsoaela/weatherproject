import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Openweather Map API Key
OPENAPIKEY = '49cc8c821cd2aff9af04c9f98c36eb74'
MAPBOXKEY = 'pk.eyJ1Ijoia3Rzb2FlbGEiLCJhIjoiY2xlNHFldTluMDJnMDN2cGdibWdsZmsxcSJ9._9ZtTK1RElmTIBMSJlSzag'


# SETTINGS
CRED_SECRET_KEY = '0%fv-pe=cx!uw&)13rcb8$bb7i(%iwflt#v()u_w9t%3eo#sy('

CRED_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# CRED_DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'weatherproject',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': '',
#     }
# }