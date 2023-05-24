from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


def post_list(request):
    return render(request, "posts/index.html", context={"value": "1"})


class Blogs(View):
    def get(self, request):
        
        return render(request, "posts/homepage.html", context={"blog_entries": [{"title": "title1","name": "name1"}]})

    def post(self, request):
        pass
