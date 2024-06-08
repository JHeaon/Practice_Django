from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-s&-zlu8x#uvq3(#0i=#+%mf-c^$0i0@4m&un489-(ar4o5ups^"
DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    # 장고 프로젝트의 모델 데이터를 관리하기 위한 강력한 인터페이스 제공
    "django.contrib.admin",
    # 장고 인증의 중심, 사용자 인증과 권한 부여 기능을 제공
    "django.contrib.auth",
    # 데이터베이스 외래키보다 유연한 외래키 GenericForeignKey 필드 지원
    "django.contrib.contenttypes",
    # 세션 지원, 여러 요청 간에 공유할 데이터를 저장/활용
    "django.contrib.sessions",
    # 1회성 성공/실패 메세지를 저장 및 표시
    "django.contrib.messages",
    # 개발 당시의 정적파일에 대한 관리를 지원
    "django.contrib.staticfiles",
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
        "NAME": BASE_DIR / "db.sqlite3",
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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
