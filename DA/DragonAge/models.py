from django.db import models
from django.urls import reverse


class Classes(models.Model):
    first=models.CharField(blank=True, null=True,max_length=20)
    plot = models.CharField(blank=True, null=True, max_length=30000)
    img = models.ImageField(null=True, blank=True, upload_to='class/')
    def __str__(self):
        return self.first
    def url(self):
        return reverse('DragonAge:clasess_list')
class Race(models.Model):
    last=models.CharField(blank=True, null=True,max_length=20)
    img = models.ImageField(null=True, blank=True, upload_to='Race/')
    plot=models.CharField(blank=True, null=True,max_length=30000)
    def __str__(self):
        return self.last

    def url(self):
        return reverse('DragonAge:race_list')
class Locations(models.Model):
    lev=models.CharField(blank=True, null=True,max_length=20)
    plot =models.CharField(blank=True, null=True,max_length=2000)
    img = models.ImageField(null=True, blank=True, upload_to='Locations/')
    def __str__(self):
        return self.lev
    def url(self):
        return reverse('DragonAge:Locations_list')


class Game(models.Model):
    name=models.CharField(blank=True, null=True,max_length=200)
    creator=models.CharField(blank=True, null=True,max_length=20)
    release=models.IntegerField(default=0)
    plot=models.CharField(blank=True, null=True,max_length=30000)
    locations=models.ManyToManyField(Locations)
    race=models.ManyToManyField(Race)
    classes=models.ManyToManyField(Classes)
    img = models.ImageField(null=True, blank=True, upload_to='Game/')

    def __str__(self):
        return self.name
    def url(self):
        return reverse('DragonAge:game_detail', args=[self.id])


class Companion(models.Model):
    imy=models.CharField(blank=True, null=True,max_length=20)
    race = models.ForeignKey(Race, blank=True, null=True, on_delete=models.SET_NULL)
    classes = models.ForeignKey(Classes, blank=True, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(null=True, blank=True, upload_to='Companion/')
    game=models.ForeignKey(Game,blank=True, null=True, on_delete=models.SET_NULL)
    plot = models.CharField(blank=True, null=True, max_length=30000)
    def __str__(self):
        return self.imy
    def url(self):
        return reverse('DragonAge:Companion_detail', args=[self.id])
    class Meta:
        ordering=['imy']
