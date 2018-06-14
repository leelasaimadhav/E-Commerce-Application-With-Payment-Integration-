from store import views
from django.urls import include,path

urlpatterns = [
    path('',views.store,name='index'),
    ]