from django.db import models
from django.urls import reverse

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_lenght=200)
    nationaitly = models.CharField(max_lenght=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('band_detail', argd=[str(self.id)])

class Member(models.Model):
    name = models.CharField(max_lenght=200)
    dob = models.DateField()
    band = models.Foreignkey(
        Band,
        on_delete=models.CASCADE,
    
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member_detail', argd=[str(self.id)])   

class Song(models.Model):
    title = models.CharField(max_lenght=200)

    def __str__(self):
        return self.title

        def get_absolute_url(self):
        return reverse('song_detail', argd=[str(self.id)])
                 


