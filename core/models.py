from django.db import models

# abstract을 통해 스키마가 생성되지 않도록 함.
# 이렇게 하면 core.models를 통해 스키마가 생성되지 않음.


class TimestampZone(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
