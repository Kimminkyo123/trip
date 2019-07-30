from django.db import models
from django.urls import reverse

class Freeboard(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField('one Line description', max_length=100, blank=True)
    upload_date = models.DateTimeField('up load Date', auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    star = models.ForeignKey('Star',on_delete=models.CASCADE, related_name='star' ,null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('freeboard:board_detail', args=(self.id,))

    class Meta:
        ordering =['upload_date']

class Star(models.Model):
    name = models.CharField(max_length=50)
    body = models.CharField('One Line Description', max_length=100, blank=True)
    img = models.ImageField(upload_to='star/',null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 