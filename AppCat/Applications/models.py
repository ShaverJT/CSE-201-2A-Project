import datetime
from django.db import models
from django.utils import timezone

# Create your models here.                                                                                                                                                           
class App(models.Model):
    app_name = models.CharField(max_length = 100)
    developers = models.CharField(max_length = 100, default='Anonymous')
    pub_date = models.DateTimeField('date published',default=timezone.now())
    description = models.TextField(default = 'An App')
    link = models.URLField()
    pic = models.URLField(default = 'http://i.imgur.com/E2Mwfu5.png')
    #models.FileField(upload_to='images/App_pic',default='images/App_pic/no_icon.png')
    approved = models.BooleanField(default=False)
    @property
    def rating(self):
        ratings = [i.rating for i in self.review_set.all()]
        if len(ratings) == 0:
            return 'Not Rated'
        return sum(ratings)/ len(ratings)
    
    def __str__(self):
        return self.app_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Review(models.Model):
    app = models.ForeignKey(App)
    review_name = models.CharField(max_length = 100)
    description = models.TextField(default = '')
    rating =  models.DecimalField(max_digits=1,decimal_places=0)
    def __str__(self):
        return self.review_name
