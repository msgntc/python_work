from django.shortcuts import render

def index(request):
    """the home page for learning_log"""
    return render(request, 'learning_logs/index.html')
