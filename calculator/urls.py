"""calculator URL Configuration

"""
from django.conf.urls import url
from views import Multiply, Divide, Addition, Subtraction

urlpatterns = [
        url(r'^multiply/?$', Multiply.as_view()),
    url(r'^divide/?$', Divide.as_view()),
    url(r'^addition/?$',Addition.as_view()),
    url(r'^subtraction/?$',Subtraction.as_view()),
]
