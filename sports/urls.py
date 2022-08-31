from django.urls import path, include

from sports import views

app_name = 'sports'

urlpatterns = [
    path('events/', views.all_events, name='all_events'),
    path('events/<int:pk>/', views.event_object, name='event-object'),
]
