from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

class Testimony(models.Model):
    witness = models.CharField(max_length=500)
    story = models.TextField()
    picture = FilerImageField(null=True, blank=True, related_name="+", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.witness


class TestimonyPluginModel(CMSPlugin):
    testimonies = models.ManyToManyField(Testimony)

    def copy_relations(self, oldinstance):
        self.testimonies = oldinstance.testimonies.all()
