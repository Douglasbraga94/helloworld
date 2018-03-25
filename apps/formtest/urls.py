from django.conf.urls import url, include
from . import views
from .views import principal

urlpatterns = [
	url(r'^$', principal.as_view(), name = "index"),
]