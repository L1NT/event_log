from django.contrib import admin

from event_log.models import SubSport, Sport, Event

class SportAdmin(admin.ModelAdmin):
    #how to hide this from the main admin menu?
    pass

class SubSportAdmin(admin.ModelAdmin):
    pass
   
class EventAdmin(admin.ModelAdmin):
    #group finishes; subgroup placing & finishers
    #filter SubSport by Sport
    #??? filter = [SubSport.objects.filter(sport=self.sport)]
    pass

admin.site.register(SubSport, SubSportAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Event, EventAdmin)   
