from django.conf.urls import url,include
from django.contrib import admin

from . import views
from about import views as aboutViews
from data import views as dataViews
from concatenate import views as concatenateViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^data/', include('data.urls')),
    url(r'^concatenate/$', concatenateViews.index),
    #url(r'^about/$', aboutViews.index),
    #url(r'^data/$', dataViews.index),
    url(r'^$', views.index),
]
