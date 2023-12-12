from django.contrib import admin
from .models import Post, Comment

# inline객체를 통해서 한 화면에 여러 객체를 보여줄 수 있도록 설정함
# StackedInline: 스택형식으로 보여줌
# TabularInline: 테이블 형식으로 보여줌
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields detail 페이지에서 세부적인 필드를 보여줄 때 사용
    # list_display list 페이지에서 보여줄 필드를 설정할 때 사용
    # fields_set list 페이지에서 보여줄 필드를 그룹화할 때 사용
    # list_filter list 페이지에서 필터를 사용할 때 사용
    # search_fields list 페이지에서 검색을 사용할 때 사용
    # inlines detail 페이지에서 연결된 객체를 같이 보여줄 때 사용

    inlines = [CommentInline]
    list_display = ("id", "title", "content", "created_at", "updated_at")
    fields = ("title", "content")
    list_filter = ("created_at",)
    search_fields = ("title", "content")

    # fieldsets = (
    #     ("기본 정보", {"fields": ("title", "content")}),
    #     ("추가 정보", {"fields": ()}),
    # )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "content", "created_at", "updated_at")
