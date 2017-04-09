from django.shortcuts import render
from .models import post

# Create your views here.
def main (request):
	return render(request, 'blog/main.html', locals())

def post_list (request):
	all_posts = post.objects.all
	return render(request, 'blog/list.html', locals())

def post_detail (request, post_id = 1):
	some_post = post.objects.get(id = post_id)
	return render(request, 'blog/post.html', locals())

