# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django_heroku
# import psycopg2
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# DATABASE_URL = os.environ['DATABASE_URL']
#
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ocvjf&p1d%!))e)dpp_uu39s-+=)w&!*oc$vl48o@n*_1fh%2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATE_INPUT_FORMATS = ['%d-%m-%Y']

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# Application definition

INSTALLED_APPS = (
    'bcp',
    'cupom',
    'participante',
    'lojista',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django_filters',
    'bootstrap4',
    'sorl.thumbnail',
    'djng',
    'storages',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'liquida2018.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'liquida2018.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'liquidateresina2018',
        'USER': 'liquida2018',
        'PASSWORD': 'solution',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'liquidateresina2018',
#         'USER': 'liquida2018',
#         'PASSWORD': 'solution',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AWS_ACCESS_KEY_ID = 'AKIAJJARDFZKGWDDQ25Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'liquidateresina2018'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

DEFAULT_FILE_STORAGE = 'liquida2018.storage_backends.MediaStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_URL = '/static/'
# #STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'),]
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp')

FORM_RENDERER = 'djng.forms.renderers.DjangoAngularBootstrap3Templates'

from django.urls import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('participante:dashboard')
LOGIN_URL = reverse_lazy('participante:login')
LOGOUT_URL = reverse_lazy('participante:logout')

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('participante:editdocfiscal', args=[u.nomedocumento])
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# python-social-auth settings
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',

    'django.contrib.auth.backends.ModelBackend',
    'participante.authentication.EmailAuthBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '340442496482403'
SOCIAL_AUTH_FACEBOOK_SECRET = '8c550fd5dd91ec4ebce457a00afea8ea'

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

# import dj_database_url
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)






django_heroku.settings(locals())
