from django.shortcuts import render

from .models import Topic

def index(request):
    """the home page for learning_log"""
    return render(request, 'learning_logs/index.html')

def topic(request):
    """show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)