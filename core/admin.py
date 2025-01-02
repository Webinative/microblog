from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, MicroBlogImage, MicroBlogPost


@admin.register(User)
class CoreUserAdmin(UserAdmin):
    """Custom UserAdmin for core.User model"""

    list_display = ["username", "is_active", "is_staff", "is_superuser"]
    list_filter = ("is_staff",)


class MicroBlogImageInline(admin.StackedInline):
    model = MicroBlogImage
    extra = 1


@admin.register(MicroBlogPost)
class MicroBlogPostAdmin(admin.ModelAdmin):
    list_display = ["compact_content", "created", "slug"]
    readonly_fields = ["content_html"]
    inlines = [
        MicroBlogImageInline,
    ]

    def compact_content(self, obj):
        return f"{obj.content_md[:48]}..."
