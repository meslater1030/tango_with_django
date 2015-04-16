from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return self.first_name + " " + self.last_name
