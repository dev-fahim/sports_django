from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone

from sports import queries as sports_queries

# Create your views here.
from sports.models import Group


@login_required
def all_events(request):
    events = sports_queries.get_all_events().order_by('id')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(events, 5)
    context = {
        'page_obj': paginator.get_page(page_number)
    }

    return render(request, 'sports/home.html', context=context)


@login_required
def event_object(request, pk: int):
    event = sports_queries.get_all_events().get(pk=pk)
    groups = Group.objects.filter()

    context = {
        'event': event,
        'now': timezone.now()
    }

    return render(request, 'sports/event-object.html', context=context)


@login_required
def home(request):
    events = sports_queries.get_all_events().order_by('id')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(events, 5)
    context = {
        'page_obj': paginator.get_page(page_number)
    }

    return render(request, 'sports/home.html', context=context)
