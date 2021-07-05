from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static
 # a list of url instances
urlpatterns = [
    url('^$' , views.get_image,name='home'),
    url(r'^search/', views.search, name='searchr'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
