from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gko#le@t0c(+v!5e^rw)cpf0-0*tm%iq0v88a+1%mhc95!ithe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'algo.up.railway.app', 'algo.freewsad.com']

CSRF_TRUSTED_ORIGINS = ["https://algo.up.railway.app", "https://algo.freewsad.com/"]




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
    'users',
    'django_summernote',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'algo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'product.context_processors.context',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n'
                
            ],
        },
    },
]

WSGI_APPLICATION = 'algo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# Define the languages supported by the application.


# Set the default language.
LANGUAGE_CODE = 'fr-fr'

# Enable Django's translation system.
USE_I18N = True

# Enable localization (time zones and numbers).
USE_L10N = True

# Enable language-specific formatting of dates and times.
USE_TZ = True

# Define the path to the project's "locale" directory.
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


LANGUAGES = [
    ('fr', 'French'),
    ('ar', 'Arabic'),
 
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Media file
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Summernot Configuration
SUMMERNOTE_THEME = 'bs4'  # set the Summernote theme
SUMMERNOTE_CONFIG = {
    'width': '100%',
    'height': '400px',
}  # set the Summernote configuration options



if os.getcwd() == '/app':
    
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = 'DO004CNRT4BAPJMAR7QH'
    AWS_SECRET_ACCESS_KEY = 'ey7KOnDSCbMRLNValKv0mqV8TkID0WssTfHsW9mTRE4'
    AWS_STORAGE_BUCKET_NAME = 'agmir'
    AWS_S3_ENDPOINT_URL = 'https://agmir.nyc3.digitaloceanspaces.com'

    AWS_S3_CUSTOM_DOMAIN = 'agmir.nyc3.cdn.digitaloceanspaces.com/agmir'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'public'




    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.postgresql_psycopg2",
            'NAME': "railway",
            'USER': "postgres",
            'PASSWORD': "aAkmpW0rpwP07Fhi93nE",
            'HOST': "containers-us-west-34.railway.app",
            'PORT': "6145",
        }
    }
