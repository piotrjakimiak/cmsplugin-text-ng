# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextNG',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
            ],
            options={
                'verbose_name': 'text',
                'verbose_name_plural': 'texts',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TextNGTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('path', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextNGTemplateCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'template category',
                'verbose_name_plural': 'template categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextNGVariableText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20, verbose_name='label', validators=[django.core.validators.RegexValidator(regex=b'[_a-z]+', message='Only lower case characters.')])),
                ('value', models.TextField(null=True, verbose_name='value', blank=True)),
                ('text_ng', models.ForeignKey(related_name='+', to='cmsplugin_text_ng.TextNG')),
            ],
            options={
                'verbose_name': 'text',
                'verbose_name_plural': 'texts',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='textngtemplate',
            name='category',
            field=models.ForeignKey(blank=True, to='cmsplugin_text_ng.TextNGTemplateCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textng',
            name='template',
            field=models.ForeignKey(to='cmsplugin_text_ng.TextNGTemplate'),
            preserve_default=True,
        ),
    ]
