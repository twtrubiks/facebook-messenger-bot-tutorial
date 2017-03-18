from django.conf.urls import include, url
from .views import MyBotView

urlpatterns = [
    url(r'^callback/?$', MyBotView.as_view())
]
