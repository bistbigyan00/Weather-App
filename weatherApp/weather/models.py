from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length =200,unique=True)

    def __str__(self):
        return self.name

    #this fucntion saves all the name into capital first letter so
    # if we send city name paris, Paris, both will be changed into Paris and can't be dublicated
    def clean(self):
        self.name = self.name.title()

    class Meta:
        verbose_name_plural = 'cities'
