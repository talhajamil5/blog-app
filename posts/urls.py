from django.urls import path
from .views import post_list, Blogs

urlpatterns = [
    path("blog-list", post_list, name="list"),
    path("blogs", Blogs.as_view(), name= "blogs")
]