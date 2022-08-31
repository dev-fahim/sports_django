from django.urls import path, include

from user_profile.views import user_login, user_signup, user_logout

app_name = 'user_profile'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', user_signup, name='signup')
]
