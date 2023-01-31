from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    cover = models.ImageField(name="cover")
    score = models.IntegerField()
    pub_date = models.DateTimeField("published datetime")

    def __str__ (self):
        return self.title

