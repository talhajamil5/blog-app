from django.urls import path
from .views import post_list, Blogs, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path("blog-list", post_list, name="list"),
    path("blogs", Blogs.as_view(), name="blog_posts"),
    path("create", CreatePost.as_view(), name="create_post"),
    path("<pk>/update", UpdatePost.as_view(), name="update_post"),
    path("<pk>/delete", DeletePost.as_view(), name="delete_post"),
]
