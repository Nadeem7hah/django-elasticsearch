
from django.contrib import admin
from django.urls import path
from  search_app.views import *
urlpatterns = [
    path('' , index),
    path('search/' , PublisherDocumentView.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
]
