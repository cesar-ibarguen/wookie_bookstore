from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.
def url(self,filecover):
    route = "cover/books_cover/%s/%s"%(self.title,str(filecover))
    return route

class Book(models.Model):
   # def cover_book(self):
    #    return mark_safe('<a href="/%s"> <img src="/%s" width=30px height=30px /> </a>'%(self.cover,self.cover))

    title = models.CharField(max_length=80, blank=False)
    description = models.CharField(max_length=8000, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to=url, blank=False)
    price = models.IntegerField(blank=False)
    year = models.IntegerField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title