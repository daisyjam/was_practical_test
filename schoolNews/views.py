from django.shortcuts import render
from schoolNews.models import News

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!

    news_list = News.objects.order_by('-date')

    context_dict = {}
    context_dict['news'] = news_list
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'schoolNews/index.html', context=context_dict)

