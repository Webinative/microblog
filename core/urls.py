from django.urls import path

from .views import home, post_detail

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path(
        "<int:year>/<int:month>/<int:day>/<int:post_id>/",
        post_detail,
        name="post_detail",
    ),
]
