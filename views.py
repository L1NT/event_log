from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic.edit import View
from django.conf import settings
from django.shortcuts import render_to_response

from event_log.models import Event

class Recaps(View):    
    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('event'):
            event_id=request.GET.get('event')
        else:
            event_id=1
        #there's a better method to return a single row
        target_event = Event.objects.filter(id=event_id)[0]
        return render_to_response('recap.html', {'event': target_event,
                                                 'css': ('%sevent_log.css' % settings.STATIC_URL),})
    
class List(View):
    def dispatch(self, request, *args, **kwargs):
        return render_to_response('list.html', {'events': Event.objects.all(),
                                                'css': ('%sevent_log.css' % settings.STATIC_URL),})
