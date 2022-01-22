from django.shortcuts import render
from .models import Video
# Create your views here.


def Index(request):

    video = Video.objects.all()
    content = {"video": video}
    return render(request, "video.html", content)
