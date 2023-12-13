from django.apps import AppConfig


# 각 애플리케이션마다 필요한 항목을 설정하는 곳
# 별칭을 정의하거나 시그널 수신자를 등록하는 등의 작업을 할 수 있음
class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
    verbose_name = "Book-Author-Publisher App"
