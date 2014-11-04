from django.db import models

# Create your models here.
class app(models.Model):
    app_name = models.CharField(max_length = 100)
#    developers = models.CharField(max_length = 100)
    description = models.TextField(default = 'An App')
    link = models.URLField()
#    pic = models.FileField(upload_to='apps')
    rating = models.DecimalField(max_digits=3,decimal_places=2)
    
