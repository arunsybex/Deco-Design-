from django.urls import path
from djproject import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]