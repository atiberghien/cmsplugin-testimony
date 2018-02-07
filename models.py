from django.db import models
from cms.models import CMSPlugin

class Testimony(models.Model):
    witness = models.CharField(max_length=500)
    story = models.TextField()

    def __unicode__(self):
        return self.witness


class TestimonyPluginModel(CMSPlugin):
    testimonies = models.ManyToManyField(Testimony)
