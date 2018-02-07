# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('witness', models.CharField(max_length=500)),
                ('story', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestimonyPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='testimony_testimonypluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('testimonies', models.ManyToManyField(to='testimony.Testimony')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
