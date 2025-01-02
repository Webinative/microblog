from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils import timezone

from .models import MicroBlogPost


def home(request):
    all_posts = MicroBlogPost.objects.order_by("-id")
    page = request.GET.get("page", 1)
    items_per_page = 5
    paginator = Paginator(all_posts, items_per_page)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "core/home.html", {"objects": posts})


def post_detail(request, year, month, day, post_id):
    target_date = timezone.datetime(year, month, day)
    post = MicroBlogPost.objects.get(created__date=target_date, id=post_id)
    return render(request, "core/post_detail.html", {"post": post})
