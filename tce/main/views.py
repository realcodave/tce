from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from operator import attrgetter
from .models import BlogPost


def Index(request):

    blog_post = sorted(BlogPost.objects.all(),
                       key=attrgetter('date_updated'), reverse=True)
    content = {"blog_post": blog_post}
    return render(request, "index.html", content)

def Article(request):
    
    blog_post = sorted(BlogPost.objects.all(),
                       key=attrgetter('date_updated'), reverse=True)
    content = {"blog_post": blog_post}
    return render(request, "article.html", content)


def Detail(request, slug):
	context = {}
	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post
	return render(request, "detail.html", context)


class About(TemplateView):
    template_name = 'about.html'


class LiveStream(TemplateView):
    template_name = 'project.html'
