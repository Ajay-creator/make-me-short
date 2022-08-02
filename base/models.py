from django.db import models

# Create your models here.

class URLMapping(models.Model):
    suffix = models.CharField(max_length=250,primary_key=True,blank=True)
    url = models.URLField(max_length=500)


    def __str__(self) -> str:
        return self.suffix

    
