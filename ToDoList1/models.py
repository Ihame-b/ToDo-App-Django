from django.db import models

# Create your models here.
class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=True)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='img', blank=True, null=True, default='https://images.app.goo.gl/BJcJytaDin7V3Zw49')

    def __str__(self):
        return self.Title           