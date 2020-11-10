from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.utils import timezone

# Create your views here.
def post_list(request):
    #posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})