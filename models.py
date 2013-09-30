#models for Event Log

from django.db import models

class Sport(models.Model):
    sport = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['sport']
    
    def __unicode__(self):
        return self.sport
       
    def __str__(self):
        return self.sport

class SubSport(models.Model):
    sub_sport = models.CharField(max_length=20)
    sport = models.ForeignKey(Sport)
    
    class Meta:
        ordering = ['sport', 'sub_sport']
    
    def __unicode__(self):
        return str(self.sport) + ': ' + self.sub_sport
    
    def __str__(self):
        return str(self.sport) + ': ' + self.sub_sport

class Event(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    location = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport)
    sub_sport = models.ForeignKey(SubSport,blank=True,null=True)
    swim_distance = models.FloatField(blank=True,null=True)
    bike_distance = models.FloatField(blank=True,null=True)
    run_distance = models.FloatField(blank=True,null=True)
    recap = models.CharField(max_length=250)
    bib_number = models.IntegerField(blank=True,null=True)
    results_url = models.URLField(blank=True,null=True)
    finish_overall = models.IntegerField(blank=True,null=True)
    finishers_overall = models.IntegerField(blank=True,null=True)
    finish_gender = models.IntegerField(blank=True,null=True)
    finishers_gender = models.IntegerField(blank=True,null=True)
    finish_age_group = models.IntegerField(blank=True,null=True)
    finishers_age_group = models.IntegerField(blank=True,null=True)
    age_group = models.CharField(max_length=10,blank=True,null=True)
    finish_handicapped = models.IntegerField(blank=True,null=True)
    
    class Meta:
        ordering = ['date']
        
    def get_absolute_url(self):
        return "/events/recaps?event=%d" % self.id  
    
    def __unicode__(self):
        return self.name + '['+self.date.ctime()+']'
      
    def __str__(self):
        return self.name + '['+self.date.ctime()+']'