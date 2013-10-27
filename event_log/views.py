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
        place = ''
        if target_event.dnf:
            place = 'DNF'
        elif target_event.finish_handicapped:
            place = str(target_event.finish_handicapped)
        elif target_event.finish_age_group:
            place = str(target_event.finish_age_group)
        elif target_event.finish_gender:
            place = str(target_event.finish_gender)
        elif target_event.finish_overall:
            place = str(target_event.finish_overall)
            
        if place.isdigit():
            if place.endswith('1'):
                place += 'st place'
            elif place.endswith('2'):
                place += 'nd place'
            elif place.endswith('3'):
                place += 'rd place'
            else:
                place += 'th place'
               
        bike_speed = ''
        if target_event.bike_distance and target_event.bike_time:
            bike_speed = target_event.bike_distance/(target_event.bike_time.hour + target_event.bike_time.minute/60 + target_event.bike_time.second/360)
        run_pace = ''
        if target_event.run_distance and target_event.run_time:
            run_pace = target_event.run_time.hour*60 + target_event.run_time.minute + target_event.run_time.second/60
            run_pace /= target_event.run_distance
            minutes = int(run_pace)
            seconds = int((run_pace-minutes)*60)
            run_pace =  str(minutes) + ':' + str(seconds)
                       
        return render_to_response('recap.html', {'event': target_event,
                                                 'css': ('%sevent_log/event_log.css' % settings.STATIC_URL),
                                                 'place': place,
                                                 'bike_speed': bike_speed,
                                                 'run_pace': run_pace,
                                                 })
    
class List(View):
    def dispatch(self, request, *args, **kwargs):
        return render_to_response('list.html', {'events': Event.objects.all(),
                                                'css': ('%sevent_log/event_log.css' % settings.STATIC_URL),
                                                'js_libs': '%sevent_log/js_libs/'%settings.STATIC_URL,
                                                })
