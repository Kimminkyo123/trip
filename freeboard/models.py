from django.db import models
from django.urls import reverse

class Freeboard(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField('one Line description', max_length=100, blank=True)
    upload_date = models.DateTimeField('up load Date', auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('freeboard:board_detail', args=(self.id,))

    class Meta:
        ordering =['upload_date']