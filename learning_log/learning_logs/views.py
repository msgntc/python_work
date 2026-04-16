from django.shortcuts import render

from .models import Topic

def index(request):
    """the home page for learning_log"""
    return render(request, 'learning_logs/index.html')

def topic(request, topic_id):
    """show a single topic and all its ."""
    topic = Topic.objects.get(id=topic_id)
    entries = Topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)
