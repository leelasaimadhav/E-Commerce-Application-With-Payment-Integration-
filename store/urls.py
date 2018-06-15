from store import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^',views.store,name='index'),
    ]