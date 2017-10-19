from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),                 ### Always need money sign
    url(r'^process_money/(?P<location>\w+)$',views.process),
    url(r'^22',views.clear)
]