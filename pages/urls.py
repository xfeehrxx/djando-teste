from django.urls import path 
from .views import HomeView, AboutView, PostView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='sobre'),
    path('post/', PostView.as_view(), name='post')
]