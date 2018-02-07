#-*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import TestimonyPluginModel, Testimony


@plugin_pool.register_plugin  # register the plugin
class TestimonyPluginPublisher(CMSPluginBase):
    model = TestimonyPluginModel
    module = "Temoignages"
    name = "Liste des temoignages"
    render_template = "testimony/testimonies.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'testimonies' : instance.testimonies.all()
        })
        return context
