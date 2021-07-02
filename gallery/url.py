from django.conf.urls import url 
from . import views
 # a list of url instances
urlpatterns = [
    url('^$' , views.welcome,name='welcome'),
]

