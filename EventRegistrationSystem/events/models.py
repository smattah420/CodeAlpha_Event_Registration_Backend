from django.db import models

# Create your models here.

class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Registration(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
