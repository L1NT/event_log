from django.conf.urls import patterns, include, url

#File "/home/luke/src/django/django/core/urlresolvers.py", line 340, in urlconf_module
#    return self._urlconf_module
#AttributeError: 'RegexURLResolver' object has no attribute '_urlconf_module'
from event_log.views import Recaps, List

urlpatterns = patterns('',
    url(r'^recaps$', Recaps.as_view()),
    url(r'^event-list$', List.as_view()),
    url(r'', List.as_view()),
)
