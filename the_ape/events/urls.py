from django.conf import settings
from django.conf.urls import url

import events.views as views
import pages

urlpatterns = [
    url(r'^(?P<event_id>\d+)/purchase/$', views.event_ticket_purchase, name='event_ticket_purchase'),
    url(r'^(?P<event_id>\d+)', pages.views.EventWrapperView.as_view(), name='event_wrapper'),
]