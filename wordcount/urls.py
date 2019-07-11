
from django.urls import path
from . import views
a = "https://docs.djangoproject.com/en/2.2/intro/tutorial01/"
urlpatterns = [
    path("",views.homepage,name = 'home'),
    path("count/",views.count,name='count'),
    path("test/",views.test,name='test'),

]
