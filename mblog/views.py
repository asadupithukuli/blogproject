from django.shortcuts import render
from mblog.models import Post

def index(request):
	post_list = Post.objects.order_by('created')[:5]
	context_dict = {'posts': post_list}

    # Render the response and send it back!
	return render(request, 'mblog/index.html', context_dict)

def post(request):

	post_list = Post.objects.order_by('created')[:5]
	context_dict = {'posts': post_list}

    # Render the response and send it back!
	return render(request, 'mblog/posts.html', context_dict)

	
	



