# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundCloud',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='cmsplugin_soundcloud_soundcloud', serialize=False, parent_link=True, primary_key=True, auto_created=True, to='cms.CMSPlugin')),
                ('url', models.CharField(help_text='(i. e. https://soundcloud.com/band/song)', max_length=255, verbose_name='Sound Cloud URL')),
                ('author_name', models.CharField(max_length=255, editable=False)),
                ('author_url', models.CharField(max_length=255, editable=False)),
                ('title', models.CharField(max_length=255, editable=False)),
                ('description', models.CharField(max_length=255, editable=False)),
                ('thumbnail_url', models.CharField(max_length=255, editable=False)),
                ('color', models.CharField(verbose_name='Color', help_text='Main color of the widget.', max_length=6, choices=[('ff6600', 'Default')], default='ff6600')),
                ('auto_play', models.BooleanField(verbose_name='Play automatically')),
                ('show_artwork', models.BooleanField(verbose_name='Show artwork')),
                ('hide_related', models.BooleanField(verbose_name='Hide related')),
                ('visual', models.BooleanField(verbose_name='Visual mode')),
                ('height', models.IntegerField(help_text='Height of widhte in visual mode.', verbose_name='Height', choices=[(300, 300), (450, 450), (600, 600)], default=300)),
                ('src', models.TextField(editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
