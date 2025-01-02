# Generated by Django 4.2 on 2025-01-02 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MicroBlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("content_md", models.TextField(max_length=255)),
                ("content_html", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "mcr_micro_blog_posts",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="MicroBlogImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("file", models.ImageField(upload_to="core/images/")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="images",
                        to="core.microblogpost",
                    ),
                ),
            ],
            options={
                "db_table": "mcr_micro_blog_images",
            },
        ),
    ]