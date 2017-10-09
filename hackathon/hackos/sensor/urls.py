from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^$', views.index ,name = "index") ,
    url(r'^get/$', views.getdata ,name ="get"),
    #url(r'^about.html/$', views.about,name ="get1")  
]
