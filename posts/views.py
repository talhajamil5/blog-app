from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreateForm
from django.urls import reverse_lazy


def post_list(request):
    return render(request, "posts/index.html")


class Blogs(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"blog_entries": posts}
        return render(request, "posts/homepage.html", context=context)

    def post(self, request):
        pass


class CreatePost(CreateView):
    model = Post
    form_class = CreateForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy("blog_posts")


class UpdatePost(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog_posts")

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("blog_posts")