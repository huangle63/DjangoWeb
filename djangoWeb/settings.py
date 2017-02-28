from __future__ import absolute_import, unicode_literals
# ^^^ The above is required if you want to import from the celery
# library.  If you don't have this then `from celery.schedules import`
# becomes `proj.celery.schedules` in Python 2.x since it allows
# for relative imports by default.

"""
Django settings for djangoWeb project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.path.abspath(__file__)  本文件所在的绝对路径
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))    #文件所在的目录
BASE_DIR = os.path.dirname(PROJECT_ROOT)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0n_8q=1rg%6t@m3dhx**#*)yf%_0feuwt4!k1$0@9)3+hno3dp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','www.software.com','192.168.62.128','10.18.78.165']



# Celery settings
CELERY_ACCEPT_CONTENT = ['json']
CELERY_BROKER_URL= 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'
CELERY_TASK_SERIALIZER = 'json'


# Application definition

INSTALLED_APPS = [
    'bootstrap_admin',        #一定要放在`django.contrib.admin`前面
    'django.contrib.admin',    #默认添加后台管理功能
    'django.contrib.auth',     #管理用户的模块
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoWeb.west',
    'djangoWeb.core',
    'djangoWeb.iqc',
    'djangoWeb.jiradata',
    'djangoWeb.authentication',
    'django_celery_beat',   #在admin管理页面中可以创建定时任务
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

ROOT_URLCONF = 'djangoWeb.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
            # os.path.join(BASE_DIR, 'templates/west/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

WSGI_APPLICATION = 'djangoWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
            'ENGINE':'django.db.backends.mysql',
            'NAME': 'djangoweb',
            'USER': 'root',
            'PASSWORD': '123qwe',
            'HOST':'localhost',
            'PORT':'3306',
        }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'


# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True
# 如果不需要在程序中特别处理时区（timezone-aware），
# 在Django项目的settings.py文件中，可以直接设置为“USE_TZ = False”就省心了
USE_TZ = False


# AUTH_USER_MODEL = "authentication.Profile"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# @login_required标签,其作用就是告诉程序，使用这个方法是要求用户登录的
# 如果用户还没有登录，默认会跳转到‘/accounts/login/’。这个值可以在settings文件中通过LOGIN_URL参数来设定
# LOGIN_REDIRECT_URL 登录成功之后跳转的页面
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'

# 保存上传的图片位置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ALLOWED_SIGNUP_DOMAINS = ['*']

# session在服务器的有效时间为30分钟
# 会话cookie可以在用户浏览器中保持有效期。True：关闭浏览器，则Cookie失效。
SESSION_COOKIE_AGE = 60*30
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

