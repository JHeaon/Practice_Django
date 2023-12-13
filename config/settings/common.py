"""
장고 개발순서는 개발자마다 다르겠지만, ERD 도식을 보면서 개발하는 경우가 많기 때문에
MVT 패턴을 순서대로 개발하는 것을 추천한다.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-2*1ffkuyg%_4zg3meo@df9n6n(a$b1gl4g!-f^q@j%(r=d1b(#"

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom apps
    "api",
    "core",
    "blog",
    # Third party apps
    "django_seed",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db" / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# LOGGING 설정
# version : logging 모듈이 업그레이드 되어도, 현재 설정을 보장할수있도록 1을 권장하고 있다.
# disable_existing_loggers: 이전 로거들을 비활성화 하지 않고, 기본 로깅 구성을 유지하고 확장한다는 의미를 가지고 있다.
# filters : 특정조건에서 로그를 출력하거나, 출력하지 않게 하기 위해서 사용한다.
# formatters : 포맷터에 로그를 출력할 형식을 설정한다.

# handler : 로그를 출력할 방법에 대해서 정의한다.
# console: 콘솔에 로그 출력
# django.server: 개발 서버에서만 콘솔로 로그 출력
# mail_admins: 로그 레벨이 error이상이고, DEBUG=False일때 로그를 이메일로 전송, 환경설정에 ADMINS = ["j3heawon@naver.com"]과 이메일 발송을 위한 SMTP처리 또한 필요하다.

# logger: 로거를 정의한다.
# django: INFO 이상 레벨의 로그 메세지를 console 및 mail_admins 핸들러에 보낸다.
# django.server: INFO 이상 레벨의 로그 메세지를 django.server 핸들러로 보낸다. 해당 로거는 개발용 웹 서버인 runserver에서 사용하는 로거이다. 5xx응답은 ERROR, 4xx응답은 WARNING, 그 외는 INFO메세지로 출력한다.


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
        # 해당 내용은 커스텀한 내용입니다.
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        # 해당 내용은 커스텀한 내용입니다.
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs" / "debug.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        # 해당 내용은 커스텀한 내용입니다.
        "api": {
            "handlers": ["file"],
            "level": "DEBUG",
        },
    },
}

LANGUAGE_CODE = "en-us"

# TIME_ZONE = Aisa/Seoul로 변경할 경우 USE_TZ = False로 하는 것을 추천한다.
TIME_ZONE = "Asia/Seoul"
USE_TZ = False
USE_I18N = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
