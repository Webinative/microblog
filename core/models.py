from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from markdown import markdown


class User(AbstractUser):
    """Custom user model"""

    class Meta:
        db_table = "mcr_users"


class TimestampedModel(models.Model):
    """An abstract base class model that provides self-updating 'created' and 'modified' fields"""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MicroBlogPost(TimestampedModel):
    content_md = models.TextField(max_length=255)
    content_html = models.TextField(blank=True, null=True)

    @property
    def slug(self):
        date_str = self.created.strftime("%Y/%m/%d")
        return f"{date_str}/{self.pk}"

    class Meta:
        db_table = "mcr_micro_blog_posts"
        ordering = ["-id"]

    def __str__(self):
        return self.slug

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """convert markdown to html before saving"""
        extensions = [
            "fenced_code",
            "tables",
            "sane_lists",
            "markdown_checklist.extension",
        ]
        self.content_html = markdown(self.content_md, extensions=extensions)
        return super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse(
            "core:post_detail",
            kwargs={
                "year": self.created.year,
                "month": self.created.month,
                "day": self.created.day,
                "post_id": self.pk,
            },
        )


class MicroBlogImage(TimestampedModel):
    post = models.ForeignKey(
        MicroBlogPost, related_name="images", on_delete=models.PROTECT
    )
    file = models.ImageField(upload_to="core/images/")

    class Meta:
        db_table = "mcr_micro_blog_images"

    def __str__(self):
        return self.file.url
