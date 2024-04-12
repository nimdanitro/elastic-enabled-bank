"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# Specify the demo user that all views will filter on
DEMO_USER_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap4'
TRANSACTION_INDEX_NAME = 'search-bank-project-transactions_v1'
TRANSACTION_PIPELINE_NAME = 'ml-inference-search-bank-project-transactions_v1'
MODEL_ID = '.elser_model_2_linux-x86_64'
PRODUCT_INDEX = 'banking-products'
PRODUCT_INDEX_PIPELINE_NAME = 'ml-inference-search-bank-project-transactions_v1'
CUSTOMER_SUPPORT_INDEX = 'search-customer-support'
LLM_AUDIT_LOG_INDEX = 'llm-audit-log'
LLM_AUDIT_LOG_INDEX_PIPELINE_NAME = 'ml-inference-sentiment'
LLM_PROVIDER = 'azure'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']
TRANSFORMER_MODEL = os.environ['TRANSFORMER_MODEL']
openai_api_key = os.environ['openai_api_key']
openai_api_type = os.environ['openai_api_type']
openai_api_base = os.environ['openai_api_base']
openai_api_version = os.environ['openai_api_version']

aws_access_key = os.environ['aws_access_key']
aws_secret_key = os.environ['aws_secret_key']
aws_region = os.environ['aws_region']
aws_model_id = os.environ['aws_model_id']

elastic_cloud_id = os.environ['ELASTIC_CLOUD_ID']
elastic_user = os.environ['ELASTIC_USER']
elastic_password = os.environ['ELASTIC_PASSWORD']
elastic_api_key = os.environ['ELASTIC_API_KEY']
kibana_url = os.environ['KIBANA_URL']


# SECURITY WARNING: don't run with debug turned on in production!§
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'public',
    'onlinebanking',
    'envmanager',
    'markdownify.apps.MarkdownifyConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Base url to serve media files
MEDIA_URL = 'media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
