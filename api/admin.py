from django.contrib import admin
from .models import *


# inline객체를 통해서 한 화면에 여러 객체를 보여줄 수 있도록 설정함
# StackedInline: 스택형식으로 보여줌
# TabularInline: 테이블 형식으로 보여줌


class PublisherInline(admin.TabularInline):
    model = Publisher
    extra = 1


class AuthorInline(admin.TabularInline):
    model = Author
    extra = 1


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields detail 페이지에서 세부적인 필드를 보여줄 때 사용
    # list_display list 페이지에서 보여줄 필드를 설정할 때 사용
    # fields_set list 페이지에서 보여줄 필드를 그룹화할 때 사용
    # list_filter list 페이지에서 필터를 사용할 때 사용
    # search_fields list 페이지에서 검색을 사용할 때 사용
    # inlines detail 페이지에서 연결된 객체를 같이 보여줄 때 사용

    list_display = ("title", "publisher", "publication_date")
    fields = ("title", "authors", "publisher", "publication_date")
    list_filter = ("created_at",)
    search_fields = ("title", "publisher__name")

    # fieldsets = (
    #     ("기본 정보", {"fields": ("title", "content")}),
    #     ("추가 정보", {"fields": ()}),
    # )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ("name", "address", "website")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "salutation", "email")
