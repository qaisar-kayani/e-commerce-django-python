
import os
from dotenv import load_dotenv
from mongoengine import connect
from pathlib import Path
import sys
from datetime import timedelta  

load_dotenv()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "utils"))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

SIMPLE_JWT = {
    'SIGNING_KEY': SECRET_KEY,
    'ALGORITHM': 'HS256',
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # other settings...
     # Use the correct claim where your user id (string) is stored inside the token
    'USER_ID_FIELD': 'id',  # or '_id' depending on your user model
    'USER_ID_CLAIM': 'user_id',

    # IMPORTANT: Disable token user id casting to int
    'TOKEN_USER_ID_CLAIM': 'user_id',

    # To disable conversion of user id to int
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',           # <--- Add this
    'django.contrib.contenttypes',   # Required by auth
    'django.contrib.sessions',       # Required by auth & middleware
    'django.contrib.messages',       # Optional but recommended
    'django.contrib.staticfiles',    # For static file serving
    'rest_framework',
    'registration',
    'products',
    'categories',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
     'utils.middleware.jwt_auth.JWTAuthMiddleware',
]


ROOT_URLCONF = 'ecommerce_project.urls'

TEMPLATES = [
]

WSGI_APPLICATION = 'ecommerce_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

connect(host=os.getenv("MONGO_URI"))

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
